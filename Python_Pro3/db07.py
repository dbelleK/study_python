import sqlite3

#변수
con, cur = None, None
data1, data2, data3, data4 = "","","",""
sql=""

con=sqlite3.connect("C:/Users/kkddy/Downloads/sqlite-tools-win32-x86-3380200/sqlite-tools-win32-x86-3380200/soldesk")
cur=con.cursor()

cur.execute("select*from userTable")

print("사용자ID     사용자이름     이메일               출생연도")
print("--------------------------------------------------------")

while(True):
    row=cur.fetchall() #한줄
    if row==None:
        break
    data1=row[0]
    data2=row[1]
    data3=row[2]
    data4=row[3]
    print("%7s %12s %15s %5s" % (data1,data2,data3,data4) )

    sql="insert into userTable values('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)

con.commit()
con.close()
