import numpy as np
np.array(list)

list = [10, 20, 30, 40, 50]

vctr = np.array(list)

print("List : ")
print(vctr)

# Menghitung dua vector dengan numpy
v1 = np.array([2, 1, 2])
v2 = np.array([3, 1, 5])

print("List v1: ")
print(v1)
print("List v2:")
print(v2)

vctr_dot = v1.dot(v2)
print("Dot product of two vector = ", vctr_dot)
