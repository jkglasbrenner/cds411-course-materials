#!/usr/bin/env python

import numpy as np

mylist_2d = [[87, 84, 91],
             [19, 64, 25],
             [24, 95, 9]]

mymatrix_2d = np.array(mylist_2d)

mymatrix_2d.shape

myvector_1d = np.array([87, 84, 91, 19, 64])

# Slicing

print(myvector_1d[1:4])
print(mymatrix_2d[:, 1])
print(mymatrix_2d[0:2, 1:3])
print(mymatrix_2d[[0, 2]])

mymatrix_3d = np.array([[[1, 2], [1, 2]], [[1, 2], [1, 2]]])

random_vec = np.random.uniform(low=0, high=10, size=50)
print(random_vec < 5)

print(random_vec[random_vec < 5])
print(random_vec[np.logical_not(random_vec < 5)])

vector_sum = 0
for row in random_vec:
    vector_sum += row

print(random_vec.sum())

vector1 = np.random.uniform(low=-100, high=100, size=3)
vector2 = np.random.uniform(low=-100, high=100, size=3)

print(vector1 * vector2)
print(vector1 + vector2)
print(vector1 ** 3)

# dot product
print(np.dot(vector1, vector2))
print(np.sum(vector1 * vector2))

print(vector1.dot(vector2))

# Matrix dot vector
print(mymatrix_2d.dot(vector1))
print(mymatrix_2d.dot(vector1).dot(vector2))

matrix2 = np.random.uniform(low=-100, high=100, size=(3, 3))

# Matrix matrix dot product
print(matrix2.dot(mymatrix_2d))
print(mymatrix_2d.dot(matrix2))

# Useful methods
print(random_vec.cumsum())
print(random_vec.mean())
print(random_vec.max())
print(random_vec.std())
print(random_vec.round(2))

# Transpose two-dimensional matrix
print(matrix2.T)

# Convert a numpy array to a Python list
random_vec.tolist()
