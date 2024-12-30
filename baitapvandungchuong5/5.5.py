import sqlite3
conn = sqlite3.connect(r'D:\baitapvandungchuong5\data5.4.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS hocsinh (
               id INTEGER PRIMARY KEY,
               'Name' TEXT,
               'Tuoi' INTEGER)""")

cursor.execute("""INSERT INTO hocsinh ('Name','Tuoi') VALUES
               ('nguyen',20),('ly',19)""")
conn.commit()

conn.close()