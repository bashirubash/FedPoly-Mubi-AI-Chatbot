import gradio as gr
import os
from chatbot_engine import get_response

def chat_fn(message, history):
    response = get_response(message)
    history.append((message, response))
    return history

def launch_app():
    with gr.Blocks() as demo:
        gr.Markdown("# 🏫 FedPoly Mubi AI Chatbot (Falcon-7B-Instruct)")
        gr.Markdown("Ask about registration, results, hostel, school fees, SIWES, etc.\n\n**No token needed – fully public model!**")

        gr.ChatInterface(
            fn=chat_fn,
            title="FedPoly Mubi AI Assistant",
            description="AI chatbot for Federal Polytechnic Mubi students, powered by Falcon-7B-Instruct."
        )

    # Use Render's provided PORT environment variable
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 locally
    demo.launch(server_name="0.0.0.0", server_port=port)

if __name__ == "__main__":
    launch_app()
