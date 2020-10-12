# extended gcd formula =  s*a + t*b = gcd(a,b)
# Remember s = s1 - q*s2  && t = t1 - q*t2
# Remember s1 = 1 & s2 =0 && t1 = 0 & t2 = 1
a = 26513
b = 32321
s1 = 1
s2 = 0
t1 = 0
t2 = 1

while(a!=0):
    q = b//a
    r = b%a
    s = s1 - q*s2
    t = t1 - q*t2
    a = r
    b = a

print(a)
print(s)
print(t)
