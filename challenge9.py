plainstring = "label"
print("The original string is = " + str(plainstring))
result_binary = ' '.join(format(ord(i), 'b') for i in plainstring)
#print("The binary of original string is = " + str(result_binary))
for i in result_binary:
    print(i, end = '')


number1 = 13
print("The original number = " + str(number1))
binary_number1 = bin(number1)[2:]
print("The binary number is " + str(binary_number1))


