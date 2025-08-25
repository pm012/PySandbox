"""
Your task is to write a function maskify, which changes all but the last four characters into '#'.
"""

# return masked string
def maskify1(cc):
   rev_cc= cc[::-1]
   masked_rev_cc= rev_cc[:4] + '#'*(len(rev_cc)-4)
   return masked_rev_cc[::-1]

#optionmized solution (without reversing the string)
def maskify(cc):
    return "#" * max(0, len(cc) - 4) + cc[-4:]       

if __name__ == "__main__":
    tests = ["4556364607935616", "64607935616", "1", "", "Skippy", "Nananananananananananananananana Batman!"]
    for test in tests:
        print(maskify(test))
    




    