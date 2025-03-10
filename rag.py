import os
from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

from langchain import hub
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict

load_dotenv()
LANGSMITH_TRACING = "true"
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = init_chat_model("gpt-4o-mini", model_provider="openai")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
prompt = hub.pull("rlm/rag-prompt")

if 'game_loaded' not in st.session_state:
    st.session_state.game_loaded = False
    st.session_state.current_game = None
    st.session_state.vector_store = InMemoryVectorStore(embeddings)

@st.cache_data
def load_context(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )
    return text_splitter.split_documents(docs)


def load_game_rules(game_title: str):
    if not game_title:
        return False

    if 'game_loaded' in st.session_state and st.session_state.game_loaded and st.session_state.current_game == game_title:
        st.success(f"Rules for {game_title} loaded from cache")
        return True

    file_path = f"./documents/{game_title.lower()}.pdf"
    if not os.path.exists(file_path):
        st.error(f"Rules for {game_title} not found")
        st.session_state.game_loaded = False
        st.session_state.current_game = None
        return False

    st.session_state.vector_store = InMemoryVectorStore(embeddings)
    all_splits = load_context(file_path)
    st.session_state.vector_store.add_documents(documents=all_splits)

    st.session_state.game_loaded =  True
    st.session_state.current_game = game_title

    st.success(f"Rules for {game_title} loaded successfully")
    return True


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

def retrieve(state: State):
    retrieved_docs = st.session_state.vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}


graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

def get_llm_response(question: str):
    if 'game_loaded' not in st.session_state or not st.session_state.game_loaded:
        return "Please select a game first."
    response = graph.invoke({"question": question})
    return response['answer']
