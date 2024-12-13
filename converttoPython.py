from scipy.io import loadmat
import h5py
import numpy as np 

Hand_Close = 'Hand_Close-1.mat'
data = loadmat(Hand_Close)


# Print variable names and data
print(data.keys())
print(data['__header__'], data['__version__'], data['__globals__'], data['value'])



