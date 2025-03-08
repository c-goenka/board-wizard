import streamlit as st


st.title("Rag App")

with st.form("rag_input_form"):
    text = st.text_area(
        "Enter your question"
    )
    submitted = st.form_submit_button("Submit")
