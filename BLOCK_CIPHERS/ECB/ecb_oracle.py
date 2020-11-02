import requests

url = 'http://aes.cryptohack.org/ecb_oracle/'
encrypt1 = 'encrypt/'


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_{}"
flag = ""

def do_padding(block):
    padding = "A" * (16 - len(block) % 16)
    block_after_padding = padding + block + padding
    return block_after_padding

def encrypt(data):
    print(data)
    
    r = requests.get(url+encrypt1+data.encode().hex())
    data = r.json()
    ciphertext = data['ciphertext']
    print("Ciphertext is: ", ciphertext)
    return ciphertext

while flag[-1:] != "}":
    for l in letters:
        flag_found = flag+l
        block_after_padding = do_padding(flag_found)
        print("Block after padding: ", block_after_padding)
        ciphertext = encrypt(block_after_padding)
        block_size = 2 * ((16 - len(flag_found) % 16) + len(flag_found))
        encrypted_guess = ciphertext[:block_size]
        encrypted_flag = ciphertext[block_size:block_size*2]
        if encrypted_guess == encrypted_flag:
                flag = flag_found
                print(l, end="")
                break
print()
