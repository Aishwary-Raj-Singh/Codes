import numpy as np
import math

v = [846835985, 9834798552]
u = [87502093, 123094980]

def v_product(i ,j):
    temp = []
    for k in range(len(j)):
        temp.append(i*j[k])
    return temp


def calculate_k(a, b):
    return math.ceil(np.divide(np.dot(a, b), np.dot(a, a)))
    

def reduction(c, d):
    temp = []
    if  c[0] < d[0] and c[1] < d[1]:
        #temp = d
        #d = c
        #c = temp
        m = calculate_k(c, d)
        if m == 0:
            print(np.dot(c, d))
        else:
            c = np.subtract(c, v_product(m, d))
            reduction(c, d)
    else:
        print("u is less than v")
        temp = d
        d = c
        c = temp
        reduction(c, d)

reduction(v, u)
#print(np.dot(v, u))
