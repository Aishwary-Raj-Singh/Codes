a = 26513
b = 32321
while(b>0):
    t = b
    b = a%b
    a = t
print(a)
