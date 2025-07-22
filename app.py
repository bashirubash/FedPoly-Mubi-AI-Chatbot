import gradio as gr
import os
from chatbot_engine import get_response

def chat_fn(message, history):
    response = get_response(message)
    history.append((message, response))
    return history

def launch_app():
    with gr.Blocks() as demo:
        gr.Markdown("# 🏫 FedPoly Mubi AI Chatbot (Flan-T5 Small)")
        gr.Markdown("Ask about registration, results, hostel, school fees, etc.\n\n**Runs on CPU – Render Friendly!**")

        gr.ChatInterface(
            fn=chat_fn,
            title="FedPoly Mubi AI Assistant",
            description="AI chatbot for Federal Polytechnic Mubi students, powered by google/flan-t5-small."
        )

    port = int(os.environ.get("PORT", 8080))
    demo.launch(server_name="0.0.0.0", server_port=port, share=False)

if __name__ == "__main__":
    launch_app()
