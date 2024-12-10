import streamlit as st
from langdetect import detect
from googletrans import Translator

st.set_page_config(
    page_title="Language Detection & Translation 🌍",
    page_icon="🌐", 
)

languages = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Azerbaijani': 'az',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Chinese (Simplified)': 'zh-CN',
    'Chinese (Traditional)': 'zh-TW',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'tl',
    'Finnish': 'fi',
    'French': 'fr',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian Creole': 'ht',
    'Hausa': 'ha',
    'Hebrew': 'he',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Igbo': 'ig',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jw',
    'Kannada': 'kn',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Korean': 'ko',
    'Kurdish': 'ku',
    'Lao': 'lo',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Macedonian': 'mk',
    'Malay': 'ms',
    'Malayalam': 'ml',
    'Urdu': 'ur'  # Added Urdu
}

def detect_translate(text, target_lang):
    
    result_lang = detect(text)

    
    translator = Translator()

    
    lang_translate = translator.translate(text, dest=target_lang).text

    return result_lang, lang_translate

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://media4.giphy.com/media/IzihZRMnD33J4DsLT1/200w.gif?cid=6c09b952htwbe31upgkfzm1sf2viq7d7z0eksd1o9tnat48h&ep=v1_gifs_search&rid=200w.gif&ct=g");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('🌍 Language Detection and Translation 🌐')

sentence = st.text_area("✍️ Enter the text you want to detect and translate:")

target_lang = st.selectbox('🌏 Select the language to translate to:', list(languages.keys()))

target_lang_code = languages[target_lang]

if sentence:

    result_lang, lang_translate = detect_translate(sentence, target_lang_code)

    st.write(f"🔍 **Detected Language:** {result_lang}")
    st.write(f"💬 **Translated Text:** {lang_translate}")
