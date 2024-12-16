import pandas as pd
import numpy as np


#df.to_csv('chuong3/euro2012.csv', index=False)
euro = pd.read_csv('D:\\baitapvandungchuong3\\euro2012.csv')
print("giá trị cột goal là: ")
#1
print(euro['Goals']) 
#2
nums_team = euro['Team'].nunique()
print(nums_team)
#3
print("thông tin euro2012 là:\n ", euro)
#4
discipline = euro.drop(['Goals','Shooting Accuracy'],axis = 1)
discipline = pd.DataFrame(discipline)
print(discipline)
#5
dis_sort_yellow = discipline.sort_values(by='Yellow Cards')[::-1]
print(dis_sort_yellow)
dis_sort_red = discipline.sort_values(by='Red Cards')[::-1]
print(dis_sort_red)
#6
yellows = dis_sort_red['Yellow Cards']
print("trung bình Yellows Cảd la: ",np.mean(yellows))
goals = euro[euro['Goals'] >6]
print("đội ghi hơn 6 bàn thắng là: ",goals)
#7
start_G= euro[euro['Team'].str.startswith('G')]
print("Đội bắt đầu bằng chứ G là: \n",start_G)
#8
print("7 dòng đồng của euro12 là: \n",euro.head(7))
#9
print("tất cả các cột trừ 3 cột cuối là: \n",euro.iloc[:,:-3])
#10
print("tất cả các cột là: ",euro)
#11
team_shoot =euro[['Team','Shooting Accuracy']]
team_shoot = team_shoot[team_shoot['Team'].isin(['England','Italy','Russia'])]
print("câu 11: \n",team_shoot)