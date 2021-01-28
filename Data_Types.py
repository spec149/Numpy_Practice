# -*- coding: utf-8 -*-
import numpy as np

arr = np.array([1.1, 0, 3.1])

narr = arr.astype(bool) #changes data type to boolean

print(narr)         #Returns [True False True]
print(narr.dtype)   #Returns bool
