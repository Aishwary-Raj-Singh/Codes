string = "label"
print("crypto{", end='')
for i in string:
    result = ord(i) ^ 13
    print(chr(result), end='')
print("}")
