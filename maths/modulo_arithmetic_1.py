# assume a ≡ b mod m
# calculate gcd of a and m for equation 11 ≡ a mod 6



a = 11
b = 6
while(b>0):
    t = b
    b = a%b
    a = t
print(a)

# then calculate gcd of 8146798528947 and 17 in equation 8146798528947 ≡ b mod 17

a = 8146798528947
b = 17
while(b>0):
    t = b
    b = a%b
    a = t
print(a)


print(min(11 % 6 , 8146798528947 % 17))
