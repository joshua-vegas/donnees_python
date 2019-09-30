import numpy as np
>>> a = np.array([1,2,3])
>>> a.ndim
1
>>> a.shape
(3,)
>>> a.dtype
dtype('int32')
>>> np.zeros((2,3))
array([[0., 0., 0.],
       [0., 0., 0.]])
>>> np.ones((5,6))
array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.]])
>>> np.arrange(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'numpy' has no attribute 'arrange'
>>> np.arange(10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.arange(2, 10, dtype = np.float)
array([2., 3., 4., 5., 6., 7., 8., 9.])
>>> np.arange(2, 15, dtype = np.float)
array([ 2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11., 12., 13., 14.])
>>> np.arange(2, 3, 0.2)
array([2. , 2.2, 2.4, 2.6, 2.8])
>>> np.linspace(1.,4.,6)
array([1. , 1.6, 2.2, 2.8, 3.4, 4. ])
>>> np.random.random((2,3))
array([[0.63786456, 0.64676945, 0.74984967],
       [0.79321509, 0.56252727, 0.82286947]])
>>> a = np.arange(3)
>>> a
array([0, 1, 2])
>>> print(a)
[0 1 2]
>>> b = np.arange(9).reshape(3,3)
>>> b
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> print(b)
[[0 1 2]
 [3 4 5]
 [6 7 8]]
>>> c = np.arange(8).reshape(2,2,2)
>>> c
array([[[0, 1],
        [2, 3]],

       [[4, 5],
        [6, 7]]])
>>> print(c)
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
>>> x = np.arange(10)
>>> x[2,5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: too many indices for array
>>> x[2:5]
array([2, 3, 4])
>>> x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> x[2:5]
array([2, 3, 4])
>>> x[:-5]
array([0, 1, 2, 3, 4])
>>> x[1:7:2]
array([1, 3, 5])
>>> y = np.arange(35).reshape(5,7)
>>> y
array([[ 0,  1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12, 13],
       [14, 15, 16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25, 26, 27],
       [28, 29, 30, 31, 32, 33, 34]])
>>> y[1:5:2, ::3]
array([[ 7, 10, 13],
       [21, 24, 27]])


>>> import pandas as pd
>>> population_dict = {"California": 38332521, "Texas": 26448193, "New York": 19651127, "Florida": 19552860, "Illinois": 12882135}
>>> area_dict = {"California": 423967, "Texas": 695662, "New York": 141297, "Florida": 170312, "Illinois": 149995}
>>> population_ = pd.Series(population_dict)
>>> area = pd.Series(area_dict)
>>> print(population_)
California    38332521
Texas         26448193
New York      19651127
Florida       19552860
Illinois      12882135
dtype: int64
>>> print(population["California" : "Texas"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'population' is not defined
>>> print(population_["California" : "Texas"])
California    38332521
Texas         26448193
dtype: int64


>>> print(population_dict["California" : "Texas"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'slice'
>>> s = Series([1,2,5,7], index = ['a', 'b', 'c', 'd'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Series' is not defined
>>> s = pandas.Series([1,2,5,7], index = ['a', 'b', 'c', 'd'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pandas' is not defined
>>> s = pd.Series([1,2,5,7], index = ['a', 'b', 'c', 'd'])
>>> s
a    1
b    2
c    5
d    7
dtype: int64
>>> s.index
Index(['a', 'b', 'c', 'd'], dtype='object')
>>> s.reindex(['c', 'b', 'a', 'e'])
c    5.0
b    2.0
a    1.0
e    NaN
dtype: float64
>>> s.descibe()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\GK\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'descibe'
>>> s.describe()
count    4.000000
mean     3.750000
std      2.753785
min      1.000000
25%      1.750000
50%      3.500000
75%      5.500000
max      7.000000
dtype: float64
