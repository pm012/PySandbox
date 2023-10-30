import random

MIN_VAL = 1
MAX_VAL = 6

roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':
    print("Rolling the dices: ")
    print("The values are... ")
    print(random.randint(MIN_VAL, MAX_VAL))
    roll_again = input("Roll the dices again?")