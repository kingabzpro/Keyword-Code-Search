# Keyword-Based Code Search with GPT-4.1

This project provides a lightweight solution for performing keyword-based searches on your codebase and then uses GPT‑4.1 to generate detailed answers or explanations based on the relevant code snippets. The tool extracts context (two lines before and after each match) and builds a prompt including your question and the corresponding code snippets.

## Features
- **Keyword-Based Search**: Search through your codebase using keywords extracted from your questions
- **Code Snippet Display**: View relevant code snippets with file paths and line numbers
- **AI Explanations**: Get explanations of the code snippets using GPT-4.1
- **Interactive Mode**: Chat with the tool in a conversational manner
- **Streaming Responses**: See AI explanations as they're being generated in real-time

## Requirements
- Python 3.8+
- OpenAI Python library (for interacting with GPT‑4.1)
- An OpenAI API key with access to GPT‑4.1

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/keyword_code_search.git
   cd keyword_code_search
   ```

2. **Install dependencies:**

   ```bash
   pip install openai
   ```

## Environment Setup

Set your OpenAI API key in the environment variable:

- On macOS/Linux:

  ```bash
  export OPENAI_API_KEY="YOUR_API_KEY_HERE"
  ```

- On Windows (Command Prompt):

  ```cmd
  set OPENAI_API_KEY=YOUR_API_KEY_HERE
  ```


## Usage

### Basic Usage
This will prompt you to enter a question about the codebase and display relevant code snippets.
```bash
python main.py --path /path/to/your/codebase
```

### Get AI Explanations
This starts an interactive chat session where you can ask multiple questions about your codebase. The tool will search for relevant code snippets and provide AI-powered explanations for each question. Type 'quit' to exit the chat.
```bash
python main.py --path /path/to/your/codebase --explain --interactive
```

## Supported File Types
The tool currently supports searching through the following file types:

- Python (.py)
- JavaScript (.js)
- Text files (.txt)
- Markdown (.md)
- HTML (.html)
- CSS (.css)
- Shell scripts (.sh)


## How It Works
1. The tool extracts keywords from your question
2. It searches through your codebase for files containing those keywords
3. It extracts relevant code snippets from the matching files
4. If the explain flag is set, it sends the question and code snippets to GPT-4.1
5. GPT-4.1 generates an explanation based on the code snippets
6. The explanation is displayed in the terminal (with streaming in interactive mode)


## License

This project is released under the MIT License.
