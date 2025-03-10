import streamlit as st
from rag import load_game_rules, get_llm_response

st.title("Board Wizard")
st.markdown("This is your smart board game companion, instantly answering rule-related questions so you can focus on playing, not flipping through manuals.")
st.markdown("Simply ask about any game scenario, and get clear, accurate explanations from the official rulebooks—no more interruptions, just smooth and enjoyable gameplay!")

st.divider()

if 'messages' not in st.session_state:
    st.session_state.messages = []

game_list = [
    'Carcassonne', 'Clank', 'Codenames', 'Earth', 'Forrest Shuffle',
    'Jaipur', 'Love Letter', 'Quacks of Quedlinburg', 'Ra', 'Wingspan'
]

game_index = None
if 'current_game' in st.session_state and st.session_state.current_game:
    game_index = game_list.index(st.session_state.current_game)

game_selection = st.selectbox(
    "What game do you need assistance with?",
    game_list,
    index=game_index,
    placeholder="Select game"
)

if game_selection and ('current_game' not in st.session_state or game_selection != st.session_state.current_game):
    with st.spinner(f"Loading rules for {game_selection}..."):
        load_game_rules(game_selection)
    intro_message = f"Ask me anything about {game_selection}, and I'll help you navigate the rules!"
    st.session_state.messages = [{'role': 'assistant', 'content': intro_message}]

st.divider()

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input(f"How do I score points in {game_selection}?"):
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
