# 🤖 AI Flashcard Generator

A simple Python project that uses **Generative AI** to automatically create 5 Question & Answer flashcards from any topic.

## 🚀 Features

- Enter any topic
- AI generates 5 simple flashcards
- Uses Hugging Face Inference API
- Secure API key using `.env`
- Error handling included

## 🛠️ Technologies

- Python
- Hugging Face
- `huggingface_hub`
- `python-dotenv`

## 📂 Structure

```text
FlashCard/
├── flashcard.py
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Setup

Install dependencies:

```bash
pip install huggingface_hub python-dotenv
```

Create `.env`:

```env
HF_TOKEN=your_huggingface_token
HF_MODEL=your_supported_model
```

Run:

```bash
python flashcard.py
```

## 🔄 Working

```text
Topic → Python → Hugging Face API → AI Model → Flashcards
```

## 🎯 Purpose

This project helps students quickly create study material using Generative AI.

**Made for educational purposes.**


# Environment variables / secrets
.env    ----
            !------# they imp to .gitignore
.env.*-------
!.env.example

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Virtual environment # when you create 
venv/
.venv/
env/

# IDE / editor files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
