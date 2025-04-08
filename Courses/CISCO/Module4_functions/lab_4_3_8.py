# A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

# In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.

# Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

# The functions:

# are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
# take one argument (the value corresponding to their names)
# Complete the code in the editor and run it to check whether your output is the same as ours.

# Here is some information to help you:

# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.

def liters_100km_to_miles_gallon(liters):
    return 100 * 0.621371192/liters * 3.785411784

def miles_gallon_to_liters_100km(miles):
    return (100 * 3.785411784)/(miles * 1.609344)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))