import shutil

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True


ingredients = ["cheese", "onions", "spam"]
pizza=[]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

#print(pizza.toppings)
number_to_sting = str
print(type(number_to_sting(5)))
