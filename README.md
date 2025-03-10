# Board Wizard

Board Wizard is an AI-powered board game companion that helps players quickly find and understand rules without flipping through lengthy manuals. By selecting a game, users can ask questions about its rules, and Board Wizard retrieves relevant answers from official rulebooks using a Retrieval-Augmented Generation (RAG) model.

You can access the web application at https://boardwizard.streamlit.app!

![board-wizard-screenshot](https://github.com/user-attachments/assets/41eae8d6-a35a-47d8-b2b4-14ca5173aa9d)


## How It Works

1. **Select a Game**: Choose which board game you need help with
2. **Ask a Question**: Type any rule-related question about the game
3. **Get an Answer**: Board Wizard searches the official rulebook and provides a response


## Installation

1. Clone the repository
```bash
git clone https://github.com/c-goenka/board-wizard.git
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

4. Run the Streamlit application
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

- Carcassonne, Clank, Codenames, Earth, Forrest Shuffle, Jaipur, Love Letter, Quacks of Quedlinburg, Ra, and Wingspan

### How to Add New Games

1. Add the game's PDF rulebook to the `rulebooks` directory
2. Name the file according to the format: `game-name.pdf` (lowercase with hyphens)
3. Update the `game_list` in `app.py` to include the new game title


## Technology Stack & Tool Selection

### Python

- Simple, readable syntax makes development accessible and efficient
- Large community support and extensive AI/ML library ecosystem

### Streamlit

- Easy to prototype web applications with clean, intuitive user interfaces using only Python
- Simple API with great documentation and a strong community offering example applications

### LangChain

- Comprehensive RAG framework with great documentation and tutorials
- Customization and integration options for extensibility and advanced development

### OpenAI

- Natural-sounding text responses and strong context understanding
- Easy to set up and learn with well-documented API


## Development Process and Reflections

My goal was to create a RAG application that uses board game rulebooks as context to answer users’ questions. I ran into setup issues with Git, virtual environments, and dependencies, but with some help from ChatGPT and Stack Overflow, I got everything working. Once that was sorted, I began going through LangChain's RAG application documentation.

My plan was to first test the app with one game before expanding. I initially used PyPDFLoader but switched to PyPDFDirectoryLoader to handle multiple files together. The basic version successfully answered questions about the game 'Ra', but I realized that when multiple games were in context, it was hard to determine which one the question referred to.

For the frontend, I had heard about Streamlit from my brother as a great tool for prototyping, though limited for scaling. After looking into it, it seemed like a great tool for the job! I built a super simple Streamlit UI and gradually turned it into a full chatbot interface. Once I had user inputs working, I updated the app to load one PDF at a time based on the selected game.

Connecting the backend to the UI was a bit difficult, especially with caching and state persistence. Debugging involved tracing the data flow at each step, and after a lot of trial and error, I finally got the RAG context to persist correctly. After that, When trying to make my GitHub repository public, I realized that I was accidentally pushing my .env file to GitHub and had to clean the repository history with some risky Git commands (lol).

Once the core functionality was working, I deployed the app through Streamlit and added final touches: improved caching speed and feedback, automatic chat clearing when switching games, new example question, updated agent prompt, and support for additional games. There was one final bug, where the agent introduction was being displayed twice, and fixing it turned out to be surprisingly tricky since it required understanding how Streamlit reloads pages after changes. But after some Stack Overflow searching (and help from Claude), I figured out that I needed to manually rerun the app to properly clear old messages. With that, everything finally looked and worked as I had hoped!


## Future Work

- User testing to gauge helpfulness of application
- Gather feedback for improvements and continued development
- Support for more board games
- OCR image to text conversion using the Unstructured library
- Voice input for more natural, hands-free usage
- Download or view game rulebook
- Game specific images and icons
- Mobile app version
