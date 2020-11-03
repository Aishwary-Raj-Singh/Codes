import math
p =  29
a = (p-1)/2
print(a)
ints = [14, 6, 11]
for i in range(1, p):
    res1 = pow(i,a)
#print(res1)
    while(res1 > 0):
        res1 = res1 % a
        a = res1/a
    print("Result 1: % d" %i)

#    result = i % p
#    print("Mod of % d is % d" %(i,result))
#    print(math.sqrt(result))
#print(math.sqrt(6))

