p = 28151
# g^n mod p
# find the smallest element g

#Let's start the value of g from 2
g = 2
found = False
while not found:
    for n in range(2,p):
        if pow(g,n,p) == 1:
            break
        if n == p-2:
            print(g)
            found = True
    g=g+1

