import numpy as np 

#Scalar arithimetic 

array = np.array([1, 2, 3])

print(array + 1)   #[2 3 4]
print(array - 2)   #[-1  0  1]
print(array * 3)   #[3 6 9]
print(array / 4)   #[0.25 0.5  0.75]
print(array ** 5)  #[  1  32 243]

#Vectorized Math Functions 

array = np.array([1.01, 2.5, 3.99])

print(np.sqrt(array))  #[1.         1.41421356 1.73205081]

print(np.round(array))  #[1. 2. 4.]
print(np.ceil(array))  #[2. 3. 4.]  round up
print(np.floor(array)) #[1. 2. 3.]  round down

print(np.pi)  # return the value of pi


#EXERCISE

radii = np.array([1, 2, 3])

print(np.pi * radii*radii) # [ 3.14159265 12.56637061 28.27433388]

#ELEMENT WISE ARITHIMETIC 

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)  #[5 7 9]
print(array1 - array2)  #[-3 -3 -3]
print(array1 * array2)  #[ 4 10 18]
print(array1 / array2)  #[0.25 0.4  0.5 ]
print(array1 ** array2) #[  1  32 729]

# COMPARISON OPERATORS   ===> this will return a boolean array

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100) # [False False  True False False False]

print(scores >= 60) 


scores[scores < 60] = 0

print(scores)  #[ 91   0 100  73  82  64]



# Element Wise Operator :---->  - Same shape → Works directly.

# 2D vs 1D
A = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])
print(A + b)

# [[11 22 33]
#  [14 25 36]]