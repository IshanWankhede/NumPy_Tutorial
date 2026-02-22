import numpy as np

#filtering = Refers to the process of selecting elements from an array tht match a given condtion  

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65], 
                 [39, 22, 15, 99, 18, 19 ,20, 21]])

teenagers = ages[ages < 18]  #boolean indexing here shape is changed from 2d --> 1d

# adults = ages[ages >= 18]  
adults = ages[(ages >= 18) & (ages < 65)]   #as numpy uses c style arrays so use c style logical oprators no the python one

seniors = ages[ages >= 65]

evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]


print(teenagers)  #[17 16 15]

print(adults) #[21 19 20 30 18 65 39 22 99 18 19 20 21]

# To preserve the array shape we use "where" function 

adults = np.where(ages >= 18, ages, 0)

# adults = np.where(condition, x, y)

# - condition → A boolean array (e.g., ages >= 18).
# - x → Values to choose when the condition is True (here, ages).
# - y → Values to choose when the condition is False (here, 0).
