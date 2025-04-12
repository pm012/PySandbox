'''
Your task is to write a program which:

asks the user for some text;
checks whether the entered text is a palindrome, and prints the result.
Note:

assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check – treat them as non-existent;
there are more than a few correct solutions – try to find more than one.

Ten animals I slam in a net => It's a palindrome

Eleven animals I slam in a net => It's not a palindrome

'''

def is_palindrome(text: str)->bool:
    text = text.lower()
    print(text)
    text = "".join(text.split())
    print(text)
    return text[::] == text[::-1]
    
    
if __name__ == "__main__":
    texts = ["Ten animals I slam in a net", "Eleven animals I slam in a net"]
    for text in texts:
        if  is_palindrome(text):
            print(f"{text} => It's a polindrome")
        else:
            print(f"{text} => It's not a polindrome")

    