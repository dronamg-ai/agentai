# app.py (Updated)
import streamlit as st
import brain
import tools
from io import StringIO

st.title("BATMAN's AI Assistant")

# --- SIDEBAR SETTINGS ---
st.sidebar.title("Agent Settings")
# 1. Add the Clear Chat Button
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.messages = []
    st.rerun() # Refresh the page to show an empty chat
    # 2. File Uploader
uploaded_file = st.sidebar.file_uploader("📁 Upload a .txt file for context", type=["txt"])
file_context = ""

if uploaded_file is not None:
    # Read file as string
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    file_context = stringio.read()
    st.sidebar.success(f"Loaded: {uploaded_file.name}")

persona = st.sidebar.selectbox(
    "Choose Astra's Personality:",
    ("Joker", "Alfred", "Robin", "Catwoman")
)

# Map the dropdown choice to a specific system prompt
prompts = {
    "Joker": "You are Joker, a witty and sarcastic assistant. Keep it brief.",
    "Alfred": "You are a formal, polite butler. Address the user as 'Master'.",
    "Robin": "You are an expert programmer. Explain concepts simply and provide code examples.",
    "Catwoman": "You are a high-energy fitness coach. Encourage the user to stay active!"
}
current_identity = prompts[persona]
# -----------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    user_input = prompt.lower()
    
    if "time" in user_input:
        response = f"The time is {tools.get_time()}"
    elif "date" in user_input:
        response = f"Today is {tools.get_date()}"
    elif "search" in user_input:
        query = user_input.replace("search", "").strip()
        response = tools.search_google(query)
    else:
        # Pass the 'current_identity' from the sidebar to the brain
        response = brain.ask_ai(prompt, current_identity)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
