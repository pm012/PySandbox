import os
import csv
from faker import Faker
from functools import wraps


def resolve_path(func):
    @wraps(func)
    def wrapper(filename, *args, **kwargs):
        file_path = os.path.join(script_dir, filename)
        return func(file_path, *args, **kwargs)
    return wrapper
    


def generate_dict_list(num: int)->list:
    contacts_list = []
    fake = Faker()
    for _ in range (0, num):
        name = fake.name()        
        fullname = f"{name}"
        email = f"{fullname.replace(" ", ".")}@{fake.domain_name()}".lower()
        contacts_list.append({"name": fullname,
                              "email": email,
                              "phone": fake.phone_number(),
                              "favorite": fake.pybool()})
    return contacts_list


@resolve_path
def write_contacts_to_file(filename: str, contacts: dict):    
    with open(filename, 'w', newline='') as fn:
        field_names = contacts[0].keys()
        writer = csv.DictWriter(fn, fieldnames = field_names)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)
            
@resolve_path
def read_contacts_from_file(filename: str):    
    result = list()
    with open(filename, 'r', newline='') as fn:
        reader = csv.DictReader(fn)
        for row in reader:
            result.append({
                'name':row['name'],
                'email': row['email'],
                'phone': row['phone'],
                'favorite': eval(row['favorite'])                
                
            })
        return result
    
def print_contacts(contacts: list):
    for contact in contacts:
        print(contact)



if __name__ == "__main__":
    #fake = Faker(locale='uk_UA')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "test3.csv")
    
    contacts_list = generate_dict_list(5)
    print("Initial contacts: ")
    print_contacts(contacts_list)
    
    write_contacts_to_file(file_path, contacts_list)
    
    recovered_contacts = read_contacts_from_file(file_path)
    print("Recovered contacts list: ")
    print_contacts(recovered_contacts)
    
    
        
    