def lab_3_2_10():
    # Prompt the user to enter a word
    # and assign it to the user_word variable.
    user_word = input("Enter a word: ")    
    for letter in user_word:
        
        # Complete the body of the for loop.
        if letter.upper() in "AEIOU":
            continue
        else:
            print(letter.upper())

def lab_3_2_11():
    word_without_vowels = ""
    user_word = input("Enter a word: ")

    # Prompt the user to enter a word
    # and assign it to the user_word variable.


    for letter in user_word:
        # Complete the body of the loop.
        if letter.upper() in "AEIOU":
            continue
        else:
            word_without_vowels+=letter.upper()

    # Print the word assigned to word_without_vowels.
    print(word_without_vowels)
    
def lab_3_2_14():
    # Define how many layers should contain certain (wall) pyramid consisting with the defined number of layers
    blocks = int(input("Define number of blocks: "))
    height = 0
    layer = 1
    
    while blocks >= layer:
        blocks -= layer
        height +=1
        layer +=1
        
    print("The height of the pyramid: ", height)
    
def lab_3_2_15():

# Implement the following (Lothar Collatz hypothesis):
# 1. take any non-negative and non-zero integer number and name it c0;
# 2. if it's even, evaluate a new c0 as c0 ÷ 2;
# 3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# 4. if c0 ≠ 1, go back to point 2.

# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

    c0 = int(input("Enter the number: "))
    cnt = 0    
    while c0 != 1:
        cnt+=1
        if c0 %2 == 0:
            c0 = int(c0 / 2)
            print (c0)
        else:
            c0 = c0*3+1
            print(c0)
            
    print("steps = ", cnt)


    
    


if __name__ == "__main__":
    #lab_3_2_10()
    #lab_3_2_11()
    #lab_3_2_14()
    lab_3_2_15()