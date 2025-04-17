'''
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check – treat them as non-existent
Test your code using the data we've provided.
Listen  and Silent  => Anagrams

modern and norman => Not Anagrams

'''
from  collections import Counter
#################################################################
def isAnagram1(word1: str, word2: str) -> bool: # without Counter
    word1 = word1.lower()
    word2 = word2.lower()
    
    if len(word1) != len(word2):
        return False

    # Build frequency dictionary manually
    def char_count(word):
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        return freq

    return char_count(word1) == char_count(word2)

###########################IS SENTENCE ANAGRAM###########################################

def isAnagram2(sentence1: str, sentence2:str)->bool: # works for sentences
    sentence1 = sentence1.lower().split()   
    sentence2 = sentence2.lower().split()
    sentence1= "".join(sentence1)
    sentence2= "".join(sentence2)
    sentence1=sorted(list(sentence1))
    sentence2=sorted(list(sentence2))
    return sentence1 == sentence2

###################THE BEST###################################
def isAnagram3(sentence1: str, sentence2: str) -> bool:
    normalize = lambda s: sorted("".join(s.lower().split()))
    return normalize(sentence1) == normalize(sentence2)

    
########################################################

def isAnagram(word1:str, word2:str)->bool:
    word1 = word1.lower()
    word2 = word2.lower()
    return Counter(word1)==Counter(word2)

def main():
    tests = [
        ("Listen", "Silent"),
        ("modern", "norman"),
        ("aabb", "abbb")       
        
    ]
    for word1, word2 in tests:
        print(f"{word1} and {word2} are: ")
        if isAnagram2(word1, word2):
            print("Anagram")
        else:
            print("Not anagram")


if __name__ == "__main__":
    main()
    #isAnagram2("Test", "Set t")