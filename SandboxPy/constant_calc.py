# Koprekar's constant
# def revert_number(n:int)->int:
#     return int(str(n)[::-1])
"""
Take any four digit number (e.g. 3942)
Rearrange its digits into ascending and descending order(e.g. 2349 and 9432)
Subtract the smaller from the larger (e.g. 9432 - 2349 = 7083)
Now repeat the same procedure with the new number.
(so here we would do 8730 - 378 = 8352
and so on ...
"""

def number_checkup(n: str) -> bool:
    """
    Checks if the input is valid:
    - Must be a string of 4 digits (including leading zeros).
    - Must have at least two distinct digits.
    """
    if len(n) != 4 or not n.isdigit():
        raise ValueError("Input must be a string of exactly 4 digits (including leading zeros).")

    unique_dgts = set(n)
    if len(unique_dgts) < 2:
        raise ValueError("Input must have at least two distinct digits.")
    return True

def calc_diff(n: str) -> int:
    """Calculates the difference between the largest and smallest permutations of the number."""
    asc = int("".join(sorted(n)))  # Sort digits in ascending order
    desc = int("".join(sorted(n, reverse=True)))  # Sort digits in descending order
    return desc - asc

def kaprekar_constant(n: str) -> int:
    """
    Calculates Kaprekar's constant (6174) for a given 4-digit string.
    The function stops when the result equals 6174.
    """
    KAPREKAR_CONSTANT = 6174
    steps = 0

    # Validate the input
    number_checkup(n)

    while int(n) != KAPREKAR_CONSTANT:
        # Calculate the difference
        diff = calc_diff(n)
        steps += 1
        print(f"{steps}. {diff} = {''.join(sorted(n, reverse=True))} - {''.join(sorted(n))}")

        # Update the string representation
        n = f"{diff:04d}"

        if diff == 0:
            raise ValueError("Kaprekar's process cannot proceed with all identical digits.")

    return steps


if __name__ == "__main__":
    try:
        console = ''
        while console != 'exit':
            console = input("Enter a 4-digit number (including leading zeros) or 'exit' to quit: ")
            if console.isdigit() and len(console) == 4:
                steps_to_constant = kaprekar_constant(console)
                print(f"It took {steps_to_constant} steps to reach Kaprekar's constant for {console}")
            elif console != 'exit':
                print("Invalid input! Please enter exactly 4 digits.")
    except ValueError as e:
        print(e)
