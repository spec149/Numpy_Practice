# -*- coding: utf-8 -*-
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

ReShapeArr = arr.reshape(4,3)
FlatArr = ReShapeArr.reshape(-1)

print(arr)          #This will retunr 1-D array
print(ReShapeArr)   #This will retunr 2-D array
print(FlatArr)      #This will retunr 1-D array
