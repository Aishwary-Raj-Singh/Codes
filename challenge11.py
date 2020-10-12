from pwn import xor

KEY1 =bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

#x = xor(bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'), 0)

flag = ""

print(KEY1)

for i in KEY1:
    flag += chr(i ^ 16)

print(flag)

