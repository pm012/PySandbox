'''
Write a lambda function, setting the least significant bit of its integer argument, and apply it to the map() 
function to produce the string 1 3 3 5 on the console.
'''
if __name__ == "__main__":
    any_list = [1, 2, 3, 4]
    # The lambda function sets the least significant bit (LSB)
    # using a bitwise OR operation with 1.
    # - If the LSB is 0 (e.g., in 2 or 4), it becomes 1.
    # - If the LSB is already 1 (e.g., in 1 or 3), it remains 1.
    # map() applies this lambda function to every item in any_list.
    even_list = list(map(lambda x: x | 1 , any_list)) # Complete the line here
    print(even_list)
    
    for num in any_list:
        print(num|1)