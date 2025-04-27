import math
def is_square(n):
    sq = math.sqrt(n)
    if (sq - int(sq))==0:
        return True
    
    return False

if __name__ == "__main__":
    print(is_square(64))