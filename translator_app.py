import streamlit as st
from deep_translator import GoogleTranslator

# Flags per language
FLAGS = {
    'ES': '🇪🇸',
    'FR': '🇫🇷🇧🇪',
    'NL': '🇳🇱🇧🇪',
    'IT': '🇮🇹'
}

# Language mapping
LANG_CODES = {
    'ES': 'spanish',
    'FR': 'french',
    'NL': 'dutch',
    'IT': 'italian'
}

# Base notice in English
NOTICE_EN = (
    "machine translated. in case of doubt, please refer to the english version of this text, "
    "or get in contact with the People Team."
)

# Translation function
def translate(text, lang_code):
    try:
        placeholder = "<<<PEOPLE_TEAM>>>"
        text = text.replace("People Team", placeholder)
        translated_main = GoogleTranslator(source='auto', target=lang_code).translate(text)
        translated_main = translated_main.replace(placeholder, "People Team")

        notice_temp = NOTICE_EN.replace("People Team", placeholder)
        translated_notice = GoogleTranslator(source='auto', target=lang_code).translate(notice_temp)
        translated_notice = translated_notice.replace(placeholder, "People Team")

        return translated_main + "\n\n*_" + translated_notice + "_*"
    except Exception as e:
        return f"⚠️ Error: {e}"

# Streamlit UI
st.set_page_config(page_title="🌍 4-Language Translator", layout="centered")
st.title("🌍 4-Language Translator")

input_text = st.text_area("✏️ Enter your English text here:", height=200)

if st.button("Translate"):
    if input_text.strip() == "":
