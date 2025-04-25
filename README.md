# 🗣️ AI Anything Chatbot

An interactive chatbot built with Gradio and powered by either OpenAI GPT-4 or Hugging Face models. This chatbot can respond to any type of query, from writing code to composing poems.

## Features

- Multi-turn conversation support
- Chat history display
- Conversation logging to a text file
- Loading animations while generating responses
- Fallback to offline Hugging Face models if OpenAI API is not available
- Clean, professional UI

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Setup

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Copy `.env-example` to a new file named `.env`
   - Replace `your_api_key_here` with your actual OpenAI API key

   ```
   cp .env-example .env
   # Then edit the .env file with your text editor
   ```

   If you don't have an OpenAI API key, the application will automatically fall back to using a Hugging Face model.

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (typically `http://127.0.0.1:7860`).

3. Type your message in the text box and click "Send" or press Enter.

4. View your conversation history and interact with the chatbot.

5. All conversations are logged to `chat_log.txt` in the application directory.

## Customization

- To use a different Hugging Face model, modify the `MODEL_NAME` variable in `app.py`.
- To use GPT-3.5 Turbo instead of GPT-4, change the model name in the OpenAI API call.

## License

[MIT License](LICENSE) 