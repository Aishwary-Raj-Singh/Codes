# v = (2,6,3), w = (1,0,0) and u = (7,7,2), calculate 3*(2*v - w) ∙ 2*u

v1 = (2*2,2*6,2*3)
print(v1[0])
print(v1[1])
print(v1[2])
w1 = (v1[0]-1 , v1[1]-0 , v1[2]-0)
print(w1)
m1 = (3*w1[0] , 3*w1[1] , 3*w1[2])
print(m1)
u1 = (2*7,2*7,2*2)
print(u1)
print(m1[0]*u1[0] + m1[1]*u1[1] + m1[2]*u1[2])
