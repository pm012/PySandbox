class Spam:
  __egg = 7
  _private_variable_ = 11
  def print_egg(self):
    print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg) # renamed to _Spam__egg and can be accessed aaaaaaa!!!!!
#encapsulation in Python is fake !!!!
print(s._private_variable_)
print(s.__egg) # object has no attribute egg
