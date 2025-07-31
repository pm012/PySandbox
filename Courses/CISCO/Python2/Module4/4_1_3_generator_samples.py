def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

if __name__ == "__main__":
    # Usage in loops
    for v in powers_of_2(8):
        print(v)
        
    # Usage in comprehensions

    my_list = [x for x in powers_of_2(8)]
    print("Generated list from comprehension: ")
    print(my_list)

    # Usage in list() function

    t = list(powers_of_2(3))
    print('Usage in list function: ')
    print(t)
    
    

