import streamlit as st
from deep_translator import GoogleTranslator

FLAGS = {
    'ES': '🇪🇸',
    'FR': '🇫🇷🇧🇪',
    'NL': '🇳🇱🇧🇪',
    'IT': '🇮🇹'
}

LANG_CODES = {
    'ES': 'spanish',
    'FR': 'french',
    'NL': 'dutch',
    'IT': 'italian'
}

NOTICE_ENGLISH = (
    "machine translated. in case of doubt, please refer to the english version of this text, "
    "or get in contact with the People Team."
)

def translate_text(original_text, target_lang_name):
    try:
        # Temporarily replace "People Team" with placeholder
        placeholder = "<<<PEOPLE_TEAM>>>"
        temp_text = original_text.replace("People Team", placeholder)

        # Translate the text
        translated = GoogleTranslator(source='auto', target=target_lang_name).translate(temp_text)

        # Restore "People Team" in the translated output
        translated = translated.replace(placeholder, "People Team")

        # Translate the notice too (but leave "People Team" untouched)
        temp_notice = NOTICE_ENGLISH.replace("People Team", placeholder)
        translated_notice = GoogleTranslator(source='auto', target=target_lang_name).translate(temp_notice)
        translated_notice = translated_notice.replace(placeholder, "People Team")

        return translated + "\n\n*_" + translated_notice + "_*"
    except Exception as e:
        return f"❌ Error translating: {e}"

# Streamlit UI
st.set_page_config(page_title="Multi-Language Translator")
st.title("🌍 Multi-Language Translator")
st.markdown("Type in English and get instant translations:")
