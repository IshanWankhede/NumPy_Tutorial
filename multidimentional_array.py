import numpy as np 

# array = np.array('A')

# print(array.ndim)  #0 dimensional array

# array = np.array(['A', 'B', 'C'])

# print(array.ndim) #1 dimensional array 

# array = np.array([['A', 'B', 'C'], 
#                   ['D', 'E', 'F'], 
#                   ['G', 'H', 'I']])

# print(array.ndim) #2 dimensional array

'''array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '1']]])

print(array.ndim) #3 dimensional array

print(array.shape) # it returns Tuple (3, 3, 3) ==> (depth, no_of_row, no_of_columns)

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1.shape)   # (5,) → 1 dimension with 5 elements

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2.shape)   # (2, 3) → 2 rows, 3 columns

# 3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3.shape)   # (2, 2, 2) → 2 blocks, each with 2 rows and 2 columns '''


array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '1']]])

# print(array[0][0][1])   #chain indexing through array "B" 

print(array[0, 0, 0])   # mutidimensional indexing with numpy "A"

word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]

print(word)