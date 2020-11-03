from pwn import xor

flag = '70369073739b1cd212aad92dbc34095c8e362cd1dca10aa3f626a65c'
key = '19072343529f54da'
res = xor(bytes.fromhex(flag), bytes.fromhex(key))

print(res)
