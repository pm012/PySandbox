import random

passlen = int(input("Set the length of the password: "))

#letters numbers and symbols allowed in password
s = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&'

p = "".join(random.sample(s, passlen))
print(p)