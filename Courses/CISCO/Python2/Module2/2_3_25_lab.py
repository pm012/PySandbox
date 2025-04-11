'''
You already know how split() works. Now we want you to prove it.

Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

it should accept exactly one argument – a string;
it should return a list of words created from the string, divided in the places where the string contains whitespaces;
if the string is empty, the function should return an empty list;
its name should be mysplit()
Use the template in the editor. Test your code carefully.


Excpected output:
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
[]
['abc']
[]

'''



def split_sort():
    s1 = 'Where are the snows of yesteryear?'
    s2 = s1.split()
    s3 = sorted(s2)    
    print(s3[1])


#-----------------------
def mysplit(strng)->list:
    return strng.split()

def mysplit_print():
    print(mysplit("To be or not to be, that is the question"))
    print(mysplit("To be or not to be,that is the question"))
    print(mysplit("   "))
    print(mysplit(" abc "))
    print(mysplit(""))
#---------------------------



def main():
    mysplit_print()
    split_sort()
    
        

        
if __name__ == "__main__":
    main()
   
    