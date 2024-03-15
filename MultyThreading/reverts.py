"""Write a function that takes in a string of one or more words, 
and returns the same string, but with all words that have five or more 
letters reversed (Just like the name of this Kata). Strings passed in will consist of only 
letters and spaces. Spaces will be included only when more than one word is present."""
def reverts(text: str) -> str:
    words = text.split(' ')
    reverted_lst = []
    for word in words:
        if len(word)>4:
            reverted_lst.append(word[::-1])
        else: reverted_lst.append(word)

    result = ' '.join(reverted_lst)
    return result

if __name__ == '__main__':
   print(reverts("Hello WorLD PytHon"))
    

    

