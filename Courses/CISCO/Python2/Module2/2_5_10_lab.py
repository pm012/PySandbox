'''
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: are the characters comprising the first string hidden 
inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as the letters "d", "o", or "g" don't appear in this order)
Hints:

you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
Test your code using the data we've provided.
donor Nabucodonosor => Yes
donut Nabucodonosor => No

'''

def find_a_word(word:str, text:str)->str:    
    start = 0
    word.lower()
    text.lower()
    for char in word:
        start = text.find(char, start)
        if start == -1:
            return "No"
        start+=1
    return "Yes"


if __name__ == "__main__":
    print(find_a_word("door", "Nabucodonaoosorr"))  # Yes
    print(find_a_word("donor", "Nabucodonosor"))  # Yes
    print(find_a_word("donut", "Nabucodonosor"))  # No
    print(find_a_word("donut", "Nabucoonosor"))  # No


    
            
        
    