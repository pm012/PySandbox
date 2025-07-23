'''
Develop the Person class. It has four properties: the user's name, their email, 
phone number phone, and the favorite property (indicating whether the contact is
 a favorite).

An example of creating a class instance:

    Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)
Develop the Contacts class. It must initialize two properties through the 
constructor: filename — the name of the file for packing an object of the 
Contacts class, contacts — a list of contacts, and instances of the Person class.

An example of creating a class instance:

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
Develop two methods for serializing and deserializing an instance 
of the Contacts class using the pickle package and storing data in a binary file.

The first method, save_to_file, saves an instance of the Contacts class to a 
file using the dump method of the pickle package. The file name is stored in the 
filename attribute.

The second method, read_from_file, reads and returns an instance of the 
Contacts class from the file filename using the load method of the pickle package.

Example:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
'''
import os
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        

    def save_to_file(self):
        with open(self.filename, 'wb') as fn:
            pickle.dump(self, fn)
        
            

    def read_from_file(self):
        with open(self.filename, 'rb') as fn:
            return pickle.load(fn)
        
if __name__ == "__main__":
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'task4.dat')

    contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts(file_path, contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

        
