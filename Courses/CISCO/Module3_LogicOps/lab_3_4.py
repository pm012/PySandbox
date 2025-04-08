def beatles():
    #step 1: create an empty list named beatles;
    # step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
    # step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
    # step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
    # step 5: use the insert() method to add Ringo Starr to the beginning of the list.
    # step 1
    beatles = []
    print("Step 1:", beatles)

    # step 2
    beatles.append("John Lennon")
    beatles.append("Paul McCartney")
    print("Step 2:", beatles)

    # step 3
    for i in range(2):        
        if i == 0: 
            prompt = "Would you like to add Stu Sutcliffe? (y/n): "
            value = "Stu Sutcliffe"
        elif i == 1: 
            prompt = "Would you like to add Pete Best? (y/n): "
            value = "Pete Best"
            
        answer = input(prompt)
        if answer == "y":
            beatles.append(value)
            
    print("Step 3:", beatles)

    # step 4
    del beatles[-1]
    beatles.remove("Stu Sutcliffe")
    print("Step 4:", beatles)

    # step 5
    beatles.insert(0, "Ringo Star")
    print("Step 5:", beatles)


    # testing list legth
    print("The Fab", len(beatles))




if __name__ == "__main__":
    beatles()
    
    