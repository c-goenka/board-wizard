# Rag App Documentation

## Setup
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt -q -U
4. streamlit run app.py

## Tools
- Python (programming language)
- Streamlit (python based web framework for AI/ML applications)
- LangChain (rag library)
- OpenAI (llm)

## Development Process
- Goal: Rag App that uses board game rules documents as context and answers user's questions about the game
- Some setup issues with git, venv, and pip that took some ChatGPT and stackoverlfow to fix
- Built simple Streamlit UI
- Reading and understanding LangChain implementation
- Current plan: build first version and test for one game. if it works well then add additional features
- Going through the tutorial to implement the basic
- I want to load PDFS. Started using PyPDFLoader. I need it for many files so found PyPDFDirectoryLoader
- Went through all of tutorial and have a basic version working. Answered a question about Ra correctly
- I'm realizing that if I have multiple games in context, its hard to decide which game the question is about.
