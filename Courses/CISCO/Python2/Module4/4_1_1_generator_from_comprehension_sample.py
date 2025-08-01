# This is comprehension as it has [] to generate list
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()


# This is generator  because it it has () when generates sequence
for v in (1 if x & 1 ==0  else 0 for x in range(10)):
    print(v, end=" ")
print()

