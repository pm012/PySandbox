# Koprekar's constant
# def revert_number(n:int)->int:
#     return int(str(n)[::-1])

def number_checkup(n:int)->bool:
    if len(n) != 4 or not n.isdigit():
        raise ValueError("input must be a string of 4 digits(including leading zeros)")
    
    unique_dgts = set(n)
    return len(unique_dgts)>=2

def calc_diff(n: int, rev: int)->int:
    return abs(n-rev)

def kaprekar_constant(n: int)-> int:
    KAPREKAR_CONSTANT = 6174
    steps = 0
    # get leading zeros
    n_str = f"{n:04d}"

    # Validate number
    if not number_checkup(n_str):
        raise ValueError("Input must have at least two distinct digits.")

    

    while n != KAPREKAR_CONSTANT:
        
        # Sort digits in ascending and descending order
        asc = int("".join(sorted(n_str)))
        desc = int("".join(sorted(n_str, reverse=True)))
        
        # Calculate the difference
        n = calc_diff(desc, asc)
        steps += 1
        print(f"{steps}. {n} = {desc} - {asc}")

        if n == 0:
            raise ValueError("Kaprekar's process cannot proceed with all identical digits.")

    return steps


if __name__ == "__main__":
    try:
        console = ''
        while console != 'exit':
            console = input("Enter 4 digit number or 'exit' to quit: ")  
            if console.isdigit():
                number = int(console)
                steps_to_constant = kaprekar_constant(number)
                print(f"It took {steps_to_constant} steps to reach Kaprekar's constant for {number}")            
    except ValueError as e:
        print(e)