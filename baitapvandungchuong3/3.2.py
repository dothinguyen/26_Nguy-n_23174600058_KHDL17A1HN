#1
import numpy as np
arr = np.arange(10)
print(arr)
print(arr.dtype)
print(arr.shape)
#2
arr_odd = arr[arr %2 !=0]
arr_event = arr[arr%2 ==0]
print("arr_odd: ",arr_odd)
print("arr_event",arr_event)
#3
arr_update_1 = np.where(arr %2 != 0, 100,arr)
print(arr_update_1)