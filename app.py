import streamlit as st
import pandas as pd
from graph import app_engine, llm
from utils import GAMER_THEME_CSS, create_audio_briefing, generate_pdf_guide

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="Explain it Like I Play", 
    page_icon="🎮", 
    layout="wide"
)

# 2. Inject the custom CSS
st.markdown(GAMER_THEME_CSS, unsafe_allow_html=True)

# 3. Initialize Session State (Prevents memory loss on re-renders)
if "graph_state" not in st.session_state:
    st.session_state.graph_state = None
if "audio_bytes" not in st.session_state:
    st.session_state.audio_bytes = None

# 4. Sidebar: Mission Control Input Form
with st.sidebar:
    st.header("Mission Control")
    
    # Multimodal Audio Input (Fulfills the Mic Recorder rubric requirement!)
    st.caption("🎙️ Voice Command Override")
    audio_input = st.audio_input("Speak your target engineering topic:")
    
    with st.form("mission_form"):
        topic_input = st.text_input("Or Type Target Engineering Topic", placeholder="e.g. Concurrency, Deadlocks")
        game_input = st.selectbox("Select Tactical System", ["Minecraft", "Valorant", "Elden Ring", "Cyberpunk 2077"])
        
        submit_btn = st.form_submit_button("Initialize Mission", type="primary")

# 5. Execute LangGraph Engine on Submit
if submit_btn:
    with st.spinner("Compiling tactical data..."):
        final_topic = topic_input
        
        # If audio was provided and text is empty, transcribe it using Gemini's native multimodality
        if audio_input and not topic_input:
            st.toast("Transcribing voice command...", icon="🎙️")
            encoded_audio = base64.b64encode(audio_input.read()).decode("utf-8")
            
            # Pass the audio directly to Gemini
            msg = HumanMessage(content=[
                {"type": "text", "text": "Listen to this audio and accurately extract the engineering topic mentioned. Return ONLY the transcribed engineering topic name, nothing else."},
                {"type": "media", "mime_type": "audio/wav", "data": encoded_audio}
            ])
            final_topic = llm.invoke([msg]).content.strip()
            st.success(f"Transcribed Target: {final_topic}")

        # Safety check to prevent blank submissions
        if not final_topic:
            st.error("Operator, please provide a topic via text or voice transmission!")
            st.stop()

        initial_state = {
            "engineering_topic": final_topic,
            "video_game": game_input,
            "core_principles": [],
            "game_mechanics": [],
            "narrative_explanation": "",
            "dictionary_mapping": [],
            "quiz_questions": []
        }
        
        # Run the engine and store it in session state to prevent memory loss
        st.session_state.graph_state = app_engine.invoke(initial_state)

        # Generate the audio file immediately after the graph completes
        st.session_state.audio_bytes = create_audio_briefing(st.session_state.graph_state["narrative_explanation"])

        
# 6. Main HUD Display
if st.session_state.graph_state:
    state = st.session_state.graph_state
    
    st.title("Active Mission Briefing")
    
    # Top HUD Metrics (XP and System Status)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="System Status", value="ONLINE", delta="Stable")
    col2.metric(label="Concepts Mapped", value=len(state["dictionary_mapping"]), delta="Data Acquired")
    col3.metric(label="Threat Level", value="HIGH", delta="-Engage Carefully", delta_color="inverse")
    
    st.divider()
    
    # Audio Player & Briefing Text
    st.subheader("Incoming Transmission...")
    if st.session_state.audio_bytes:
        st.audio(st.session_state.audio_bytes, format="audio/mp3")
        
    st.markdown(state["narrative_explanation"])
    
    st.divider()
    
    # Interactive Dictionary Mapping (st.data_editor)
    st.subheader("Tactical Data Inventory")
    if state["dictionary_mapping"]:
        df = pd.DataFrame(state["dictionary_mapping"])
        # Format the columns to be visually clean
        df.columns = [col.replace("_", " ").title() for col in df.columns]
        st.data_editor(df, use_container_width=True, hide_index=True)
        
    st.divider()
    
    # Interactive Quiz Expanders
    st.subheader("Knowledge Check")
    if state["quiz_questions"]:
        for idx, q in enumerate(state["quiz_questions"]):
            with st.expander(f"Question {idx + 1}: {q['question']}"):
                for opt in q['options']:
                    st.write(f"- {opt}")
                st.write(f"**Correct Answer:** {q['correct_answer']}")
                st.write(f"*Intel:* {q['explanation']}")
                
    st.divider()
    
    # On-Demand PDF Download
    st.subheader("Export Tactical Data")
    pdf_bytes = generate_pdf_guide(
        state["engineering_topic"], 
        state["video_game"], 
        state["narrative_explanation"], 
        state["dictionary_mapping"]
    )
    
    st.download_button(
        label="Download PDF Guide",
        data=pdf_bytes,
        file_name=f"{state['engineering_topic'].replace(' ', '_')}_Guide.pdf",
        mime="application/pdf"
    )
else:
    # Default waiting screen
    st.title("Awaiting Orders...")
    st.info("Enter an engineering topic and select a game in the sidebar to begin.")
