"""There is a list. It is required to return string made of list items separated by comma and 'and' between two last items"""

def format_ingridients(items: list) -> str:
    res = ", ".join(items[:-1])
    res += f" and {items[-1]}"
    print(res)    
    return res

if __name__ == "__main__":
    ingridients = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegear"]
    format_ingridients(ingridients)
