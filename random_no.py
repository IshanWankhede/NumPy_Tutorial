import numpy as np

rng = np.random.default_rng()

print(rng.integers(low=1, high=101, size=3))

print(rng.integers(low=1, high=101, size=(3, 2)))


print(np.random.uniform(low=-1, high=1, size=(3, 2)))  # generates a random floating poin no between 0 and 1

#< =========================================================================== ># 

rng = np.random.default_rng()

array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)

print(array)

fruits = np.array(["🍎", "🍍", "🍊", "🥥", "🍌"])

fruit = rng.choice(fruits, size=(10,10))

print(fruit)