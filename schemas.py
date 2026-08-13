# we will use Pydantic here , so to get the output in the format we wanted to get 

from pydantic import BaseModel, Field
from typing import List 

class DeconstructionOutput(BaseModel):
    """Schema for Node 1: Deconstructs the topic and game."""

    core_principles : List[str] = Field(description = "List of 3 to 5 core engineering topic.")

    game_mechanics : List[str] = Field(description= "A list of 3 to 5 key mechanics from the selected video game.")

class DictionaryItem(BaseModel): 
    """Schema for a single row in the st.data_editor table."""
    engineering_term : str = Field(description= "the techinical engineering term.")
    game_mechanic_equivalent : str = Field(description = "The equivalent mechanic in the selected game.")
    in_game_function: str = Field(description="A short explanation of how the game mechanic mirrors the engineering concept.")
    complexity_score: str = Field(description="A complexity score out of 5 (e.g., '3/5').")

class QuizQuestion(BaseModel):
    """Schema for an interactive quiz question."""
    question : str = Field(description = "A question testing the engineering concept using the game's mechanics.")
    options : List[str] = Field(description = "A list of 4 multiple-choice options (A, B, C, D).")
    correct_answer : str = Field(description= "The exact string of the correct option.")
    explanation : str = Field(description = "A brief explanation of why this answer is correct.")

class AssetOutput(BaseModel):
    """Schema for Node 3: The final compiled dictionary and quiz."""
    dictionary_mapping: List[DictionaryItem]
    quiz_questions: List[QuizQuestion]
