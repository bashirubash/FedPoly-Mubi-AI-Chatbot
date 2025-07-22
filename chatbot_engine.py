from transformers import pipeline

# Load Falcon-7B-Instruct (free & public)
chatbot = pipeline(
    "text-generation",
    model="tiiuae/falcon-7b-instruct",
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
