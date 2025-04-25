import os
import random
import time
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple responses for demonstration
RESPONSES = [
    "That's an interesting question. I'd have to think about that.",
    "I understand what you're saying. Could you tell me more?",
    "That's a great point! I appreciate your perspective.",
    "I'm not entirely sure about that, but here's what I think...",
    "Thanks for sharing that with me. It's quite insightful.",
    "I've been thinking about similar topics recently.",
    "That's a complex question with many possible answers.",
    "I see what you mean. Have you considered looking at it from another angle?",
    "That's fascinating! I'd love to learn more about your thoughts on this.",
    "I think many people would agree with your perspective on that.",
    "That's a unique way of looking at things. I hadn't considered that before.",
    "If I understand correctly, you're saying that...",
    "Your question touches on some important concepts.",
    "I think the key to understanding this is to consider multiple perspectives.",
    "That reminds me of something I read recently about this topic.",
]

# In-memory chat history (in a real app, this would be a database)
chat_history = []

def save_conversation(user_input, bot_response):
    """Save the conversation to a log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] User: {user_input}\n")
        f.write(f"[{timestamp}] Bot: {bot_response}\n\n")

def generate_response(message):
    """Generate a simple response"""
    # For demonstration, we'll use simple pattern matching for common questions
    message_lower = message.lower()
    
    # Simple response patterns
    if "hello" in message_lower or "hi" in message_lower or "hey" in message_lower:
        bot_response = "Hello! How can I help you today?"
    elif "how are you" in message_lower:
        bot_response = "I'm just a program, but I'm functioning well. How are you doing?"
    elif "your name" in message_lower:
        bot_response = "I'm an AI Anything Chatbot, designed to have conversations with you."
    elif "help" in message_lower or "can you" in message_lower:
        bot_response = "I'm here to chat with you about anything! Just type your questions or thoughts, and I'll respond."
    elif "thank" in message_lower:
        bot_response = "You're welcome! Feel free to ask if you need anything else."
    elif "bye" in message_lower or "goodbye" in message_lower:
        bot_response = "Goodbye! It was nice chatting with you. Come back anytime!"
    elif any(word in message_lower for word in ["code", "programming", "python", "javascript"]):
        bot_response = "Programming is fascinating! While I can't generate code in this simple version, I'd be happy to discuss programming concepts."
    elif "joke" in message_lower:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why was the math book sad? Because it had too many problems.",
            "What do you call a fake noodle? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        bot_response = random.choice(jokes)
    else:
        # For other messages, choose a random thoughtful response
        bot_response = random.choice(RESPONSES)
    
    # Simulate thinking time
    time.sleep(0.5)
    
    # Save the conversation
    save_conversation(message, bot_response)
    
    return bot_response

@app.route('/')
def home():
    # Create an empty chat log file if it doesn't exist
    if not os.path.exists("chat_log.txt"):
        with open("chat_log.txt", "w", encoding="utf-8") as f:
            f.write("# AI Anything Chatbot - Conversation Log\n\n")
            
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Get response
    bot_response = generate_response(user_message)
    
    # Add to history
    chat_history.append({"user": user_message, "bot": bot_response})
    
    return jsonify({
        'response': bot_response,
        'history': chat_history
    })

if __name__ == '__main__':
    # Create the templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Create the index.html file
    with open('templates/index.html', 'w') as f:
        f.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🗣️ AI Anything Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .description {
            text-align: center;
            margin-bottom: 20px;
            color: #666;
        }
        #chat-container {
            border: 1px solid #ddd;
            border-radius: 8px;
            height: 500px;
            overflow-y: auto;
            padding: 10px;
            margin-bottom: 20px;
            background: #f9f9f9;
        }
        .message {
            margin-bottom: 10px;
            padding: 8px 15px;
            border-radius: 18px;
            max-width: 70%;
            word-wrap: break-word;
        }
        .user-message {
            background-color: #DCF8C6;
            margin-left: auto;
            color: #000;
            text-align: right;
        }
        .bot-message {
            background-color: #E5E5EA;
            margin-right: auto;
            color: #000;
        }
        .message-container {
            display: flex;
            margin-bottom: 10px;
        }
        .user-container {
            justify-content: flex-end;
        }
        .bot-container {
            justify-content: flex-start;
        }
        .input-container {
            display: flex;
        }
        #user-input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        #send-button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            margin-left: 10px;
            cursor: pointer;
        }
        #send-button:hover {
            background-color: #45a049;
        }
        .typing {
            font-style: italic;
            color: #888;
            margin-left: 10px;
        }
        .hidden {
            display: none;
        }
        .settings {
            margin-top: 20px;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 4px;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>🗣️ AI Anything Chatbot</h1>
    <p class="description">
        Ask me anything! I can respond to a variety of topics and questions.<br>
        Just type your message below and I'll respond to the best of my abilities.
    </p>
    <div id="chat-container"></div>
    <div class="typing hidden" id="typing-indicator">Bot is typing...</div>
    <div class="input-container">
        <input type="text" id="user-input" placeholder="Type your message here..." autofocus>
        <button id="send-button">Send</button>
    </div>
    <div class="settings">
        <p>- Using simple pattern-based responses</p>
        <p>- Conversations are logged to chat_log.txt</p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const chatContainer = document.getElementById('chat-container');
            const userInput = document.getElementById('user-input');
            const sendButton = document.getElementById('send-button');
            const typingIndicator = document.getElementById('typing-indicator');
            
            // Send message when Send button is clicked
            sendButton.addEventListener('click', sendMessage);
            
            // Send message when Enter key is pressed
            userInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });
            
            function sendMessage() {
                const message = userInput.value.trim();
                if (message === '') return;
                
                // Add user message to chat
                addMessageToChat('user', message);
                
                // Clear input
                userInput.value = '';
                
                // Show typing indicator
                typingIndicator.classList.remove('hidden');
                
                // Send to server
                fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message }),
                })
                .then(response => response.json())
                .then(data => {
                    // Hide typing indicator
                    typingIndicator.classList.add('hidden');
                    
                    // Add bot response to chat
                    addMessageToChat('bot', data.response);
                })
                .catch(error => {
                    console.error('Error:', error);
                    typingIndicator.classList.add('hidden');
                    addMessageToChat('bot', 'Sorry, there was an error processing your request.');
                });
            }
            
            function addMessageToChat(sender, text) {
                const messageContainer = document.createElement('div');
                messageContainer.className = `message-container ${sender}-container`;
                
                const messageElement = document.createElement('div');
                messageElement.className = `message ${sender}-message`;
                messageElement.textContent = text;
                
                messageContainer.appendChild(messageElement);
                chatContainer.appendChild(messageContainer);
                
                // Scroll to bottom
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }
        });
    </script>
</body>
</html>
        ''')
    
    app.run(debug=True, port=7860) 