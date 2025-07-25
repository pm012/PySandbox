'''
As you have already understood, for the Contacts class, creating a 
surface copy of a class instance will not succeed because we have a 
contacts attribute. This attribute is a list of object instances of the 
Person class, which means that all of them will be passed by reference. 
Therefore, you need to use the deepcopy method from the copy package.

For the Contacts class, implement the copy_class_contacts function. 
As a parameter, it takes an instance of the Contacts class and returns a 
deep copy of the object using the deepcopy function from the copy package.

Example:

persons = Contacts("user_class.dat", contacts)

new_persons = copy_class_contacts(persons)

new_persons.contacts[0].name = "Another name"

print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name

'''
import copy
import os
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


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


def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)

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
    file_path = os.path.join(script_path, "task8.dat")

    persons = Contacts(file_path, contacts)

    new_persons = copy_class_contacts(persons)

    new_persons.contacts[0].name = "Another name"

    print(persons.contacts[0].name)  # Allen Raymond
    print(new_persons.contacts[0].name)  # Another name

