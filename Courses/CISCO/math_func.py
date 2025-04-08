from math import ceil, floor, trunc
from random import random, seed
import platform
from platform import python_implementation, python_version_tuple
import os

seed(0)

# for i in range(5):
#     print(random())

x = 1.4
y = 2.6

print(platform.platform())
print(platform.platform(1))
print(platform.platform(0,1))

print(platform.machine())
print(platform.system())

print(platform.version())


print(python_implementation())

for atr in python_version_tuple():
    print(atr)

print(dir(os))
