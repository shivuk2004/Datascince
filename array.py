import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
#deep copy
arr1=arr.copy()
arr1[0]=6
print(arr)
print(id(arr))
print(id(arr1))











            
