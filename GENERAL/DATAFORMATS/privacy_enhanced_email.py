from Crypto.PublicKey import RSA
f= open('cert.pem', 'r')
key = RSA.importKey(f.read())

print(key.d)
print(key.n)
print(key.e)
