# lists
def slices(data):
    # data[p1:p2:p3] - extract list from p1 indx to p2 index with step p3
    odd_numbers = data[0:len(data):2]
    print(odd_numbers)
    return odd_numbers

def format_ingredients(items):
    #write items in following format item[1], item[2]... item[n-1], item[n]
    i = 0
    str = ""
    while i < len(items):
        if i == len(items) - 2:
            str += items[i] + " and "
        elif i == len(items) - 1:
            str += items[i]
        else:
            str += items[i] + ", "
        i += 1
    return str

def prepare_data(data):
    # sorting list, removing extrims and reverse list
    data.sort()
    print(data)
    while True:
        tmp = data[0]
        data.pop(0)
        print(data)
        if tmp != data[0]:
            break

    while True:
        tmp = data[len(data) - 1]
        data.pop()
        print(data)
        if tmp != data[len(data) - 1]:
            break

#------ Module 4, hw4-----

ECTS = {"F": [1, (0, 34), "Unsatisfactorily"], "FX": [2, (35, 59), "Unsatisfactorily"],
        "E": [3, (60, 66), "Enough"], "D":[3, (67, 74), "Satisfactorily"],
        "C":[4, (78, 89), "Good"], "B": [5, (90-95), "Very good"],
        "A": [5, (96, 100), "Perfectly"]}
def get_grade(key):
    res = None
    try:
         res = ECTS[key][0]
         return res
    except KeyError:
        return res

def get_description(key):
    res = None
    try:
        res = ECTS[key][2]
        return res
    except KeyError:
        return res


# -----task5---------------
def lookup_key(data, value):
    result = []
    for key, val in data.items():
        if val == value:
            result.append(key)
    return result


# -------task6-----------------
def split_list(grade):
    less_avg = []
    more_avg = []
    grade.sort()
    tmp = tuple(grade)
    avg = sum(tmp) / len(tmp)
    if len(tmp) > 0:
        for item in tmp:
            if item <= avg:
                less_avg.append(item)
            else:
                more_avg.append(item)
    return (less_avg, more_avg)


def split_list1(grade):
    less_avg = []
    more_avg = []
    avg = None

    if len(grade) > 0:
        avg = sum(grade) / len(grade)
        for item in grade:
            if item <= avg:
                less_avg.append(item)
            else:
                more_avg.append(item)
    return (less_avg, more_avg)


# -------------------task 7 ----------------
points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def list_coordinates(coordinates):
    res = []
    if len(coordinates) > 1:
        a = coordinates[0]
        for el in range(1, len(coordinates)):
            b = coordinates[el]
            if a <= b:
                tpl = (a, b)
            else:
                tpl = (b, a)
            res.append(tpl)
            a = b
    return res


def calculate_distance(coordinates):
    if len(coordinates) <= 1:
        return 0

    dist = 0
    coord_tpls = list_coordinates(coordinates)
    for key in coord_tpls:
        dist += points[key]

    return dist


# -----task-8-----------------------------
def game(terra, power):
    res = power
    for list in terra:
        for el in list:
            if el <= res:
                res += el
            else:
                break
    return res


# ------------------task -9 --------------
def is_valid_pin_codes(pin_codes):
    res = False
    if len(pin_codes) > 0 and len(pin_codes) == len(set(pin_codes)):
        for pin in pin_codes:
            if not isinstance(pin, str):
                return False
            elif len(pin) == 4 and pin.isdigit():
                res = True
            else:
                return False

    return res


# --------------task -10 --------------------
from random import randint


def get_random_password():
    pwd = ''
    for i in range(1, 9):
        pwd += chr(randint(40, 126))
    return pwd


# --------------task-11----------------
def is_valid_password(password):
    has_lower_alpha = False
    has_upper_alpha = False
    has_digit = False

    if (len(password) == 8):
        for ch in password:
            if not has_digit:
                if ch.isdigit():
                    has_digit = True
            if not has_lower_alpha or not has_upper_alpha:
                if ch.isalpha():
                    if ch.isupper():
                        has_upper_alpha = True
                    else:
                        has_lower_alpha = True
            if (has_lower_alpha and has_upper_alpha and has_digit):
                return True
    return False


# --------------------- task-13-----------
from pathlib import Path


def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_dir():
            folders.append(i.name)
        if i.is_file():
            files.append(i.name)

    return files, folders


p = Path('/home/devel/Documents')

# ----------task-14 -------------------
import sys


def parse_args():
    result = ""
    sys.argv.pop(0)
    result = " ".join(sys.argv)
    return result


# -----------------
# data = [-5, 8, 10, 25, 4, -6, 25, 1, -6]
# prepare_data(data)
# ------------------------
# ingridients = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
# print(format_ingredients(ingridients))
# ----------------------
# fact(3)
# ----------task4-----------
# ECTS = {"F": [1, (0, 34), "Unsatisfactorily"], "FX": [2, (35, 59), "Unsatisfactorily"], "E": [3, (60, 66), "Enough"], "D":[3, (67, 74), "Satisfactorily"], "C":[4, (78, 89), "Good"], "B": [5, (90-95), "Very good"],  "A": [5, (96, 100), "Perfectly"]}
# print( get_description("E"))
# print( get_description("M"))
# print(get_grade("D"))
# print(get_grade("N"))
# -------task5- testing------
# dict1 = {6 : "accounting",9: "development", 7: "management", 8: "development"}
# print(lookup_key(dict1, "QAs"))
# print(lookup_key(dict1, "management"))
# print(lookup_key(dict1, "development"))
# ------------------ task6 - testing ---------------
# data = [5, 8, 10, 25, 4, 6, 25, 1, 6]
# print(split_list(data))
# ------------------task7 - testing --------------
# tst = [0, 1, 3, 2, 0]

# print(list_coordinates(tst))

# print(calculate_distance(tst))
# -----------------task8 - testing -----------
# terra1 = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
# print(game(terra1, 1))
# ----------------task9 - testing ----------

# pins1 = ['1101', '9034', '0011']
# pins2 = ['1101', '9034', 2222]
# pins3 = []
# pins4 = ['1101', '9034', '0011', '9034']
# pins5 = ['1101', '9034', '00']
# pins6 = ['1101', '9034', 'abcd']
# pins7 = ['1111']

# print(is_valid_pin_codes(pins1))
# print(is_valid_pin_codes(pins2))
# print(is_valid_pin_codes(pins3))
# print(is_valid_pin_codes(pins4))
# print(is_valid_pin_codes(pins5))
# print(is_valid_pin_codes(pins6))
# print(is_valid_pin_codes(pins7))
# -----------------task10 - testing -------------
# print(get_random_password())
# -----------------task11 -testing---------------
"""
#False <8
print(is_valid_password('Ab9'))
#False >8
print(is_valid_password('Ab9abcabcabc###'))
#True
print(is_valid_password('Secret0!'))
#False no lower case
print(is_valid_password('SECRET0!'))
#False no upper case
print(is_valid_password('secret0!'))
#False no digit
print(is_valid_password('NmlDl1V0'))
"""
# ----------------task13 - testing ---------------
# print(parse_folder(p))
# ----------------task14 - testing -----------------
# print(parse_args())