from pwn import xor

hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

result = bytes.fromhex(hex_string)
flag = []
for i in result:
    flag += xor(chr(i), 16)
for i in flag:
    print(chr(i), end='')
print()
