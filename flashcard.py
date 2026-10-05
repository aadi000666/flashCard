import os
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

HF_TOKEN = os.getenv("HF_TOKEN", "").strip()
HF_MODEL = os.getenv("HF_MODEL", "Qwen/Qwen2.5-7B-Instruct").strip()

if not HF_TOKEN:
    raise SystemExit(
        "Error: HF_TOKEN is missing. Add HF_TOKEN=your_token to the .env file."
    )

if not HF_MODEL:
    raise SystemExit(
        "Error: HF_MODEL is empty. Set it to a model supported by your Hugging Face providers."
    )

topic = input("Which topic ? ").strip()

if not topic:
    raise SystemExit("Topic cannot be empty.")

client = InferenceClient(
    token=HF_TOKEN,
    provider="auto",
)
prompt = f"""Generate exactly 7 simple Q&A flashcards on the topic: {topic}

Use this format and do not add any extra text:

Card1: Question
Ans: Answer

Card2: Question
Ans: Answer

Card3: Question
Ans: Answer

Card4: Question
Ans: Answer

Card5: Question
Ans: Answer

Card6: Question
Ans: Answer

Card7: Question
Ans: Answer

Keep the questions simple and the answers short."""

try:
    response = client.chat.completions.create(
        model=HF_MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
    )

    if not response.choices:
        raise RuntimeError("The model returned no response choices.")

    content = response.choices[0].message.content
    if not content or not content.strip():
        raise RuntimeError("The model returned an empty response.")

    print("\n---Generated Flashcards---\n")
    print(content.strip())

except Exception as exc:
    print("\nError while generating flashcards:")
    print(exc)
    print(
        "\nCheck that HF_MODEL is available through a provider enabled for your "
        "Hugging Face account."
    )
