import pem

with open('privacy_enhanced_mail.pem', 'rb') as f:
   certs = pem.parse(f.read())
print(certs)
