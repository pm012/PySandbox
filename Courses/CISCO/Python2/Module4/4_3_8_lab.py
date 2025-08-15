"""
A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. 
Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:

aBc
res/lab_4_3_8.txt
the expected output should look as follows:

Output
a -> 1
b -> 1
c -> 1

Tip: We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values.

"""
from os import path

def process_latin_letters(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        exit(1)

    letter_counts = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            char_lower = char.lower()  # Convert to lowercase
            if char_lower in letter_counts:
                letter_counts[char_lower] += 1
    return letter_counts            
    

def print_histogram_results(letter_counts):
    for letter in letter_counts.keys():
        if letter_counts[letter] > 0:
            print(f"{letter} -> {letter_counts[letter]}")

if __name__ == "__main__":
    filename = input("Enter the name of the file to read: ")

    script_path = path.dirname(path.abspath(__file__))
    dir_path = path.join(script_path, "res")
    file_path = path.join(dir_path, filename)
    
    letter_counts = process_latin_letters(file_path)
    # Print the histogram in alphabetical order
    print_histogram_results(letter_counts)
    