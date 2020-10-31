import base64
from binascii import b2a_base64


hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byte_string = bytes.fromhex(hex_string)
print(byte_string)
flag_string = b2a_base64(byte_string)
print(flag_string.decode())
