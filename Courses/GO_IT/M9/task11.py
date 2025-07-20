'''
For a numbers list, you should calculate the sum of the elements using 
the reduce function.

numbers = [3, 4, 6, 9, 34, 12]
Create the sum_numbers(numbers) function, the result of which is the sum 
of the numbers of all elements of the numbers list.
'''

from functools import reduce

def sum_numbers(numbers):
    return reduce(lambda x, y: x+y, numbers)

if __name__ == "__main__":
    numbers = [3, 4, 6, 9, 34, 12]
    print(sum_numbers(numbers))