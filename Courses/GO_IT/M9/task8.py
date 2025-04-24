# 8. Create a function that takes a list of dictionaries and returns a list of emails.
# The function should take a list of dictionaries as an argument, where each dictionary represents a contact with the following keys: name, email, phone, and favorite. The function should return a list of emails from the contacts.
def get_emails(list_contacts):
    res = []
    for i in map(lambda x: x['email'], list_contacts):
        res.append(i)
    return res
if __name__ == "__main__":
    list_conacts = [{
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }, {
        "name": "Hodge Mcclain",
        "email": "hodge.mcclain@gmail.com",
        "phone": "1-800-555-0123",
        "favorite": True,
    }, {
        "name": "Kalvin Clain",
        "email": "kalvin.clain@ukr.net",
        "phone": "1-800-555-0123",
        "favorite": True}]
    print(get_emails(list_conacts))