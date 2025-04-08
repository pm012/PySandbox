import sys

def parse_args():
    result = " ".join(sys.argv[1:])
    print(result)
    return  result



if __name__ == "__main__":
    parse_args()