import sqlite3 
conn= sqlite3.connect(r'D:\baitapvandungchuong5\data5.4.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM hocsinh")
rows =cursor.fetchall()
print("Danh sách các bản ghi trong bảng 'hocsinh':")
for row in rows:
    print(row)
conn.close()