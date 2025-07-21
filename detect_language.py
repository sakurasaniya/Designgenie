# app/detect_language.py

from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Make language detection deterministic
DetectorFactory.seed = 42

def detect_language(text):
    """
    Detect the language of a given text using langdetect
    Returns an ISO 639-1 language code (e.g., 'en', 'fr', 'hi')
    """
    try:
        lang_code = detect(text)
        return lang_code
    except LangDetectException:
        return "en"  # fallback to English if detection fails
