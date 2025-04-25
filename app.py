import os
import gradio as gr
import time
from datetime import datetime
import random

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

def save_conversation(user_input, bot_response):
    """Save the conversation to a log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] User: {user_input}\n")
        f.write(f"[{timestamp}] Bot: {bot_response}\n\n")

def generate_response(message, history):
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

# Create the Gradio interface
with gr.Blocks(title="🗣️ AI Anything Chatbot") as demo:
    gr.Markdown("""
    # 🗣️ AI Anything Chatbot
    
    Ask me anything! I can respond to a variety of topics and questions.
    Just type your message below and I'll respond to the best of my abilities.
    
    Your conversation will be saved to chat_log.txt for future reference.
    """)
    
    chatbot = gr.Chatbot(
        height=500,
        show_copy_button=True,
        bubble_full_width=False,
    )
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message here...",
            scale=9,
            container=False,
            show_label=False,
        )
        submit = gr.Button("Send", scale=1, variant="primary")
    
    with gr.Accordion("Settings", open=False):
        info = gr.Markdown("""
        - Using simple pattern-based responses
        - Conversations are logged to chat_log.txt
        """)
    
    def respond(message, chat_history):
        bot_message = generate_response(message, chat_history)
        chat_history.append((message, bot_message))
        return "", chat_history
    
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    submit.click(respond, [msg, chatbot], [msg, chatbot])
    
if __name__ == "__main__":
    # Create an empty chat log file if it doesn't exist
    if not os.path.exists("chat_log.txt"):
        with open("chat_log.txt", "w", encoding="utf-8") as f:
            f.write("# AI Anything Chatbot - Conversation Log\n\n")
    
    # Launch the Gradio app
    demo.launch(share=True) 