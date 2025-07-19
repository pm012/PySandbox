'''
Last time, we implemented two functions. The first one, get_grade, accepts the ECTS grade as a key and returns the corresponding five-point grade (first column of the table). The second one, get_description, also takes the ECTS grade as a key but returns an explanation of the grade in text format (the last column of the table). For a non-existent key, 
functions must return None value.

You should implement a higher-order function, get_student_grade, that accepts an option parameter. 
If it is equal to the value "grade", then the function must return the get_grade function; if its value is equal to "description", 
it has to return the get_description function. If the parameter does not match the specified values, then the get_student_grade function must 
return a None value.
'''

def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


def get_student_grade(option):
    match option:
        case "grade":
            return get_grade
        case "desctiption":
            return get_description
        case _:
            return None
        
# Or another implementation
def get_student_grade1(option):
    if option == 'grade':
        return get_grade
    elif option == 'description':
        return get_description
    else:
        return None