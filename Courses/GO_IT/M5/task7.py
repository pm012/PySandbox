CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# Create translation dictionary using str.maketrans
TRANS = str.maketrans(
    {c: l for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION)} |
    {c.upper(): l.upper() for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION)}
)

def translate(name: str) -> str:
    """
    Transliterate a string from Cyrillic to Latin.
    
    :param name: String containing Cyrillic characters.
    :return: Transliterated string.
    """
    if not isinstance(name, str):
        raise ValueError("Input must be a string.")
    
    return name.translate(TRANS)


# old implementation: 
# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = {}

# for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c)] = l
#     TRANS[ord(c.upper())] = l.upper()
    


# def translate(name):
            
#     return name.translate(TRANS)
    
    

# Example Usage
if __name__ == "__main__":
    print(translate("Привет"))  # Output: Privet
    print(translate("Мир"))     # Output: Mir



