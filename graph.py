import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START, END, StateGraph

import json

from states import DictionaryState
from schemas import DeconstructionOutput, AssetOutput
from prompts import deconstrution_prompt, mission_briefing_prompt, asset_builder_prompt

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash", 
    temperature = 0.7, 
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def node_breakdown(state: DictionaryState):
    """Node 1: Breaks down the topic and extracts game mechanics."""
    structured_llm = llm.with_structured_output(DeconstructionOutput)
    chain = deconstrution_prompt | structured_llm
    
    try:
        response = chain.invoke({
            "engineering_topic": state["engineering_topic"],
            "video_game": state["video_game"]
        })
        
        # 1. Ideal Case: It returned the clean Pydantic object
        if hasattr(response, "core_principles"):
            return {
                "core_principles": response.core_principles,
                "game_mechanics": response.game_mechanics
            }
            
        # 2. Case: It returned a standard dictionary
        elif isinstance(response, dict):
            return {
                "core_principles": response.get("core_principles", ["Concept Error"]),
                "game_mechanics": response.get("game_mechanics", ["Mechanic Error"])
            }
            
        # 3. Case: LangChain returned the raw list/JSON string (Your current error)
        else:
            raw_text = ""
            if isinstance(response, list) and len(response) > 0:
                # Extract the text from the weird LangChain list
                raw_text = response[0].get("text", "") 
            elif hasattr(response, "content"):
                raw_text = response.content
            else:
                raw_text = str(response)

            # Strip any markdown formatting Gemini might have sneaked in
            raw_text = raw_text.replace("```json", "").replace("```", "").strip()
            
            # Manually parse the JSON
            parsed_json = json.loads(raw_text)
            
            return {
                "core_principles": parsed_json.get("core_principles", ["Parse Error"]),
                "game_mechanics": parsed_json.get("game_mechanics", ["Parse Error"])
            }

    except Exception as e:
        print(f"🚨 Node 1 Execution Error: {e}")
        # Ultimate fallback so Streamlit never crashes
        return {
            "core_principles": ["Fallback: Concurrency", "Fallback: Resource Allocation"],
            "game_mechanics": ["Fallback: Game Loop", "Fallback: Inventory Limits"]
        }

def node_analogy_engine(state: DictionaryState):
    """Node 2: Generates the NPC Mission Briefing."""
    chain = mission_briefing_prompt | llm
    
    core_principles = state.get("core_principles", ["General Concept"])
    game_mechanics = state.get("game_mechanics", ["General Mechanic"])
    
    response = chain.invoke({
        "engineering_topic": state.get("engineering_topic", "Engineering Concept"),
        "video_game": state.get("video_game", "Video Game"),
        "core_principles": ", ".join(core_principles),
        "game_mechanics": ", ".join(game_mechanics)
    })
    
    # EXTRACT CLEAN TEXT FROM GEMINI'S MESSAGE BLOCK
    content = response.content
    
    # If Gemini returns a list with metadata, extract just the text string
    if isinstance(content, list):
        text_parts = [block.get("text", "") for block in content if isinstance(block, dict) and "text" in block]
        final_text = "\n".join(text_parts)
    else:
        # If it's already a standard string, use it directly
        final_text = str(content)
    
    return {"narrative_explanation": final_text.strip()}

def node_interactive_assets(state: DictionaryState):
    """Node 3: Compiles the structured dictionary and quiz."""

    structured_llm = llm.with_structured_output(AssetOutput)

    chain = asset_builder_prompt | structured_llm

    response = chain.invoke({
        "narrative_explanation": state["narrative_explanation"]
    })

    # Convert Pydantic objects to standard Python dictionaries for Streamlit
    return{
        "dictionary_mapping": [item.model_dump() for item in response.dictionary_mapping],
        "quiz_questions" : [item.model_dump() for item in response.quiz_questions]
    }

# .model_dump() -> built in method that transform a pydantic class instance into a python dictionary. 
workflow = StateGraph(DictionaryState)

# 1. ADD THE NODES FIRST (If these are missing, it throws your exact error!)
workflow.add_node("node_breakdown", node_breakdown)
workflow.add_node("node_analogy_engine", node_analogy_engine)
workflow.add_node("node_interactive_assets", node_interactive_assets)

# 2. THEN CONNECT THE EDGES
workflow.add_edge(START, "node_breakdown")
workflow.add_edge("node_breakdown", "node_analogy_engine")
workflow.add_edge("node_analogy_engine", "node_interactive_assets")
workflow.add_edge("node_interactive_assets", END)

app_engine = workflow.compile()
