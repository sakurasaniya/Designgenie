# ui/streamlit_app.py

import streamlit as st
import sys
import os

# Ensure app/ is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from app.translate import translate_text
from app.detect_language import detect_language
from app.config import LANG_CODE_MAP

st.set_page_config(page_title="Multilingual Translator", page_icon="🌍")
st.title("🌍 Multilingual Translation Chatbot")

st.markdown("""
This app uses Meta's NLLB model to perform high-quality translation between 200+ languages. 
Just enter text and select the target language!
""")

with st.form("translate_form"):
    input_text = st.text_area("Enter text to translate", height=150)
    target_lang = st.selectbox("Select target language", options=list(LANG_CODE_MAP.keys()), index=0)
    submit_button = st.form_submit_button("Translate")

if submit_button:
    if not input_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner("Detecting language and translating..."):
            source_lang = detect_language(input_text)
            translated_text = translate_text(input_text, source_lang, target_lang)

        st.markdown(f"*Detected Source Language:* {source_lang}")
        st.markdown(f"*Translated Text:*")
        st.success(translated_text)

st.markdown("---")
st.caption("Powered by 🤖 Hugging Face Transformers & Meta's NLLB model")
