#1
import numpy as np
arr_zeros = np.zeros(10,dtype = int)
arr_zeros[5] = 1
print(arr_zeros)
#2
arr_h = np.arange(10,25)
arr_h[::-1]
#3
arr_k = np.array([1,2,0,8,2,0,1,3,0,5,0])
arr_1 = arr_k[arr_k != 0]
print(arr_1)
#4
arr_l = np.append(arr_1,[10,20])
print(arr_1)