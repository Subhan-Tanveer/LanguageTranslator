import streamlit as st
from langdetect import detect
from googletrans import Translator

st.set_page_config(page_icon='🌍', page_title='Language Translator' )

# List of all supported languages
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
    'Urdu': 'ur'
}

def detect_translate(text, target_lang):
    # Detect the language of the input text
    result_lang = detect(text)

    # Initialize the Translator
    translator = Translator()

    # Translate the text into the target language
    lang_translate = translator.translate(text, dest=target_lang).text

    return result_lang, lang_translate



st.title('🌍 Language Detection and Translation 🌐')

# Text input for user
sentence = st.text_area("✍️ Enter the text you want to detect and translate:")

# Dropdown menu for target language selection with the languages dictionary
target_lang = st.selectbox('🌏 Select the language to translate to:', list(languages.keys()))

# Get the language code for the selected language
target_lang_code = languages[target_lang]

if sentence:
    # Detect and translate the input sentence
    result_lang, lang_translate = detect_translate(sentence, target_lang_code)

    # Display results with emojis
    st.write(f"🔍 **Detected Language:** {result_lang}")
    st.write(f"💬 **Translated Text:** {lang_translate}")
