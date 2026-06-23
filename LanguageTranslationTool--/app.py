import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool")

st.title("🌍 Language Translation Tool")
st.write("Translate text into different languages")

text = st.text_area("Enter Text")

languages = {
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "French": "fr",
    "Spanish": "es"
}

target_language = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

if st.button("Translate"):
    if text.strip():
        translated = GoogleTranslator(source='auto', target=languages[target_language]).translate(text)

        st.success("Translated Text:")
        st.text_area(
            "Output",
            translated,
            height=100
        )
    else:
        st.warning("Please enter text.")