'''
There is a list, each element of which is a dictionary with user contacts 
of the following type:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
The dictionary contains the name of the user name, their email, phone number, 
and favorite property (whether the contact is a favorite or not).

Develop two functions. One is for serializing and deserializing a 
list of contacts using a json package, and the other is for storing the resulting data in a text file.

The first function, write_contacts_to_file, takes two parameters: 
filename — the file’s name, and contacts — the list of contacts. It saves the specified list to a file using the dump method of the json package.

The json file structure should be as follows:

{
  "contacts": [
    {
      "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": false
    },
    ...
  ]
}
That is, the list of contacts should be stored under the "contacts" key, 
not just save the list to a file.

The second function read_contacts_from_file reads and returns the 
specified list of contacts from the file filename, previously saved by 
the write_contacts_to_file function, using the load method of the json package.

'''
import json
import os

def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as fn:
        json_structure = {"contacts": contacts}
        json.dump(json_structure, fn)

def read_contacts_from_file(filename):
    with open(filename, 'r') as fn:
        list = json.load(fn)['contacts']
        return list
    
if __name__ == "__main__":

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "text2.txt")
    
    contacts_dict = {
  "contacts": [
    {
      "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": False
    },
    {
      "name": "Kiany Rives",
      "email": "kiany.reeves@vestibul.co.uk",
      "phone": "(333) 777-0022",
      "favorite": False
    }
  ]
}
    
    write_contacts_to_file(file_path,contacts_dict)
    contacts_dict_recovered = read_contacts_from_file(file_path)
    print(contacts_dict_recovered)

