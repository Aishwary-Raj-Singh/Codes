from Crypto.PublicKey import RSA
f= open('2048b-rsa-example-cert.der', 'r')
key = RSA.importKey(f.read())

print(key.d)
print(key.n)
print(key.e)

