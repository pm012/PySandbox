"""#---lecture---
#--Specification samples---
#Output numbers 1-15 in decimal, hex, binary, oct formats
for i in range(16):
    s = "int: {0:d}; hex: {0:#x}; bin: {0:#b}; oct: {0:#o}".format(i)
    print(s)

#precision
print ('pi: {:0.3}'.format(3.1415)) # pi: 3.14

# format of neg/positive digits
print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4)) #"1" "+2" "-3" " 4"

# format of element disposition
print("|{:<10}|{:*^10}|{:>10}|".format('left','center','right'))  # |left     |**center**|     right|


#Print numbers 1-12 with  power 3 and power 2 as a table, center columns by 10 symbol width
width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))

s =  "{name!r} {last_name!s}".format(last_name="Dilan", name="Bob")
print(s)  # 'Bob' Dilan - Bob s convert to string, r - print without conversion
"""


# ------task -1 --------
def real_len(text):
    return len(''.join(text.split()))


# ------task -2 ---------------
def find_articles(key, letter_case=False):
    res_list = []
    for article in articles_dict:
        if letter_case:
            if (article['title'].find(key) != -1) or \
                    (article['author'].find(key) != -1):
                print(f"Found {key}")
                res_list.append(article)
        else:
            key = key.lower()
            if (article['title'].lower().find(key) != -1) or \
                    (article['author'].lower().find(key) != -1):
                print(f"Found {key}")
                res_list.append(article)

    return res_list


# -------task -3 -------------
def sanitize_phone_number(phone):
    import re
    pattern = [r'\d+']
    for i in pattern:
        match = re.findall(i, phone)
        return "".join(match)


# -----task -4 -----------------
def is_check_name(fullname, first_name):
    return fullname.startswith(first_name)


# ----------task -5 --------------
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


def get_phone_numbers_for_countries(list_phones):
    phones_dict = {"UA": [], "JP": [], "TW": [], "SG": []}
    ua_phones = []
    jp_phones = []
    tw_phones = []
    sg_phones = []

    """ua_phones ={"UA": '380'}
    jp_phones = {"JP": '81'} 
    tw_phones = {"TW": '886'} 
    sg_phones = {"SG": '65'}"""

    normalized_phone = None
    for phone in list_phones:
        normalized_phone = sanitize_phone_number(phone)
        if normalized_phone.startswith('81'):
            jp_phones.append(normalized_phone)
        elif normalized_phone.startswith('886'):
            tw_phones.append(normalized_phone)
        elif normalized_phone.startswith('65'):
            sg_phones.append(normalized_phone)
        else:
            ua_phones.append(normalized_phone)

    phones_dict = phones_dict.update({"UA": ua_phones, "JP": jp_phones, "TW": tw_phones, "SG": sg_phones})
    return phones_dict


phones = ['+380502590542', ' (886) 5342332', ' +81 50 234 45 45', '   65 2345 52 99', '099 4562343', '050 23452345',
          '+886 8983432']
print(get_phone_numbers_for_countries(phones))

# ---------task1 - testing -------------
# text1 = "Alex\nKdfe23\t\f\v.\r" #11
# text2 = "Al\nKdfe23\t\v.\r" #9
# print(real_len(text1))
# print(real_len(text2))
# ----------task 2 - testing ------------
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

#print(find_articles("Ocean"))
#print(find_articles("Ocean", True))
# ------task-3 testing --------------
# sanitize_phone_number("(050)8889900")
#---------task4 testing -----------
# print(is_check_name("Serhii Kroshka", "Serhii"))
# print(is_check_name("serhii Kroshka", "Serhii"))
# print(is_check_name("Serhii Kroshka", "serhii"))
# print(is_check_name("Alex Kroshka", "Serhii"))
#-----------task 5 testing - ----------------




