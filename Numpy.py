import numpy as np

temp = [-1.5, -1.2, 0.0, 2.1, 24.2]

np_temp = np.array(temp)

print(3*np_temp)
print(np.array([42,1337], np.int8)) # 1 Byte pro Zahl

dt = np.dtype("i8")
print(dt.byteorder)
print(dt.type)

print("Hello World")
print("test Hallo welt")
print("Ich hab Covid!!")
print("Ich habe kein bock")
