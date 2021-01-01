from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
	padding = message[-message[-1]:]
	return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
	# Derive AES key from shared secret
	sha1 = hashlib.sha1()
	sha1.update(str(shared_secret).encode())
	key = sha1.digest()[:16]
	# Decrypt flag
	ciphertext = bytes.fromhex(ciphertext)
	iv = bytes.fromhex(iv)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(ciphertext)
	if is_pkcs7_padded(plaintext):
		return unpad(plaintext, 16).decode('utf-8')
	else:
		return plaintext


def Point_addition(v1,v2):
	O = (0,0)

	if v1 == O:   
		return v2

	elif v2 == O: 
		return v1

	else:         
		x1,y1 = v1
		x2,y2 = v2

		if (x1 == x2) and (y1 == -y2): 
			return O

		else: 

			if v1 != v2: 
				l = (y2 - y1) * pow(x2-x1, -1 ,E['p'])

			else: 
				l = ( ( 3*pow(x1,2) + E['a'] ) * pow(2 * y1,-1 , E['p']) ) 

	x3 = (l**2 - x1 - x2 ) % E['p']      
	y3 = (l*(x1 - x3) - y1) % E['p'] 

	return (x3,y3)


def Scalar_Multiplication(n,Q):
	R = (0,0)

	while n > 0: 

		if n % 2 == 1: 
			R = Point_addition(R, Q)

		Q = Point_addition(Q,Q) 
		n = n//2

	return R



E = {'a':497,'b':1768,'p':9739}

n_B = 6534
q_x = 4726


pos_Qy = [] 

for y in range(1,E['p']):
	if ( pow(y,2) - pow(q_x,3) - E['a']*q_x - E['b'] ) % E['p'] == 0: # (y^2 - x^3 - a*x - b) % p == 0
		pos_Qy.append(y)


for q_y in pos_Qy:
	test_Q = (q_x , q_y)

	S = Scalar_Multiplication(n_B,test_Q) 
	print(S)


	shared_secret = 1791 
	iv = 'cd9da9f1c60925922377ea952afc212c'
	ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

	flag = decrypt_flag(shared_secret, iv, ciphertext)
	if 'crypto{' in flag:
		print(flag)
		break

