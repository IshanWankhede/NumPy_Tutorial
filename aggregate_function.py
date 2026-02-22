import numpy as np

#Aggregate functions = summarize data and typically return a single value 

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(np.sum(array))

print(np.mean(array))
print(np.std(array))   #standard deviation 
print(np.var(array))   # varience = (std)^2

print(np.min(array))  #returns min value in an array
print(np.max(array))  #returns max value in an array

print(np.argmin(array)) #returns the position of the minimum value (index_no)
print(np.argmax(array))

print(np.sum(array, axis=0))  # this returns an list of sum of array of all the column 

# axis = 0 is column 
# axis = 1 is rows