# What is the inverse element: 3 * d ≡ 1 mod 13?

a = 7
m = 11

a = a%m
for i in range(13):
    if((a*i)%m == 1):
        print(i)

