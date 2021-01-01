from Crypto.Util.number import getPrime, inverse, bytes_to_long
import numpy as np
import random
import math

FLAG = b'crypto{?????????????????????}'

def gaussianreduction(v1,v2):
    x = v1.dot(v1)
    y = v2.dot(v2)
    if y<x:
        v1.v2=v2,v1
    m = int(np.dot(v1,v2)/(v1.dot(v1)))
    if m ==0:
        return v1,v2
    v2 = v2 - np.multiply(m,v1)
    return gaussianreduction(v1,v2)

def gen_key():
    q = getPrime(512)
    upper_bound = int(math.sqrt(q // 2))
    lower_bound = int(math.sqrt(q // 4))
    f = random.randint(2, upper_bound)
    while True:
        g = random.randint(lower_bound, upper_bound)
        if math.gcd(f, g) == 1:
            break
    h = (inverse(f, q)*g) % q
    return (q, h), (f, g)


def encrypt(q, h, m):
    assert m < int(math.sqrt(q // 2))
    r = random.randint(2, int(math.sqrt(q // 2)))
    e = (r*h + m) % q
    return e


def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m


public, private = gen_key()
q, h = public
f, g = private

m = bytes_to_long(FLAG)
e = encrypt(q, h, m)

print(f'Public key: {(q,h)}')
print(f'Encrypted Flag: {e}')
