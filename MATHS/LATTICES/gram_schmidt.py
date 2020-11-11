import numpy as np

def dot_product(i, j):
    return np.dot(i, j)

def v_add(i, j):
    return np.add(i, j)

def v_subtract(i, j):
    return np.subtract(i,j)

def v_divide(i, j):
    return np.divide(i, j)

def v_product(i ,j):
    temp = []
    for k in range(len(j)):
        temp.append(i*j[k])
    return temp


v1 = (4, 1, 3, -1)
v2 = (2, 1, -3, 4)
v3 = (1, 0, -2, 7)
v4 = (6, 2, 9, -5)

l1 = list(v1)
l2 = list(v2)
l3 = list(v3)
l4 = list(v4)

#Calculate u1
u1 = l1
print("U1 is: ", u1)
#temp = []

#To calculate u2
result = v_product(dot_product(v2,u1), u1)
print(result)
u2 = v_subtract(l2, v_divide(result, dot_product(u1, u1)))
print("U2 is: ", u2)

#To calculate u3
result = 0
result = v_product(dot_product(l3,u1),u1)
print(result)
result_u3 = v_subtract(l3, v_divide(result, dot_product(u1, u1)))
print(result_u3)
u3 = v_subtract(result_u3, v_divide(v_product(dot_product(l3, u2), u2), dot_product(u2, u2)))
print("U3 is: ", u3)

#To calculate u4

result = 0
result = v_product(dot_product(l4,u1),u1)
print(result)
result_u4 = v_subtract(l4, v_divide(result, dot_product(u1, u1)))
print(result_u4)
result_u4_1 = v_subtract(result_u4, v_divide(v_product(dot_product(l4, u2), u2), dot_product(u2, u2)))
print(result_u4_1)
u4 = v_subtract(result_u4_1, v_divide(v_product(dot_product(l4, u3), u3), dot_product(u3, u3)))
print("U4 is: ", u4)
print("Flag is: ", round(u4[1],5))

