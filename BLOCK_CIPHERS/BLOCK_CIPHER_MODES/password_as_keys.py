from Crypto.Cipher import AES

import requests
import hashlib
import sys
import binascii

url = 'http://aes.cryptohack.org/passwords_as_keys/'
encrypt = 'encrypt_flag/'
decrypt = 'decrypt/'

r = requests.get(url+encrypt)
data = r.json()
ciphertext_hex = data['ciphertext']

print("Ciphertext: ", ciphertext_hex)

with open('words', 'r') as f:
    for word in f:
        word = word.strip()
        attempted_key = hashlib.md5(word.encode()).hexdigest()

        ciphertext = bytes.fromhex(ciphertext_hex)
        key = bytes.fromhex(attempted_key)
        cipher = AES.new(key, AES.MODE_ECB)
        try:
            decrypted = cipher.decrypt(ciphertext)
            result = binascii.unhexlify(decrypted.hex())
            if result.startswith('crypto{'.encode()):
                print("key is %s" % word)
                print(result.decode('utf-8'))
                sys.exit(0)
        except ValueError as e:
            continue

