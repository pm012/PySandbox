import os
import re
def rem_chords():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(script_dir, 'text.txt')
    chords = ['Am', 'Dm', 'E', 'Em', 'F', 'G']

    # Regex pattern: full line must be only chords, separated by spaces
    chord_pattern = re.compile(rf'^({"|".join(chords)})(\s+({"|".join(chords)}))*\s*$')

    with open(file, 'r') as fn:
        lines = fn.readlines()

    with open(file, 'w') as fn:
        for line in lines:
            stripped = line.strip()
            if stripped and not chord_pattern.fullmatch(stripped):                
                fn.write(line)
                
def get_yield():
    yield 1
    yield from [2,3]
    yield 4
    


if __name__ == "__main__":    
    #rem_chords()
    print(list(get_yield()))
    