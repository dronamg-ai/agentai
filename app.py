# app.py
import streamlit as st
import brain
import tools

st.title(" BATAGENTIC-Why so Serious")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What's up?"):
    # Display user message in chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process "Hands" (Tools) or "Brain"
    user_input = prompt.lower()
    
    if "time" in user_input:
        response = f"The time is {tools.get_time()}"
    elif "date" in user_input:
        response = f"Today is {tools.get_date()}"
    elif "search" in user_input:
        query = user_input.replace("search", "").strip()
        response = tools.search_google(query)
    else:
        # Get response from your local Ollama brain
        response = brain.ask_ai(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
