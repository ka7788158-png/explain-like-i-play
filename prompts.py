from langchain_core.prompts import ChatPromptTemplate

# Node : Deconstruction point
deconstrution_prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "Your are an expert Sofware Engineer and a hardcore gamer."
     "your task is to analyze the engineering topic '{engineering_topic} and the video game '{video_game}'" 
     "Break down the topic into core principles and extract the mechanics from the game. "
     "that could be used as analogies."
), 
("user", "Execute the deconstruction.")
])

# Node 2: Missing breifing prompt {Analogy Engine}
mission_briefing_prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are the in-game NPC Mission Commander for the game '{video_game}'. "
     "Your objective is to explain the complex engineering concept of '{engineering_topic}' "
     "to the player, disguised as a critical in-game mission briefing. "
     "\n\nIncorporate these core engineering principles: {core_principles}"
     "\nMap them to these game mechanics: {game_mechanics}"
     "\n\nSpeak directly to the player. Be immersive, use the jargon of the game, "
     "and maintain the tone of a high-stakes tutorial or tactical briefing."
    ),
    ("user", "Give me my mission briefing.")
])

# Node 3: Asset Builder Prompt
asset_builder_prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are a technical documentation assistant. Based on the following mission briefing: "
     "\n\n{narrative_explanation}\n\n"
     "Extract the analogies into a structured dictionary mapping the engineering terms to the game mechanics. "
     "Then, generate 2 challenging multiple-choice questions that test the user's understanding of the engineering topic "
     "using the game's logic."
    ),
    ("user", "Generate the dictionary and quiz assets.")
])
