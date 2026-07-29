# TextAnalyser CLI
 
A fully interactive, keyboard-driven text analysis tool built with **vanilla Python** — no third-party CLI frameworks, just custom terminal rendering, arrow-key navigation, and a from-scratch analysis engine.
 
Write or import a `.txt` file and instantly get word/character statistics, keyword search & replace, an ASCII word cloud, and sentiment analysis — all navigated purely with your keyboard.
 
## Features
 
- **Interactive menu navigation** — move through options with `↑ / ↓` and `← / →`, confirm with `Enter`, and back out with `Esc`. No typing commands.
- **Two ways to provide text**
  - Write directly in a built-in text editor
  - Import an existing `.txt` file through a file picker dialog
- **Word Stats** — total word count, unique word count, keyword count, and a side-by-side table of the most frequent words vs. keywords
- **Character Stats** — character count, unique character count, and a full character-frequency table
- **Search** — find every occurrence of a word or phrase in the text
- **Replace** — swap out a word/phrase across the whole text
- **Word Cloud** — visualize word frequency as either a text-based cloud or bar chart, toggle between keywords-only and all words
- **Sentiment Analysis** — overall positive/negative sentiment breakdown, percentage of positive vs. negative sentences, and a color-coded sentence-by-sentence view
- Colorful, styled terminal output (custom-built styling, no external color libraries)
 

## Requirements
 
- **Python 3.x**
- **Windows OS** — the app currently relies on the `msvcrt` module for real-time keyboard input, which is Windows-only
- A terminal window at least **150 columns wide** (the app will prompt you to widen it if it's too narrow)
 
> Note: check the repo for a `requirements.txt` — if the word cloud / bar chart rendering or sentiment lexicon relies on additional packages (e.g. for visualization), install them with `pip install -r requirements.txt` before running.
 
## Installation
 
```bash
git clone https://github.com/HananMoAlnakhal/TextAnalyser_CLI.git
cd TextAnalyser_CLI
python main.py
```
 
## Usage
 
1. Run `python main.py`.
2. Choose whether to **write your text** in the built-in editor or **import a text file**.
3. Once analysis finishes, use the arrow keys to move through the main menu:
   - Words stats
   - Character stats
   - Search for a word
   - Replace word
   - Word Cloud
   - Text Sentiment
   - Try with new text
   - Exit
4. Press `Enter` to open a section, and `Esc` to return to the menu.
 
## Project Structure
 
```
TextAnalyser_CLI/
├── main.py            # Entry point — menu system and screen navigation
├── app/
│   ├── Analyzer.py     # Core text analysis engine (SmartTextAnalyzer)
│   ├── TextEditor.py   # Built-in interactive text editor
│   ├── predictor.py    # Keyword / prediction logic
│   ├── TEXTstyling.py  # Terminal color & text styling helpers
│   └── util.py         # Shared utilities (screen clearing, key detection, etc.)
├── lang_models/        # Language/sentiment data used by the analyzer
└── demo_data/           # Sample text files for testing
```
 
## How It Works
 
The CLI draws its own menus directly to the terminal using ANSI escape codes and cursor positioning, and listens for keypresses in real time via `msvcrt.kbhit()` — rather than waiting for a line of input like a typical `input()`-based script. This is what makes the arrow-key menu navigation possible without any external TUI library.
 
## Roadmap Ideas
 
- [ ] Cross-platform keyboard input (replace `msvcrt` with a library like `keyboard` or a custom solution for macOS/Linux)
- [ ] Save/export analysis reports and edited text to a file
- [ ] Add a `requirements.txt` / packaging (`pyproject.toml`) for easier setup
- [ ] Unit tests for the analysis engine
 
## Author
 
Made by **Hanan Mohamed Alnakhal**
