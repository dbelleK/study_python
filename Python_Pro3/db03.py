import sqlite3

con=sqlite3.connect("C:/Users/kkddy/Downloads/sqlite-tools-win32-x86-3380200/sqlite-tools-win32-x86-3380200/soldesk")
cur=con.cursor()

cur.execute("select * from T_STU_INFO")

rows=cur.fetchall()

for r in rows:
    print('ST_name:{0}, ST_code:{1}, ST_MAJ:{2}, ST_GRA:{3}, ST_PHO:{4}' .format(r[0],r[1],r[2],r[3],r[4]))

cur.close()
con.close()
