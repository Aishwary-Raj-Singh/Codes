results = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

for i in range(851,1000):
    for j in range(1000):
        if((results[0] * j) % i) == results[1]:
            if((results[1] * j) % i) == results[2]:
                print("crypto{",i,",",j,"}")
