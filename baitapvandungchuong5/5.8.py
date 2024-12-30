import sqlite3
conn = sqlite3.connect(r'D:\baitapvandungchuong5\data5.4.db')
cursor = conn.cursor()
cursor.execute("""DELETE FROM hocsinh WHERE id =1""")
rows =cursor.execute("SELECT * FROM hocsinh")
print("đã xóa hàng có id =1")
conn.commit()
for row in rows:
    print(row)
conn.close()