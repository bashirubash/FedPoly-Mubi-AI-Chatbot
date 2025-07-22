from transformers import pipeline

# Load Mistral 7B Instruct from Hugging Face
chatbot = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_new_tokens=200,
    temperature=0.6,
    do_sample=True
)

def get_response(user_input):
    prompt = (
        "You are an academic assistant chatbot for Federal Polytechnic Mubi.\n"
        "Answer the student's question clearly and accurately.\n\n"
        f"Student: {user_input}\nAssistant:"
    )

    result = chatbot(prompt)[0]['generated_text']

    # Extract only the assistant's response
    if "Assistant:" in result:
        reply = result.split("Assistant:")[-1].strip()
    else:
        reply = result.strip()
    
    return reply
