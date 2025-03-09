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
- Now to work on the front end to get this progress showing up nicely
- wanting to go through streamlit documentation to understand the creative limits
- Read up on streamlit: seems very basic and not scalable, but very easy to prototype something with
    pretty decent ui. I think its worth going with this. If after some testing, the app seems to be
    helpful for users. I will switch to FastAPI to scale.
- Working through streamlit examples to understand how to create chat bot front end and its design
    options
- Created basic streamlit chat bot setup
- Editing application to load one pdf at a time before advancing on UI
- UI is setup
- Difficulty connecting backend to UI
- going through data flow and writing the output at each stage
- Using LLm to figure out but not much luck
- looks like it only works when the app is first run. After a reload, it stops working. The data is not being cached correclty?
