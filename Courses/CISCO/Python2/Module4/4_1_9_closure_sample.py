def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]
 
    def inner(str):
        return tg + str + tg2
    return inner

if __name__ == "__main__":
#-------------make_closure sample ---------------------
    fsqr = make_closure(2)
    fcub = make_closure(3)

    for i in range(5):
        print(i, fsqr(i), fcub(i))
    print("End -------------make_closure sample ---------------------")
        
#-------------tag closure---------------
    b_tag = tag('<div>')
    print(b_tag('Monty Python'))
    print("End -------------tag closure sample ---------------------")