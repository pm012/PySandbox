'''
Let's continue to extend the example from the previous task. 
Add the is_unpacking attribute to the Contacts class, 
which should be set to False by default. Implement the __setstate__ magic 
method for the Contacts class. When unpacking an instance of the class, 
the method should change the value of the is_unpacking attribute to True. 
Thus, this property will determine that the class instance was obtained as a 
result of unpacking.

Example:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True


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
        self.count_save = 0
        self.is_unpacking = False
        

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] += 1
        return attributes # returns attributes dict that is automatically passed to 
    #value parameter in setstate method (below)

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


if __name__ == "__main__":
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'task6.dat')

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
    print(persons.is_unpacking)  # False
    print(person_from_file.is_unpacking)  # True