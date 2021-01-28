# -*- coding: utf-8 -*-
import numpy as np

arr = np.array([1,2,3,4], ndmin = 5)
arrSame = np.array([[[[[1,2,3,4]]]]])

print(arr)
print(arrSame) #arr and arrSame will return same values

print(arr.shape)
print(arrSame.shape)
