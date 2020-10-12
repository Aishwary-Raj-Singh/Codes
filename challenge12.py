from pwn import xor

KEY1_string = bytearray.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
KEY2_string = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(KEY1_string)
print(KEY2_string)

answer = 'crypto{'

def get_key(hex_string, answer1):

    key = ''
    for i in range(len(answer)):
        key += chr(hex_string[i] ^ ord(answer[i]))
    return key

key = get_key(KEY1_string, answer)
print(key)
#print(KEY1_string)
def get_flag(hex_string, flag_key):

    flag = ''
    x = len(flag_key)
    for i in range(len(hex_string)):
        flag += chr(hex_string[i] ^ ord(flag_key[i%x]))
    return flag

flag = get_flag(KEY2_string, key)
print(flag)
