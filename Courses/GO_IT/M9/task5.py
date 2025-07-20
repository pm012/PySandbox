'''
In module 5, we wrote the sanitize_phone_number function to normalize a string with a phone number. Let us remind you that when 
receiving the following strings:

    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
We received the following output:

380501233234
0503451234
0508889900
380501112222
380501112211
Imagine that elsewhere in the program we have a requirement to make a conclusion in such a format:

+380501233234
+380503451234
+380508889900
+380501112222
+380501112211
And here, creating a decorator for the sanitize_phone_number function is ideal. 
The decorator should add the +38 prefix for short numbers and only the + sign for full international numbers (with 12 characters). 
You should implement the format_phone_number decorator for the sanitize_phone_number function with the required functionality.
'''

def format_phone_number(func):
    def phone_output_formatting(phone):
        phone = func(phone)        
        if len(phone)==12 and phone.isdigit():
            return "+"+func(phone)
        elif len(phone)==10 and phone.isdigit():
            return "+38"+func(phone)
        elif len(phone)==13 and phone.startswith('+') and phone[1:].isdigit():
            return func(phone)
                
    return phone_output_formatting
        


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

if __name__ == "__main__":
    phones_lst = [ "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

    for phone in phones_lst:
        print(sanitize_phone_number(phone))
