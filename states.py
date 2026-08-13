from typing import TypedDict, List, Dict, Any

class DictionaryState(TypedDict): 

    # this is for giving the input to the first node 
    # this we will get by help of streamlit -> form -> st.form

    engineering_topic : str
    video_game : str

    # this is for Node 1 -> recieving the output from the Node 1 
    core_principle : List[str]
    game_mechanics : List[str]

    # Node2: recieve the output from the Node 2 
    narrative_explanation : str

    # 4. Outputs from Node 3 (Asset Builder)
    # Formatted specifically for st.data_editor
    dictionary_mapping: List[Dict[str, Any]] # List that contains multiple Dictionaries.

    # Formatted for our interactive expander UI
    quiz_questions: List[Dict[str, Any]]

