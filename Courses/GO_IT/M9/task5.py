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

#TODO