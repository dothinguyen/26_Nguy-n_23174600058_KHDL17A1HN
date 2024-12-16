#1
import numpy as np 
arr_a = [1,2,3,2,3,4,3,4,5,6]
arr_b = [7,2,10,2,7,4,9,4,9,8]
arr_c = []
for i in arr_a:
    if i in arr_b and i not in arr_c:
            arr_c.append(i)
print(arr_c)
#2
arr_d  = []
for i in arr_a:
    if i not in arr_b and i not in arr_d:
        arr_d.append(i)

print(arr_d)
#3
arr_e = np.array([2,6,1,9,10,3,27,8,6,25,16])
arr_f = []
for i in arr_e:
    if i>4 and i<11:
        arr_f.append(i)
arr_f = np.array(arr_f)
print(arr_f)