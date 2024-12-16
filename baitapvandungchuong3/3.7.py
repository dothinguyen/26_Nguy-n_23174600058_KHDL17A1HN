import numpy as np
#1
np_baseball = np.loadtxt('D:\\baitapvandungchuong3\\baseball_2D.txt', delimiter=',',encoding='utf-8-sig')
print(np_baseball)
#2
print("in gia tri thu 50: ",np_baseball[50])
#3
np_weight = np_baseball[::,:1]
print(np_weight)
#4
print("chiều cao của vận động viên thứ 124: ",np_baseball[124][1:])
#5
np_height = np_baseball[::,1:]
print("chiều cao trung bình là: ",np.mean(np_height))
print("cân nặng trung bình là: ",np.mean(np_weight))
#6
print("em thấy chiều cao của cầu thủ tỉ lệ thuận với cân nặng ")