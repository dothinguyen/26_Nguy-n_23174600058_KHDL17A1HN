import numpy as np
#1
arr = np.full((3,3),True)
print(arr)
print()
#2
arr_1D = np.array([0,1,2,3,4,5,6,7,8])
arr_2D = np.reshape(arr_1D,(3,3))
arr_2D = arr_2D[:,::-1]
print(arr_2D)
print()
#3
arr_2D[:2] = arr_2D[:2][::-1]
print(arr_2D)
print()
#4
arr_2D= arr_2D[::-1]
print(arr_2D)
print()
#5
arr_2D = arr_2D[:,::-1]
print(arr_2D)
print()
#6
arr_2D_null= np.array([[1,2,3],[np.nan,5,6],[7,np.nan,9],[4,5,6]])
ktra_rong = np.isnan(arr_2D_null)
print(ktra_rong)
print()
#7
arr_2D_null[np.isnan(arr_2D_null)] =0
print(arr_2D_null)