import streamlit as st
from rag import load_game_rules, get_llm_response

st.title("Board Wizard")
st.markdown("This is your smart board game companion, instantly answering rule-related questions so you can focus on playing, not flipping through manuals.")
st.markdown("Simply ask about any game scenario, and get clear, accurate explanations from the official rulebooks—no more interruptions, just smooth and enjoyable gameplay!")

st.divider()

game_list = [
    'Ra', 'Quacks'
]

game_selection = st.selectbox(
    "What game do you need assistance with?",
    game_list,
    index=None,
    placeholder="Select game"
)

if game_selection:
    with st.spinner(f"Loading rules for {game_selection}..."):
        load_game_rules(game_selection)

st.divider()

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("Example question: Which player goes first?"):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        ai_response = get_llm_response(prompt)

    if not ai_response:
        ai_response = "I'm not sure. Try rephrasing your question."

    st.session_state.messages.append({'role': 'assistant', 'content': ai_response})
    with st.chat_message('assistant'):
        st.markdown(ai_response)
