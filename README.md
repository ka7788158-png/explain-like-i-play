# EXPLAIN IT LIKE I PLAY
**PROJECT TRACK** 
selected from Category F: Accessibility & Advanced Utilities
Project - 29 -> The "Explain it Like I Play" Dictionary: Users select a favorite video game (like
Minecraft or Valorant) and input a complex engineering topic. The AI explains the concept
entirely through the mechanics of that specific game.

**STATUS:** `ONLINE` || **THREAT LEVEL:** `HIGH` || **FRAMEWORK:** `LANGGRAPH + GEMINI`

> "Complex engineering concepts, mapped directly into the video games you already understand."

![UI Preview] 

<img width="1910" height="866" alt="image" src="https://github.com/user-attachments/assets/87fe5386-6bed-4c1e-bfbd-cb938c8bdf0e" />
* Game Like Theme
<img width="1905" height="845" alt="image" src="https://github.com/user-attachments/assets/7aa31390-b5dd-44e0-9e10-170beb5c86c2" />
* Every Node Visible , Improve User experience
<img width="1895" height="607" alt="image" src="https://github.com/user-attachments/assets/c6d5c028-7642-41f8-adcb-5ebb2f674844" />
<img width="1883" height="655" alt="image" src="https://github.com/user-attachments/assets/ee2e7e84-618c-4208-a65f-37f04550494d" />
<img width="1773" height="653" alt="image" src="https://github.com/user-attachments/assets/f2fbd85e-dc66-4aa7-8884-11182c00513f" />
* Mission briefing available in **Audio format**
<img width="1818" height="339" alt="image" src="https://github.com/user-attachments/assets/f6fa7c92-924c-4ee5-ab92-e8a570f23433" />

<img width="1832" height="337" alt="image" src="https://github.com/user-attachments/assets/b8d6f8f2-9b8e-4482-853c-57bee3b067a8" />
* Questions to check Your Knowledge
<img width="858" height="197" alt="image" src="https://github.com/user-attachments/assets/dad37930-2eef-4467-9c84-a63bf6ce75ed" />

* Downloding as PDF option also available

<img width="1353" height="457" alt="image" src="https://github.com/user-attachments/assets/b53a3d47-97d5-4ec7-9ddc-c24ba6d94de4" />
* Can even ask a follow UP questions as well. 

---

## 📡 [ACCESS LIVE TRANSMISSION HERE]
**Link:** ->  https://explain-like-i-play.streamlit.app/

## 🛠️ MISSION BRIEFING (Overview)
**Explain it Like I Play** is a highly interactive, agentic AI application built to translate complex computer science and engineering topics into video game mechanics. 

By leveraging a cyclical **LangGraph** state machine and the **Gemini 1.5 Flash** multimodal LLM, the system processes text or voice commands to generate a personalized "Mission Briefing." It outputs dynamic audio (TTS), a conceptual dictionary mapping table, and an interactive quiz—all wrapped in a custom-built, responsive 8-bit esports dashboard.

---

## ⚙️ SYSTEM ARCHITECTURE 
The backend engine utilizes a fault-tolerant, stateful graph execution model to ensure data structuring is strictly maintained between LLM calls.

```mermaid
graph TD
    A[User Input: Text / Voice Mic] -->|Streamlit Frontend| B(State Machine Initialization)
    B --> C{LangGraph Engine}
    C -->|Node 1| D[Generate Game Analogy & Narrative]
    C -->|Node 2| E[Construct Dictionary Mapping]
    C -->|Node 3| F[Generate Tactical Quiz]
    D --> G(Update Global State)
    E --> G
    F --> G
    G --> H[Synthesize Briefing Audio TTS]
    G --> I[Pollinations.ai Image Generation]
    H --> J[Render Gamer UI HUD]
    I --> J
    J --> K[Interactive Comms Channel / Chat Memory]
```
# 🚀 DEPLOYMENT INSTRUCTIONS: EXPLAIN IT LIKE I PLAY

## ☁️ Option 1: Live Cloud Deployment (Streamlit Community Cloud)
Streamlit Community Cloud lets you deploy your apps in just one click. Follow these exact steps to host your app live on a secure HTTPS connection (which automatically enables the browser microphone permissions):

**Step 1: Push code to GitHub**
* Ensure your entire codebase (`app.py`, `graph.py`, `utils.py`, `requirements.txt`) is committed and pushed to your public GitHub repository.

**Step 2: Connect to Streamlit Cloud**
* Go to [share.streamlit.io](https://share.streamlit.io/) and click "Continue with GitHub" to log into your account.
* Once in your workspace, click the **"Create app"** button in the upper-right corner.

**Step 3: Configure the App Repository**
* **Repository:** Pick your project's GitHub repo from the dropdown menu.
* **Branch:** Select `main` (or whichever branch holds your final code).
* **Main file path:** Type in `app.py` as your entrypoint.

**Step 4: Inject API Secrets**
* Before you click Deploy, you must click on **"Advanced settings"**.
* In the "Secrets" text field, paste your API keys. *Note: Streamlit Cloud uses TOML format instead of a standard `.env` file, so format it exactly like this*:
  ```toml
  GOOGLE_API_KEY="your_gemini_key_here"
  LANGCHAIN_API_KEY="your_langsmith_key_here"
  LANGCHAIN_TRACING_V2="true"
  LANGCHAIN_PROJECT="explain-like-i-play"
  ```
* Click "Save".

**Step 5: Launch the Application**
Click "Deploy!". Your app will begin building and will launch in a few minutes. Any time you push new code to GitHub, your live app will update immediately.

## 🏆 TECHNICAL METRICS
* Multimodality: Integrated st.audio_input for direct voice-to-text processing via Gemini.

* UI/UX: Custom CSS injection overriding native Streamlit components for a unified, dark-mode 8-bit aesthetic.

* Memory Management: Sliding-window context architecture for the Tactical Comms Channel (Chatbot) to prevent token overflow.

**OPERATIVE LOG: Developed by Kavya Agrawal | B.Tech Artificial Intelligence & Machine Learning (2024-2028).**

