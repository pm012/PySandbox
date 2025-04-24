def normal_name(list_name):
    res = []
    for i in map(lambda x: x.capitalize(), list_name):
        res.append(i)
    return res
    
    
if __name__ == "__main__":
    list_name = ["ivan", "petr", "sasha"]
    print(normal_name(list_name))
    # ['Ivan', 'Petr', 'Sasha']