'''
There is a contacts list, the elements of which are contact dictionaries of the 
following type:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
The dictionary contains the user's name, email, phone number, 
and the property whether the contact is selected.

Create a get_favorites(contacts) function returning a list containing 
only your favorite contacts. Use the filter function to filter only your 
favorite contacts by the favorite field.
'''
import json

def get_favorites(contacts):    
    return list(filter(lambda x: x["favorite"], contacts))

if __name__ == "__main__":
    contacts_list = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
{
    "name": "Jack Daniels",
    "email": "jack.daniels@vestibul.co.uk",
    "phone": "(558) 881-3420",
    "favorite": True,
},
{
    "name": "Jimmy Hendrics",
    "email": "jim.hendrix@vestibul.co.uk",
    "phone": "(332) 714-5732",
    "favorite": False,
},
{
    "name": "Donald Trump",
    "email": "donald.trump@vestibul.co.uk",
    "phone": "(080) 014-2722",
    "favorite": True,
}]
    
    print(json.dumps(get_favorites(contacts_list), indent=4))
    

    