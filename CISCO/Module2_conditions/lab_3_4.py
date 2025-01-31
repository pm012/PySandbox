def lab_3_4_6():
    hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
    print(hat_list)

    # Step 1: write a line of code that prompts the user
    # to replace the middle number with an integer number entered by the user.
    hat_list[len(hat_list) // 2] = int(input("Enter a value for the new middle element: "))
    print(hat_list)

    # Step 2: write a line of code that removes the last element from the list.
    print("Hat list length before deletion: ", len(hat_list))
    del hat_list[-1]
    

    # Step 3: write a line of code that prints the length of the existing list.
    print(len(hat_list))
    print(hat_list)
    
    
if __name__ == "__main__":
    lab_3_4_6()