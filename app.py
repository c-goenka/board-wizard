import streamlit as st


st.title("Board Wizard")
st.markdown("This is your smart board game companion, instantly answering rule-related questions so you can focus on playing, not flipping through manuals.")
st.markdown("Simply ask about any game scenario, and get clear, accurate explanations from the official rulebooks—no more interruptions, just smooth and enjoyable gameplay!")
st.divider()

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("Example question: Which player goes first?"):
    with st.chat_message('user'):
        st.markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})
