#import base64
a = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print("The decimal value is = %d" % a)
print("Binary of a = ", bin(a))
print("Hexadecimal of a = ", hex(a))
print("Octal of a = ", oct(a))
b = hex(a)
print(b)
c = b[2:]
print(c)
byte_string = bytearray.fromhex(c)
result = byte_string.decode("ASCII")
print("Final result : %s " % result)

