# Open terminal and type in "pip install numpy" initially
# Then, in python, type command: "import numpy as np"
import numpy as np
a = np.array([2, 3, 4])        # create a numpy array by passing a list
b = np.arange(1, 14, 2)        # range from 1 to 14 in a step of 2
c = np.linspace(1, 12, 6)      # linear spacing between 1.0 to 12.0 six times
d = c.reshape(3,2)             # reshapes variable, but does not overwrite orginal variable
print(d.size)                  # scalar value
print(d.shape)                 # rows and cols of the array
print(d.dtype)                 # data type = float64 (numpy data default type)
print(d.itemsize)              # how much memory each element of array takes up in bytes (8 in this case)
e = np.array([(1.5, 2, 3, 4.25), (4, 5, 6, 7)])
print(e)
test_each_element = e >= 4.1
mult_each_element_in_array = e * 1.5
# Or even more efficiency, use the "variable *= number""
# Performs mathematical operations on each element in an array without needing a for loop
e *= 100
f = np.pi
import math
print(math.pi * f ** 2)
print(d)
print(e)
print(f)
print(test_each_element)       # note that this is displaying the test on i before i was changed via i *= 5
print(mult_each_element_in_array)
# Create an empty array full of zeros
zeros_array = np.zeros((3,7))  # These are all default float64 values
ones_array = np.ones((2,3))
ones_row = np.ones(4)
A = np.array([2,3,4], dtype=np.int16)   # int16 uses up less memory
print(A.dtype)
print(A.itemsize)
B = np.random.random((4,6))    # random values from 0 to 1
print(B)
np.set_printoptions(precision=2, suppress=True)   # 2 sig.digits, but don't want scientific notation
print(B)
C = np.random.randint(0,10,12) # random integers from 0 to 10 inclusive, with 12 elements
print(C)
print(B.sum())
print(C.sum())
print(C.min())
print(C.max())
print(C.mean())
print(C.var())
print(C.std())
D = np.random.randint(1,10,6)
print(D)
D = D.reshape(3,2)
print(D)
print(D.sum(axis=1))           # sum of horizontal axis (rows)
print(D.sum(axis=0))           # sum of vertical axis (cols)
# Works for any other math functions: min, max, mean, var, std, etc.
print(mult_each_element_in_array)
print(mult_each_element_in_array.std(axis=1))
print(mult_each_element_in_array.std(axis=0))
E = np.arange(8)
print(E)
np.random.shuffle(E)           # don't print this or assign it to a variable (e.g. E = )
# it's an in-place shuffle like sort function
print(E)
print(np.random.choice(E))
print(np.random.choice(E))
print(np.random.choice(E))
print(np.random.random_integers(14,21,2))
