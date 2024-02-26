# -*- coding: utf-8 -*-
"""Numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1APp3bWluyXGkD3-lPD7Jxrg4wYfNSIix
"""

import numpy as np
# creating arrays
arr=np.array([1,2,3,4,5])
print(arr)

import numpy as np
zeros_arr=np.zeros((3,3),dtype=int)
print(zeros_arr)

zeros_arr=np.zeros((3,3),dtype=int)
print(zeros_arr)

ones_arr=np.ones((2,2),dtype=int)
print(ones_arr)

#array manipulation
arr=np.array([1,2,3,4,5])
reshaped_arr=arr.reshape(5,1)
print(reshaped_arr)

sliced_arr=arr[2:4]
print (sliced_arr)

a=np.array([1,2,3,4,5,6,7,8])
b=a.T
print(b)

b=np.split(a,4)
print(b)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=np.dot(a,b)
print(c)
d=np.linalg.eig(c)
print(d)

data=np.loadtxt("/content/drive/MyDrive/DATASET/DAP.txt",dtype=int)
d=np.savetxt("/content/date.txt",data)
print(d)
print(data)

import numpy as np
arange_arr=np.arange(0,1000,5)
print(arange_arr)
c=np.savetxt("/content/date.txt",arange_arr)

import numpy as np
a=np.random.rand()
print(a)
b=np.random.randint(0,10)
print(b)

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(type(a))
print(a.ndim)
print(a.shape)

a=np.linspace(0.8,2,5)
print(a)

import numpy as np
arange_arr=np.arange(24).reshape(3,2,4)
print(arange_arr)

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a*b)
print(a@b)
c=np.dot(a,b)

from numpy import random
a=np.ones((2,3),dtype=int)
print(a.sum(axis=1))
a=np.floor(np.random.random((2,12)))
print(a)
c=np.random.random((2,12))
c1=np.random.random((2,2))
print(c)
print(c1)

from numpy import random
a=np.ones((2,3),dtype=int)
print(a)
print(a.sum())
print(a.sum(axis=1))
print(a.sum(axis=0))

from numpy import random
a=np.array([2,3,4,5,6,7])
b=np.array([8,9,10,11,12,13])
a.resize(2,3)
b.resize(2,3)
print(np.vstack((a,b)))
print(np.hstack((a,b)))

from numpy import random
a=np.arange(30).reshape(2,3,5)
print(a)
print(np.dstack(a))

"""no.of rows become groups,no.of columns become rows,groups become columns

"""

import numpy as np
a1= np.full((2,2),3)
print(a1)
print(a1.itemsize)

import numpy as np
a1=np.eye(4)
print(a1)

import numpy as np
x=[1,2,3]
a=np.asarray(x)
print(a)

import numpy as np
x=np.array([1,4,0],float)
y=np.array([2,2,1],float)
print(np.inner(x,y))
print(np.outer(x,y))
print(np.cross(x,y))

import numpy as np
a=np.array([2,3,4,5,6,])
b=np.array([8,9,10,11,12,])
print(np.true_divide(a,b))

import numpy as np
a=np.array([1,1,2,2,3,3,4,4])
print(np.unique(a))

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.union1d(a,b))

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[1,3],[7,8]])
print(np.union1d(a,b))
print(np.intersect1d(a,b))

import numpy as np
a=([1.2,2.6,3.3,4.5,6.6])
print(np.rint(a))

a=np.array([[1,2],[3,4]])
b=np.array([[1,3],[7,8]])
print(np.setdiff1d(a,b))

a=8,
b=6,
c=np.hypot(a,b)
print(c)
print(np.sin(0))

a=np.array([10,20,30,40,50])
b=np.array([20,21,2,20,25])
print(np.divmod(a,b))

a=np.array([10,20,30,40,50])
b=np.array([20,21,2,20,25])
print(np.divide(a,b))

a=np.array([10,20,30,40,50])
b=np.array([20,21,2,20,25])
print(np.multiply(a,b))

from numpy import random
x=random.normal(size=(2,3))
print(x)

from numpy import random
x=random.normal(loc=(1),scale=(2),size=(2,3))
print(x)

"""loc denotes mean value,scale denotes standard deviation

"""

x=random.binomial(n=12,p=0.5,size=10)
y=random.poisson(lam=2,size=10)
print(x)
print(y)
c=random.choice([1,3,6,23,5])
print(c)
d=random.choice([3,5],p=[0.5,0.5],size=(3,5))
print(d)