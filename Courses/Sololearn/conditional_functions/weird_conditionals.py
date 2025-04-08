y = [x if x==1 else x*2 for x in ["1", "2"]][0]
print(y)
y=[]
for x in ["1", "2"]:
    if x==1:
        y.append(x)
    else:
        y.append(x*2)

print(y[0])