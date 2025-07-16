'''
Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from the range [0..23] – we will be using military time), 
minutes (from the range [0..59]) and seconds (from the range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", 
with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside
the objects by +1/-1 second respectively.
Use the following hints:

all object properties should be private;
consider writing a separate function (not method!) to format the time string.
Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.

Expected ouput:
23:59:59
00:00:00
23:59:59
'''

class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        

    def convert_str(self, val: int)->str:
        if val<10:
            return "0"+str(val)
        else:
            return str(val)
        
    def next_second(self):
        self.__second+=1
        if self.__second == 60:
            self.__second = 0
            self.__minute+=1
            if self.__minute == 60:
                self.__minute=0
                self.__hour+=1
                if self.__hour == 24:
                    self.__hour=0
        
    def prev_second(self):
        self.__second-=1
        if self.__second == -1:
           self.__second = 59
           self.__minute-=1
           if self.__minute == -1:
               self.__minute=59
               self.__hour-=1
               if self.__hour == -1:
                   self.__hour=23
    
    def __str__(self):        
        return f"{self.convert_str(self.__hour)}:{self.convert_str(self.__minute)}:{self.convert_str(self.__second)}"
    
if __name__ == "__main__":
    timer = Timer(23, 59, 59)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)
    
    
        
        