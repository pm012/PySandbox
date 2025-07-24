'''
We will continue to expand the example from the previous task. Add the count_save attribute to the Contacts class. It should be set to 0 by default. Implement the magic __getstate__ method for the Contacts class. When packing an instance, the class method should increase the value of the count_save attribute by one. Thus, this property is a counter for repeated operations of packing an instance of a class.

Example:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3
'''

import pickle
import os


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
        self.count_save = 0
        

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        # self.count_save+=1 # incorrect solution as it increments counter before serialization
        attributes = self.__dict__.copy()
        attributes["count_save"] += 1 # correct solution
        
        attributes['fh'] = None
        return attributes

if __name__ == "__main__":
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'task5.dat')
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
    first = persons.read_from_file()
    first.save_to_file()
    second = first.read_from_file()
    second.save_to_file()
    third = second.read_from_file()

    print(persons.count_save)  # 0
    print(first.count_save)  # 1
    print(second.count_save)  # 2
    print(third.count_save)  # 3

        
        
        