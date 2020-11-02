import requests

url = 'http://aes.cryptohack.org/block_cipher_starter/'
encrypt = 'encrypt_flag/'
decrypt = 'decrypt/'

r = requests.get(url+encrypt)
data = r.json()
ciphertext = data['ciphertext']

print("Ciphertext: ", ciphertext)

r = requests.get(url+decrypt+ciphertext+'/')
data = r.json()
plaintext = data['plaintext']

print("Plaintext is in hex format: ", plaintext)

print("Plaintext is: ", bytes.fromhex(plaintext).decode())
