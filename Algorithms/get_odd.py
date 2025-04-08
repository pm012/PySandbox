"""
You are given an array (which will have a length of at least 3, but could be very large) 
containing integers. The array is either entirely comprised of odd integers or entirely comprised 
of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
"""
def find_outlier(integers)->int:    
    cnt = 0
    res = None
    for i in range(3):        
        if integers[i]%2 != 0:
            cnt+=1
    if cnt > 1:
        for num in integers:
            if num%2 == 0:
                return num
    else:
        for num in integers:
            if num%2 != 0:
                return num
            
if __name__ == '__main__':
    print(find_outlier([2, 4, 6, 8, 10, 11]))
    print(find_outlier([1, 3, 5, 7, 9, 12]))


        


    

    