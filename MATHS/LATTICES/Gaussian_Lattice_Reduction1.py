import numpy as np
import math

v1 = [846835985, 9834798552]
v2 = [87502093, 123094980]

print(v1)
print(v2)
if v1[0] > v2[0]:
    if v1[1] > v2[1]:
        print("v1 is greater than v2")
        temp = v2
        v2 = v1
        v1 = temp
        print(v1)
        print(v2)

#print("V1 is: ", v[0])
#print("V2 is: ", v[1])
#print("U1 is: ", u[0])
#print("U2 is: ", u[1])

#u1 = v1

#print("U1: ", u1)

k = np.dot(v2, v1)//np.dot(v1, v1)
print("K :", math.floor(k))

v2 = np.subtract(v2, np.dot(k, v1))
print("Printing vectors:")
print(v1)
print(v2)
if v1[0] > v2[0]:
    if v1[1] > v2[1]:
        print("v1 is greater than v2")
        temp = v2
        v2 = v1
        v1 = temp
        print("Printing vectors after swapping :")
        print(v1)
        print(v2)

k = np.dot(v2, v1)//np.dot(v1, v1)
print("K :", math.floor(k))
v2 = np.subtract(v2, np.dot(k, v1))
print("Printing Vectors :")
print(v1)
print(v2)
print(np.dot(v1,v2))
