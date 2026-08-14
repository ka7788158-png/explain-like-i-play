import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START, END, StateGraph

from states import DictionaryState
from schemas import DeconstructionOutput, AssetOutput
from prompts import deconstrution_prompt, mission_briefing_prompt, asset_builder_prompt

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "Gemini 3.1 Flash Lite", 
    temperature = 0.7, 
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def node_breakdown(state: DictionaryState):
    """Node 1: Breaks down the topic and extracts game mechanics."""
    structured_llm = llm.with_structured_output(DeconstructionOutput)
    chain = deconstrution_prompt | structured_llm

    response = chain.invoke({
        "engineering_topic" : state["engineering_topic"], 
        "video_game": state["video_game"]
    })

    # Update the state with the exact lists
    return {
        "core_principles": response.core_principles, 
        "game_mechanics" : response.game_mechanics
    }

def node_analogy_engine(state : DictionaryState):
    "Node 2: "
    # narrative_explanation
    # Standard text generation (no structured output needed here)

    chain = mission_briefing_prompt | llm

    response = chain.invoke({
        "engineering_topic": state["engineering_topic"],
        "video_game": state["video_game"],
        "core_principles": ", ".join(state["core_principles"]),
        "game_mechanics": ", ".join(state["game_mechanics"])
    })

    return {"narrative_explanation" : response.content}

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
        "quiz_questions" : [item.model_sump() for item in response.quiz_questions]
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
