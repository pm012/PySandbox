def add_five(x):
    return x+5

nums = [11, 22, 33, 44, 55]
#example of map  usage to use callable for each element of the list
result = list(map(add_five, nums))
print(result)

# same with lambda

print(list(map(lambda x: x+5, nums)))