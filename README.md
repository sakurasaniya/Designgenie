# Designgenie
“DesignGenie: An AI-powered design assistant that transforms your ideas into visually stunning, voice-guided layouts in seconds.”
# 🌍 Multilingual Translation Chatbot

This is a multilingual text-to-text translation chatbot built using Meta's NLLB model (No Language Left Behind) and deployed via Streamlit. It can automatically detect the input language and translate it into over 200 supported languages.

---

## 📦 Features

✅ Automatic language detection using langdetect

✅ High-quality translation using facebook/nllb-200-distilled-600M

✅ Streamlit web interface

✅ Lightweight & easy to deploy (Kaggle, Hugging Face Spaces, local)

✅ Extendable to include voice (via SeamlessM4T) or chat memory

---

## 🧰 Tech Stack

- Python 3.9+
- Hugging Face Transformers
- Meta NLLB model
- Streamlit
- Langdetect
- dotenv

---

## 📁 Folder Structure


multilingual-chatbot/
├── app/
│   ├── translate.py           # Translation logic
│   ├── detect_language.py     # Language detection
│   └── config.py              # Config and constants
│
├── ui/
│   └── streamlit_app.py       # Streamlit UI logic
│
├── requirements.txt
├── README.md
└── .env                       # Optional: Hugging Face token


---

## 🚀 How to Run Locally

1. Clone the repo or download the folder

bash
git clone https://github.com/yourusername/multilingual-chatbot.git
cd multilingual-chatbot


2. Create a virtual environment and install dependencies:

bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt


3. Run the Streamlit app:

bash
streamlit run ui/streamlit_app.py


---

## 🔐 (Optional) Hugging Face Token

Some models require authentication. Create a .env file and add:


HUGGINGFACE_TOKEN=your_token_here


---

## 📚 Model Reference

- [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M)

---

## 🧠 Future Improvements

- [ ] Add chat history with LangChain
- [ ] Add SeamlessM4T for voice-to-text and speech translation
- [ ] Add Gradio version
- [ ] Deploy on Hugging Face Spaces / Kaggle

---

## 🧑‍💻 Author

Built with ❤ by [Your Name] for educational and real-world translation use cases.

---

## 📄 License

MIT License
