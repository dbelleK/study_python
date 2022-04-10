import sqlite3

#변수
con, cur = None, None
data1, data2, data3, data4 = "","","",""
sql=""

con=sqlite3.connect("C:/Users/kkddy/Downloads/sqlite-tools-win32-x86-3380200/sqlite-tools-win32-x86-3380200/soldesk")
cur=con.cursor()

while(True):
    data1=input("사용자 ID ==>")
    if data1=="": #연도에 엔터치면 break

        break
    data2=input("사용자 이름 ==>")
    data3=input("사용자 이메일 ==>")
    data4=input("사용자 출생연도 ==>")
    sql="insert into userTable values('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)

con.commit()
con.close()
