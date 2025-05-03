def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = value >=min and value <= max
        except ValueError:
            print("Error: wrong input")
            continue
        if not ok:            
            print(f"Error: value is not within permitted range ({str(min)}..{str(max)})")
    return value
   

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
    