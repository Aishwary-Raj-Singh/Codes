from Crypto.PublicKey import RSA

key = RSA.importKey(open("key.pem", "rb").read())

n = key.n
e = key.e

print(n)
print(e)
