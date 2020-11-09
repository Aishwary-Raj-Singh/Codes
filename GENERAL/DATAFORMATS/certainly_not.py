from Crypto.PublicKey import RSA

#used the below command to convert der to pem
#openssl x509 -inform DER -outform PEM -in 2048b-rsa-example-cert.der -out mykey.pem

f= open('mykey.pem', 'r')
key = RSA.importKey(f.read())

#print("Private exponent: ", key.d)
print("Modulus is: ", key.n)
#print("Public exponent: ", key.e)

