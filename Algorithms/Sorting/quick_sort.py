from faker import Faker
import random

def quick_sort(array):
    if len(array) <=1:
        return array
    else:
        s = array[0]
        n = [i for i in array[1:] if i <= s]
        m = [i for i in array[1:] if i > s]

        return quick_sort(n) + [s] + quick_sort(m)

def sort_list_dict():
    fake = Faker()
    people = [{'name': fake.name(), 'age': random.randint(20, 60)} for x in range(0, 10) ]
    print('Created:')
    for person in people:
        print(person)

    print('_________________________________________________')
    print("Sorted:")
    sorted_people = sorted(people,
                           key=lambda x: (x['name'], x['age']))
    
    for person in sorted_people:
        print(person)


if __name__ == "__main__":
    # Sort by keys
    #sort_list_dict()
    # quick sort
    arr = [random.randint(1, 1000) for i in range(1, 50)]
    print("Not sorted array")  
    print(arr)
    x = quick_sort(arr)
    print("Sorted array")  
    print(x)
    


    
