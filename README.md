# Board Wizard

Board Wizard is an AI-powered board game companion that helps players quickly find and understand rules without flipping through lengthy manuals. By selecting a game, users can ask questions about its rules, and Board Wizard retrieves relevant answers from official rulebooks using a Retrieval-Augmented Generation (RAG) model.

You can access the web application at https://boardwizard.streamlit.app!


## How It Works

1. **Select a Game**: Choose which board game you need help with
2. **Ask a Question**: Type any rule-related question about the game
3. **Get an Answer**: Board Wizard searches the official rulebook and provides a response


## Installation

1. Clone the repository
```bash
https://github.com/c-goenka/board-wizard.git
```

2. Navigate into the project directory
```bash
cd board-wizard
```

3. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Set up environment variables
- Create a .env file in the project root folder and add your API keys:
```

OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
```

4. Run the Streamlit aplication
```bash
streamlit run app.py
```


## Project Structure

```
board-wizard/
├── app.py              # Streamlit frontend application
├── rag.py              # LangChain RAG implementation
├── rulebooks/          # PDF rulebooks for supported games
├── requirements.txt    # Project dependencies
└── .env                # Environment variables (not tracked in git)
```


## Supported Games

- Carcassonne, Clank, Codenames, Earth, Forrest Shuffle, Jaipur, Love Letter, Quacks of Quedlinburg, Ra, Wingspan

### How to Add New Games

1. Add the game's PDF rulebook to the `rulebooks` directory
2. Name the file according to the format: `game-name.pdf` (lowercase with hyphens)
3. Update the `game_list` in `app.py` to include the new game title


## Technology Stack & Tool Selection

### Streamlit (frontend)

- Easy to prototype web applications with clean, intuitive user interfaces using only Python
- Simple API with great documentation and a strong community offering example applications

### Python (backend)

- Simple, readable syntax makes development accessible and efficient
- Large community support and extensive AI/ML library ecosystem

### LangChain (rag implementation)

- Comprehensive RAG framework with great documentation and tutorials
- Customization and integration options for extensibility and advanced development

### OpenAI (large language model)

- Natural-sounding text responses and strong context understanding
- Easy to set up and learn with well-documented API


## Development Process and Reflections (INCOMPLETE)

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
- accidentally push .env. used git commands to remove from history. added gitignore
- fixed state persistance to store rag context after reloads
- working app deployed with streamlit
- want to add agent intro when game is selected and check if caching is working correctly
- final touch features: fixed caching, added intro, clear chat when new game is selected, new example question,
    early cache check, updated prompt, added additional games
- weird bug where only sometimes the intro is displayed twice
- fixed intro message ghosting
- adding final documentation


## Future Work

- Support for more board games
- OCR image to text conversion using the Unstructured library
- Voice input for more natural, hands-free usage
- Download or view game rulebook
- Game specific images and icons
- Mobile app version
