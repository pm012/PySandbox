# Koprekar's constant
# def revert_number(n:int)->int:
#     return int(str(n)[::-1])

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

def calc_diff(n: int, rev: int) -> int:
    """Calculates the difference between two numbers."""
    return abs(n - rev)

def kaprekar_constant(n: str) -> int:
    """
    Calculates Kaprekar's constant (6174) for a given 4-digit string.
    The function stops when the result equals 6174.
    """
    KAPREKAR_CONSTANT = 6174
    steps = 0

    # Validate the input
    number_checkup(n)

    # Convert the input string to an integer
    n_int = int(n)

    while n_int != KAPREKAR_CONSTANT:
        # Sort digits in ascending and descending order
        asc = int("".join(sorted(n)))
        desc = int("".join(sorted(n, reverse=True)))

        # Calculate the difference
        n_int = calc_diff(desc, asc)
        steps += 1
        print(f"{steps}. {n_int} = {desc} - {asc}")

        # Update the string representation
        n = f"{n_int:04d}"

        if n_int == 0:
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