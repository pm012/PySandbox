'''
To copy an instance of the Person class from the previous example, implement the copy_class_person function. It takes an instance of the Person class as a parameter and returns a "surface" copy of the object using the copy function from the copy package.

Example:

person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name)  # True
...

'''
import copy

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)

if __name__ == "__main__":
    person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

    copy_person = copy_class_person(person)

    print(copy_person == person)  # False
    print(copy_person.name == person.name)  # True
    