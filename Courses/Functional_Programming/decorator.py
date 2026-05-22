# Decorator to be done here
from datetime import datetime
import time

def decorator(func):
    def wraper(*args, **kwargs):
        start = datetime.now()
        print("Start working at ", start)
        result = func(*args, **kwargs)
        endtime = datetime.now()
        print("End working at", endtime)
        duration = endtime - start
        print(f"Execution duration {duration.total_seconds()} seconds" )
        return result
    return wraper

@decorator
def  my_func(seconds: int):
    time.sleep(seconds)  


print("With 10 seconds")
my_func(10)


print("with 28 seconds:")
my_func(28)      
        