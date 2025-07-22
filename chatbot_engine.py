from transformers import pipeline

# Load lightweight model for Render Free Tier
chatbot = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

def get_response(user_input):
    prompt = (
        "You are an academic assistant chatbot for Federal Polytechnic Mubi.\n"
        "Answer clearly and briefly.\n\n"
        f"Student: {user_input}\nAssistant:"
    )

    result = chatbot(prompt, max_new_tokens=100)[0]['generated_text']
    return result.strip()
