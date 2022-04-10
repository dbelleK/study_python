import sqlite3

#변수
con, cur = None, None
data1, data2, data3, data4 = "","","",""
sql=""

con=sqlite3.connect("C:/Users/kkddy/Downloads/sqlite-tools-win32-x86-3380200/sqlite-tools-win32-x86-3380200/soldesk")
cur=con.cursor()

ch=int(input("<입력>:1, <출력>:2를 입력하세요 : "))

if ch==1 :



elif ch==2:


con.commit()
con.close()
