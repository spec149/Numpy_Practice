# -*- coding: utf-8 -*-
import numpy as np

arr = np.array([1,2,3,4,5,6,7])

def copyArr():
    x = arr.copy()
    arr[0] = 42
    return arr, x

def viewArr():
    y = arr.view()
    arr[0] = 42
    return arr, y

print(copyArr()) # Arr and x should differ
print(viewArr()) # Arr and x should not differ
