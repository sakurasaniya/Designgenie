# app/translate.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load the model and tokenizer once when the module is imported
MODEL_NAME = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def get_lang_code(lang_name):
    """
    Convert language name or ISO code to NLLB language token
    e.g., "english" -> "eng_Latn", "fr" -> "fra_Latn"
    """
    mapping = {
        "en": "eng_Latn", "english": "eng_Latn",
        "fr": "fra_Latn", "french": "fra_Latn",
        "hi": "hin_Deva", "hindi": "hin_Deva",
        "es": "spa_Latn", "spanish": "spa_Latn",
        "de": "deu_Latn", "german": "deu_Latn",
        "zh": "zho_Hans", "chinese": "zho_Hans",
        "bn": "ben_Beng", "bengali": "ben_Beng",
        "mr": "mar_Deva", "marathi": "mar_Deva",
        "gu": "guj_Gujr", "gujarati": "guj_Gujr",
        # Add more if needed
    }
    return mapping.get(lang_name.lower(), "eng_Latn")  # fallback to English

def translate_text(text, source_lang, target_lang):
    """
    Translate text using the NLLB model from source_lang to target_lang
    """
    source_lang_code = get_lang_code(source_lang)
    target_lang_code = get_lang_code(target_lang)

    # Tokenize with source language code
    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True,
    ).to(model.device)

    # Set the forced_bos_token_id to the target language
    tokenizer.src_lang = source_lang_code
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang_code)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            forced_bos_token_id=forced_bos_token_id,
            max_length=512
        )

    translated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    return translated_text
