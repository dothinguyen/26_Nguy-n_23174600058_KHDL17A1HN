import numpy as np
#1
np_position = np.loadtxt('D:\\baitapvandungchuong3\\positions.txt',dtype=str, delimiter=',',encoding='utf-8-sig')
np_heights = np.loadtxt('D:\\baitapvandungchuong3\\heights.txt',dtype=float, delimiter=',',encoding='utf-8-sig')
position = np.reshape(np_position,(-1,1))
heights = np.reshape(np_heights,(-1,1))
#2
arr = np.hstack((position,heights))
mask = arr[:,0] == "GK"
arr_gk = arr[mask] 
heights_gk = arr_gk[:,1].astype(float)
print("chiều cao trung bình của GK là: ",np.mean(heights_gk))
#3
mask1 = arr[:,0] != "GK"
arr_else_gk= arr[mask1]
heights_else_gk= arr[:,1].astype(float)
print("chiều cao trung bình của những vị trí khác là: ",np.mean(heights_else_gk))
#4
structured_dtype = np.dtype([('position', 'U5'), ('height', 'f4')])
players = np.array([(row[0], float(row[1])) for row in arr], dtype=structured_dtype)
print(players)
#5
sort_players = np.sort(players, order = 'height')[::-1]
max_height = np.argmax(sort_players['height'])
min_height = np.argmin(sort_players['height'])
print("vị trí có chiều cao cao nhất là: ",max_height)
print("vị trí có chiều cao thấp nhất là: ",min_height)