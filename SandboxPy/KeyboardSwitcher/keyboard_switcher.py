import pynput
import keyboard
import subprocess
import nltk
from nltk.corpus import words

# Download dictionary once
nltk.download("words")

# Load English words
ENGLISH_WORDS = set(words.words())

# Ukrainian words (you can extend this list)
UKRAINIAN_WORDS = {"користувач", "привіт", "будинок", "машина", "вода"}

# Ukrainian to English layout mapping
UA_TO_EN = {
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p',
    'ф': 'a', 'і': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l',
    'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm'
}

EN_TO_UA = {v: k for k, v in UA_TO_EN.items()}

def transliterate(word, mapping):
    return ''.join(mapping.get(char, char) for char in word)

def detect_and_fix_layout(text):
    corrected_en = transliterate(text, UA_TO_EN)
    corrected_ua = transliterate(text, EN_TO_UA)

    if corrected_en in ENGLISH_WORDS:
        return corrected_en
    elif corrected_ua in UKRAINIAN_WORDS:
        return corrected_ua
    return text

def switch_layout():
    current_layout = subprocess.run(["setxkbmap", "-query"], capture_output=True, text=True).stdout
    if "ua" in current_layout:
        subprocess.run(["setxkbmap", "us"])
    else:
        subprocess.run(["setxkbmap", "ua"])

typed_text = ""

def on_key_press(key):
    global typed_text
    try:
        char = key.char
        if char.isalpha():
            typed_text += char
        elif key == keyboard.Key.space:
            corrected_word = detect_and_fix_layout(typed_text)
            print(f"Corrected: {typed_text} -> {corrected_word}")
            typed_text = ""
    except AttributeError:
        pass

with pynput.keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
