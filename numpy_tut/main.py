import numpy as np

l1 = [1,2,4]
l2 = [4,5,6]
a = np.array([l1])
b = np.array([l2])


dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)


np_dot = np.dot(a,b)
print(np_dot)

