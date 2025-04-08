import string

def is_spam_words(text: str, spam_words: list[str], space_around: bool = False) -> bool:
    """
    Check if the text contains any spam words.

    :param text: The input text to check.
    :param spam_words: A list of spam words to search for.
    :param space_around: If True, matches only complete words.
    :return: True if spam words are found, False otherwise.
    """
    if not spam_words:
        return False  # No spam words to check
    
    text = text.lower()
    spam_words = [word.lower() for word in spam_words]

    if not space_around:
        # Check for substring match
        return any(spam_word in text for spam_word in spam_words)
    else:
        # Split text into words and handle delimiters
        words = text.translate(str.maketrans("", "", string.punctuation)).split()
        return any(word in spam_words for word in words)

# Example Usage
if __name__ == "__main__":
    print(is_spam_words("This is a test message.", ["test"]))            # True
    print(is_spam_words("This is a test message.", ["spam"]))            # False
    print(is_spam_words("Buy cheap meds now.", ["med"], space_around=True))  # False
    print(is_spam_words("Buy cheap meds now.", ["meds"], space_around=True))  # True
