import base64

hexadecimal_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

byte_string = bytearray.fromhex(hexadecimal_string)

print(byte_string)

bytes_to_hex64 = base64.b64encode(byte_string)

print(str(bytes_to_hex64))
