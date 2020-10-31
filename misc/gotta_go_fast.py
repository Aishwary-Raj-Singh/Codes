import binascii

cipher1_flag = "e5db9fb69d3700592fb242ce7385676e3e423fb4babc5900d8477eae"
cipher2 = "52d339b35ee159f4f6e8d78fc3d360a1e536fe628da1c94c699d36f7"
message = "00000000000000000000000000000000000000000000000000000000"
m_in_b = bytes.fromhex(message)
print(m_in_b)
cipher1 = bytes.fromhex(cipher1_flag)
print(cipher1)
cipher2 = bytes.fromhex(cipher2)
print(cipher2)


#length_key = min(len(cipher2), len(m_in_b))
#key = ""
#for i in range(length_key):
#    key = bytes([cipher2[i] ^ m_in_b[i]])

#print(key)

#length_flag = min(len(cipher1), len(key))

#for i in range(length_flag):
#    flag = bytes([cipher1[i] ^ key[i]])
#flag = bytes.fromhex("40b71d1417fbc257ff14f054c722ab46d41a7a55fba60349779585c1")
flag = bytes.fromhex("40b71d1417fbc257ff14f054c722ab46d41a7a55fba60349779585c1").decode("ASCII")
print(flag)

