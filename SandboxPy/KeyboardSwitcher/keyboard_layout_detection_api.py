import pynput
import keyboard
import subprocess
import requests
from PyDictionary import PyDictionary

dictionary = PyDictionary()

# Ukrainian to English layout mapping
UA_TO_EN = {
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p',
    'ф': 'a', 'і': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l',
    'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm'
}

EN_TO_UA = {v: k for k, v in UA_TO_EN.items()}

def transliterate(word, mapping):
    """ Convert a mistyped word to the correct layout """
    return ''.join(mapping.get(char, char) for char in word)

def is_valid_english(word):
    """ Check if the word is valid in English using PyDictionary """
    try:
        meaning = dictionary.meaning(word)
        return meaning is not None
    except Exception:
        return False

def is_valid_ukrainian(word):
    """ Check if the word is valid in Ukrainian using an API """
    url = f"https://api.ukrainian-words.com/check?word={word}"  # Example API, replace with actual API
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("valid", False)
    except requests.RequestException:
        pass
    return False

def detect_and_fix_layout(text):
    """ Detect incorrect layout and correct the word """
    corrected_en = transliterate(text, UA_TO_EN)
    corrected_ua = transliterate(text, EN_TO_UA)

    if is_valid_english(corrected_en):
        return corrected_en
    elif is_valid_ukrainian(corrected_ua):
        return corrected_ua
    return text  # Return original if no correction needed

def switch_layout():
    """ Switch the keyboard layout between English and Ukrainian """
    current_layout = subprocess.run(["setxkbmap", "-query"], capture_output=True, text=True).stdout
    if "ua" in current_layout:
        subprocess.run(["setxkbmap", "us"])
    else:
        subprocess.run(["setxkbmap", "ua"])

# Global variable to store typed text
typed_text = ""

def on_key_press(key):
    global typed_text
    try:
        char = key.char
        if char.isalpha():
            typed_text += char  # Add letter to buffer
        elif key == keyboard.Key.space:
            corrected_word = detect_and_fix_layout(typed_text)
            print(f"Corrected: {typed_text} -> {corrected_word}")
            typed_text = ""  # Reset buffer
    except AttributeError:
        pass  # Ignore special keys

# Start listening for keyboard input
with pynput.keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
