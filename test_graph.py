from graph import app_engine

def run_test(): 
    print("Initializing LangGraph Engine...")

    initial_state = {
        "engineering_topic": "Deadlocks in Operating Systems", 
        "video_game" : "Minecraft", 
        "core_principles": [], 
        "game_mechanics": [], 
        "narrative_explanations": "", 
        "dictionary_mapping": [], 
        "quiz_questions": []
    }

    print(f"🎮 Topic: {initial_state['engineering_topic']} | Game: {initial_state['video_game']}\n")
    print("⏳ Running graph... (Check LangSmith for live traces!)")

    # Invoke the graph
    final_state = app_engine.invoke(initial_state)

    # Print the final results to the terminal
    print("\n✅ --- GRAPH EXECUTION COMPLETE --- ✅\n")
    
    print("📜 MISSION BRIEFING (Node 2 Output):")
    print(final_state["narrative_explanation"])

    print("\n📚 DICTIONARY MAPPING (Node 3 Output):")
    for item in final_state["dictionary_mapping"]:
        print(f"- {item['engineering_term']} -> {item['game_mechanic_equivalent']} ({item['complexity_score']})")

    print("\n🧠 QUIZ QUESTION (Node 3 Output):")
    if final_state["quiz_questions"]:
        print(f"Q: {final_state['quiz_questions'][0]['question']}")
        print(f"Answer: {final_state['quiz_questions'][0]['correct_answer']}")

if __name__ == "__main__":
    run_test()
