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

print(f'platform: {platform.platform()}')
print(f'platform.platform(1): {platform.platform(1)}')
print(f'platform.platform(0,1): {platform.platform(0,1)}')


print(f'platform.machine(): {platform.machine()}')
print(f'system: {platform.system()}')

print(f' version: {platform.version()}')


print(f'python implementation: {python_implementation()}')

print('--------------print attributes--------------')
for atr in python_version_tuple():
    print(atr)

print('________________print  dir (os)__________________________')
print(dir(os))
