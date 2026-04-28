import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarise(text):
    prompt = f"""
    Summarise the following text in exactly 3 bullet points.
    Be concise and capture the most important information.

    Text: {text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages = [{
            "role": "user",
            "content": prompt 
        }]
    )

    return response.choices[0].message.content

print("AI Text Summariser - paste your text and press Enter twice when done. Type 'quit' to exit.\n")

while True:
    lines = []
    while True:
        line = input()
        if line.lower() == "quit":
            exit()
        if line == "":
            break
        lines.append(line)

    text = " ".join(lines)
    if text:
        result = summarise(text)
        print(f"\n{result}\n")

