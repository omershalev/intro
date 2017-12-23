import numpy as np

# 1D array (vector) definition
vec = np.array([1,2,3,4,5])
print vec

# 2D array definition
mat = np.array([[1,2,3], [4,5,6]])
print mat

# Zeros and ones (3D arrays)
zeros = np.zeros((2,2,2))
print zeros
ones = np.ones((3,3,3))
print ones

# Identity matrix
print np.identity(3)

# Size
print mat.shape

# Reshape
print np.reshape(mat, (3,2))

# Transpose
print np.transpose(mat)

# Flatten
print mat.flatten()

# Element-wise arithmetics
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])

print a + b
print a - b
print a * b
print a / b
print a % b

# Sum and product
print np.sum(mat, axis=0)
print np.sum(mat, axis=1)
print np.sum(mat)
print np.prod(mat, axis=0)
print np.prod(mat, axis=1)
print np.prod(mat)

# Min and max
print np.min(mat, axis=0)
print np.min(mat, axis=1)
print np.min(mat)
print np.max(mat, axis=0)
print np.max(mat, axis=1)
print np.max(mat)

# Mean and std
print np.mean(mat, axis=0)
print np.mean(mat, axis=1)
print np.mean(mat)
print np.std(mat, axis=0)
print np.std(mat, axis=1)
print np.std(mat)

# Dot product
a = np.array([1,2])
b = np.array([3,4])
print np.dot(a, a)

# Determinant
A = np.array([[1,2], [2,1]])
print np.linalg.det(A)

# Eigenvalues and eigenvectors
vals, vecs = np.linalg.eig(A)
print vals
print vecs

# Inverse
print np.linalg.inv(A)

# Matrix multiplication
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
print np.matmul(A,B)