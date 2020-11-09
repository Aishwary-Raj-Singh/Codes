import matplotlib.pyplot as plt

data = plt.imread('/home/b00139256/Codes/GENERAL/XOR/lemur.png')
plt.imshow(data)
plt.show()
data1 = plt.imread('/home/b00139256/Codes/GENERAL/XOR/flag.png')
plt.imshow(data1)
plt.show()
plt.imshow(data ^ data1)
plt.show()