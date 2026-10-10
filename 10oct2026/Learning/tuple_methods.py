tup= (23, 4, 67, 89, 9, 2, "heloo", "world")
print(tup, type(tup))
print(tup[1:4])
print(tup)
print(tup.index(67))
print(tup.count(9))
print(tup[-1])
print(tup[1:4:2])
print(tup[::-1])


## You cant Directly Modify tuple because they are immutable(so coverted into list and do)
temp= list(tup)
def modify_tup():
    temp.append("russia")
    print(temp)
    temp.pop(4)
    print(temp)
    temp.insert(2,"India")
    print(temp)
    tup = tuple(temp)
    print("modified tuple",tup)
    print("modified list",temp)
modify_tup()

print("origanal",tup)

