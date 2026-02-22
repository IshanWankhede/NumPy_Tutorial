import numpy as np

array = np.array([[1,2,3,4], 
                  [5,6,7,8], 
                  [9,10,11,12], 
                  [13,14,15,16]])

# array[start:end:step]

# ROW SELECTION ===============>

# print(array[-1]) #[13 14 15 16] 
# print(array[-2]) #[9,10,11,12]

# print(array[0]) #[1,2,3,4] 
# print(array[1]) #[5,6,7,8]
# print(array[2]) #[9,10,11,12]
# print(array[3]) #[13,14,15,16]

# print(array[0:3])  # staring with 0 ending till 3 where 3 is exclusive

# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# print(array[0:4:2]) 

# [[ 1  2  3  4]
#  [ 9 10 11 12]]

# print(array[::2])   by doing this :: we are telling numpy to select all the rows 

# print(array[::-1])  by doing this numpy will return all the rows revered 

# [[13 14 15 16]
#  [ 9 10 11 12]
#  [ 5  6  7  8]
#  [ 1  2  3  4]]

# COLUMN SELECTIO ===============>

# print(array[:, 0])    #here : is for selection all the rows and geting the 0th index column

# [ 1  5  9 13]

# print(array[:, 0:3])

# [[ 1  2  3]
#  [ 5  6  7]
#  [ 9 10 11]
#  [13 14 15]]

# print(array[:, ::2])

# [[ 1  3]
#  [ 5  7]
#  [ 9 11]
#  [13 15]]