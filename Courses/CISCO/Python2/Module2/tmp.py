
sum = 0
while (str!="ENTER"):
    str = input("Enter a number")
    if str.isdigit():
        sum += int(str)
        
print(sum)