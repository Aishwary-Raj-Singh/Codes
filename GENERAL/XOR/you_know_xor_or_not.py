from pwn import xor 

hex_string1 = bytearray.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
hex_string2 = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(hex_string1)
print(hex_string2)

print(len(hex_string1))

#for i in len(hex_string1):
#    print(chr(ord(hex_string1[i])), end='')

flag = "crypto{"
print(len(flag))
key = ''

#for i in range(17):
#    flag_len = len(flag)
#    print(hex_string1[i])
#    print(ord(flag[i]))
#   key += xor(hex_string1[i], ord(flag[i]))
#    print(key)
#    key += chr(ord(xor(hex_string1[i], ord(flag[i%flag_len]))))
#print(key+'y')
key = 'myXORkey'
len_key = len(key)
for i in range(len(hex_string1)):
    flag += chr(xor(hex_string1[i], ord(key[i%len_key])))
print(flag)
#    print(ord(i), end='')
    
