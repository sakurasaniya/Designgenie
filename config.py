# app/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Hugging Face token (optional)
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN", None)

# Default model name
TRANSLATION_MODEL_NAME = "facebook/nllb-200-distilled-600M"

# Supported language codes (ISO → NLLB mapping)
LANG_CODE_MAP = {
    "en": "eng_Latn",
    "fr": "fra_Latn",
    "hi": "hin_Deva",
    "es": "spa_Latn",
    "de": "deu_Latn",
    "zh": "zho_Hans",
    "bn": "ben_Beng",
    "mr": "mar_Deva",
    "gu": "guj_Gujr",
    # Add more languages as needed
}

# Fallback language
DEFAULT_LANG_CODE = "eng_Latn"
