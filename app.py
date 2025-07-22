import gradio as gr
from chatbot_engine import get_response

def chat_fn(message, history):
    response = get_response(message)
    history.append((message, response))
    return history

def launch_app():
    with gr.Blocks() as demo:
        gr.Markdown("# 🏫 FedPoly Mubi AI Chatbot (Mistral Powered)")
        gr.Markdown("Ask about registration, results, hostel, school fees, etc.\n\nNo training needed!")

        gr.ChatInterface(
            fn=chat_fn,
            title="FedPoly Mubi AI Assistant",
            description="This chatbot uses the Mistral-7B-Instruct model deployed on Render."
        )

    demo.launch(server_name="0.0.0.0", server_port=8080)

if __name__ == "__main__":
    launch_app()
