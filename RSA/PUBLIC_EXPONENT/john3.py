#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes


n = 19402640770593345339726386104915705450969517850985511418263141255686982818547710008822417349818201858549321868878490314025136645036980129976820137486252202687238348587398336652955435182090722844668488842986318211649569593089444781595159045372322540131250208258093613844753021272389255069398553523848975530563989367082896404719544411946864594527708058887475595056033713361893808330341623804367785721774271084389159493974946320359512776328984487126583015777989991635428744050868653379191842998345721260216953918203248167079072442948732000084754225272238189439501737066178901505257566388862947536332343196537495085729147
e = 3
c = 5603386396458228314230975500760833991383866638504216400766044200173576179323437058101562931430558738148852367292802918725271632845889728711316688681080762762324367273332764959495900563756768440309595248691744845766607436966468714038018108912467618638117493367675937079141350328486149333053000366933205635396038539236203203489974033629281145427277222568989469994178084357460160310598260365030056631222346691527861696116334946201074529417984624304973747653407317290664224507485684421999527164122395674469650155851869651072847303136621932989550786722041915603539800197077294166881952724017065404825258494318993054344153


d = -1
while d == -1:
    p = getPrime(1024)
    q = getPrime(1024)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)

n = p * q

flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
pt = bytes_to_long(flag)
print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")

pt = pow(c, d, n)
decrypted = long_to_bytes(pt)
print(decrypted)

