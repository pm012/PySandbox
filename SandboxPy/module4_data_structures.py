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

#------ End Module 4, hw4-----

#-----------------
#data = [-5, 8, 10, 25, 4, -6, 25, 1, -6]
#slices(data) #[-5, 10, 4, 25, -6]
#-----------------------------
#ingridients = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
#print(format_ingredients(ingridients)) #result = 2 eggs, 1 liter sugar, 1 tsp salt and vinegar
#------ Module 4, hw4 implementation-----
ECTS = {"F": [1, (0, 34), "Unsatisfactorily"], "FX": [2, (35, 59), "Unsatisfactorily"], "E": [3, (60, 66), "Enough"], "D":[3, (67, 74), "Satisfactorily"], "C":[4, (78, 89), "Good"], "B": [5, (90-95), "Very good"],  "A": [5, (96, 100), "Perfectly"]}
print( get_description("E"))
print( get_description("M"))
print(get_grade("D"))
print(get_grade("N"))

#------ Module 4, hw4 implementation end-----
