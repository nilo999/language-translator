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

NOTICE = (
    "\nmachine translated. in case of doubt, please refer to the english version of this text, "
    "or get in contact with the People Team."
)

st.set_page_config(page_title="Multi-Language Translator")
st.title("🌍 Multi-Language Translator")
st.markdown("Type in English and get instant translations:")

text = st.text_area("Enter English text:", height=150)

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some English text.")
    else:
        for lang, lang_name in LANG_CODES.items():
            try:
                translated = GoogleTranslator(source='auto', target=lang_name).translate(text)
                st.markdown(f"### {FLAGS[lang]} {lang}")
                st.write(translated + NOTICE)
            except Exception as e:
                st.error(f"Error translating to {lang}: {e}")

