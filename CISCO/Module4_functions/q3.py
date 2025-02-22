def duplicates_of_2():
    tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
    duplicates = tup.count(2)
    print(duplicates)
    
def glue_dicts():
    d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
    d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
    d3 = {}
 
    for item in (d1, d2):        
       d3.update(item)
 
    print(d3)
    
def list_to_tuple():
    my_list = ["car", "Ford", "flower", "Tulip"]

    t =  tuple(my_list)
    print(t)



if __name__ == "__main__":
    #duplicates_of_2()
    #glue_dicts()
    #list_to_tuple()
    temperature = float(input('Enter current temperature:'))

    if temperature > 0:
        print("Above zero")
    elif temperature < 0:
        prin("Below zero")
    else:
        print("Zero")
    
    