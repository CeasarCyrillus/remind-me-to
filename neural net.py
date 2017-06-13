import numpy as np
from random import uniform
# sigmoid function
def nonlin(x,deriv=False):
    if deriv:
        return x*(1-x)
    return 1/(1+np.exp(-x))
def array_string(arr):
	string = ""
	for elem in arr:
		string += str(round(float(elem)))
	return string
# input dataset
"""
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
    
# output dataset            
y = np.array([[0,0,0,0]]).T
"""
#OR trainging out/in
X = np.array([[0, 0], #False and False
			  [1, 0], #True and False
			  [1, 1], #True and True
			  [0, 1]]) #False and True
y = np.array([[0, 0, 1, 0]]).T
desired = y
# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((2,1)) - 1
iterations = 0
for i in range(10000):
	iterations += 1
    # forward propagation
	l0 = X
	l1 = nonlin(np.dot(l0,syn0))
	# how much did we miss?
	l1_error = y - l1
	# multiply how much we missed by the 
	# slope of the sigmoid at the values in l1
	l1_delta = l1_error * nonlin(l1,True)

	# update weights
	syn0 += np.dot(l0.T,l1_delta)
print("Output After Training:")
print(l1)
print("Desired Output:")
print(desired)