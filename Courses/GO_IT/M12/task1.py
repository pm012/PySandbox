'''
There is a list, each element of which is a dictionary with user 
contacts of the following type:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
The dictionary contains the name of the user name, their email, 
phone number, and the favorite property (whether the contact is a 
favorite or not).

Implement two functions. One is for serializing and deserializing a 
list of contacts using the pickle package, and the other is for storing the 
resulting data in a binary file.

The first function, write_contacts_to_file, takes two parameters: filename — 
the file’s name, and contacts — the list of contacts. It saves the specified 
list to a file using the dump method of the pickle package.

The second function, read_contacts_from_file, reads and returns the specified 
list of contacts from the file filename using the pickle package's load method.
'''

import pickle
import os


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as fn:
        pickle.dump(contacts, fn)   
        


def read_contacts_from_file(filename):
    with open(filename, "rb") as fn:
        return pickle.load(fn)   

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "text1.txt")

    contacts =  {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
    write_contacts_to_file(file_path, contacts)
    contacts1 = read_contacts_from_file(file_path)
    print(contacts1)

    
        
    
