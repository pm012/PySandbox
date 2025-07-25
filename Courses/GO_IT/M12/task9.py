'''
Implement the __copy__ method for the Person class.

Implement the __copy__ and __deepcopy__ methods for the Contacts class.
'''

from copy import copy, deepcopy
import pickle
import os
import pprint


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_person =  Person(copy(self.name),
        copy(self.email),
        copy(self.phone),
        copy(self.favorite))
        return copy_person


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_contacts = Contacts(copy(self.filename),
        copy(self.contacts))
        copy_contacts.is_unpacking = copy(self.is_unpacking)
        copy_contacts.count_save = copy(self.count_save)
        return copy_contacts
        

    def __deepcopy__(self, memo): # memo is dictionary to check if the object has been copied and 
        #avoid endless recursion
        deep_copy_contacts = Contacts(deepcopy(self.filename), deepcopy(self.contacts))
        memo[id(deep_copy_contacts)] = deep_copy_contacts
        deep_copy_contacts.is_unpacking = copy(self.is_unpacking)
        deep_copy_contacts.count_save = copy(self.count_save)
        return deep_copy_contacts
    
if __name__ == "__main__":
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


    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, "task9.dat")

    persons = Contacts(file_path, contacts)       

    # Звичайне копіювання (поверхневе)
    shallow_copied = copy(persons)
    # Глибоке копіювання
    deep_copied = deepcopy(persons)

    # Перевірки
    print("Original contacts object ID:", id(persons))
    print("Shallow copy contacts object ID:", id(shallow_copied))
    print("Deep copy contacts object ID:", id(deep_copied))
    print()

    print("Original first person ID:", id(persons.contacts[0]))
    print("Shallow copy first person ID:", id(shallow_copied.contacts[0]))
    print("Deep copy first person ID:", id(deep_copied.contacts[0]))
    print()

    # Змінимо атрибути, щоб побачити різницю
    persons.contacts[0].name = "MODIFIED NAME"
    shallow_copied.contacts[0].email = "shallow@changed.com"
    deep_copied.contacts[0].phone = "999-999-9999"

    print("=== Original ===")
    pprint.pprint([(p.name, p.email, p.phone) for p in persons.contacts])

    print("=== Shallow Copy ===")
    pprint.pprint([(p.name, p.email, p.phone) for p in shallow_copied.contacts])

    print("=== Deep Copy ===")
    pprint.pprint([(p.name, p.email, p.phone) for p in deep_copied.contacts])


    

    

    