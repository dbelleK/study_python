import sqlite3

con=sqlite3.connect("C:/Users/kkddy/Downloads/sqlite-tools-win32-x86-3380200/sqlite-tools-win32-x86-3380200/soldesk")
cur=con.cursor()

cur.execute("drop table T_STU_INFO ")
cur.execute("create table T_STU_INFO(ST_name char(32), ST_code char(32), ST_MAJ char(32), ST_GRA char(32), ST_PHO char(32))")

cur.close()
con.close()
