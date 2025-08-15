"""
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)
Assuming that the input file contains just one line filled with:

cBabAa
samplefile.txt
the expected output should look as follows:

Output
a -> 3
b -> 2
c -> 1
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

    # Sort the histogram by frequency (descending order)
    sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    # items() returns a list of tuples (letter, count), which is suitable for printing and saving
    # key=lambda item: item[1] sorts by the count (item[1])
    # reverse=True sorts from highest to lowest count (descending order)
    return sorted_counts
    

def save_results_to_hist_file(sorted_counts, file_path):    
    # Save the histogram to a file with the same name but with '.hist' suffix
    output_lines = []
    for letter, count in sorted_counts:
        if count > 0:
            output_lines.append(f"{letter} -> {count}")

    hist_file_path = f"{file_path}.hist"
    with open(hist_file_path, 'w') as hist_file:
        hist_file.write("\n".join(output_lines))
    print(f"Histogram saved to '{hist_file_path}'")

if __name__ == "__main__":
    filename = input("Enter the name of the file to read: ")

    script_path = path.dirname(path.abspath(__file__))
    dir_path = path.join(script_path, "res")
    file_path = path.join(dir_path, filename)
    
    sorted_counts = process_latin_letters(file_path)    
    save_results_to_hist_file(sorted_counts, file_path)