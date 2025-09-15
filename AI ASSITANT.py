from groq import Groq
from dotenv import load_dotenv #to load from .env file
import os # to access environment variables

load_dotenv()
# load API key
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in .env file!")

# Initialize Groq client
client = Groq(api_key=API_KEY)

# Supported models (try high-quality first, fallback to fast)
MODELS = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]

def get_model():
    """Return the first working model."""
    for model in MODELS:
        try:
            # Test model with an empty prompt with hello meassage
            client.chat.completions.create(model=model, messages=[{"role": "user", "content": "Hello"}])
            return model
        except Exception:
            continue
    raise RuntimeError("❌ No available Groq models!")

ACTIVE_MODEL = get_model() # store the active model
print(f"✅ Using Groq model: {ACTIVE_MODEL}")

def ask_groq(prompt: str): # to check response from groq
    """Send a prompt to Groq and return the response."""
    resp = client.chat.completions.create(
        model=ACTIVE_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content
# first generated response from ai assitant 
def main():
    print("Welcome! I'm your AI assistant SOPHIA (Groq). Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":# ask until it prints quit 
            break
        try:
            response = ask_groq(user_input)# ask groq for user_input
            print("\nSOPHIA:", response)# handle errors 
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__": # run the main program
    main()

    