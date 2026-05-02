from deep_translator import GoogleTranslator

def translate_text(text: str, source_lang='auto', target_lang='en'):
    if target_lang == 'en' and source_lang == 'en':
        return text
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated
    except Exception as e:
        print(f"Translation Error: {e}")
        return text # fallback to original

def get_language_code(lang_str: str) -> str:
    lang_str = lang_str.lower()
    if lang_str in ['hindi', 'hi']:
        return 'hi'
    elif lang_str in ['marathi', 'mr']:
        return 'mr'
    return 'en'
