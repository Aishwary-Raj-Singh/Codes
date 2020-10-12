from pwn import xor

# rule1 KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# rule2 KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# rule3 KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# rule4 FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5f24

KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')

print(KEY1)

###XOR with KEY1 in rule2 on both sides so that KEY1 ^ KEY1 = 0 i.e, KEY2 ^ 0 = KEY2

KEY2 = xor(bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'), KEY1)

print(KEY2)

###XOR both sides with KEY2 in rule3

KEY3 = xor(bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'), KEY2)

print(KEY3)

##XOR kEY2 and KEY3

KEY4 = xor(KEY2, KEY3)

print(KEY4)

##XOR KEY1 and KEY4

KEY5 = xor(KEY1, KEY4)

print(KEY5)

##XOR in equation FLAG ^ KEY5 ^ KEY5 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf ^ KEY5

FLAG = xor(bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'), KEY5)

print(FLAG)


