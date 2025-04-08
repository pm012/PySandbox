"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

"""

def get_count(sentence: str)-> int:
    vovels = ["a", "e", "i", "o", "u"]
    cnt = 0
    for ch in sentence:
        if ch in vovels:
            cnt+=1
    
    return cnt

if __name__ == '__main__':
    print(get_count('dsf'))