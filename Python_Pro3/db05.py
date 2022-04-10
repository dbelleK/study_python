import sqlite3

con=sqlite3.connect("C:/Users/kkddy/Downloads/sqlite-tools-win32-x86-3380200/sqlite-tools-win32-x86-3380200/soldesk")
cur=con.cursor()

#테이블생성
cur.execute("drop table userTable")
cur.execute("create table userTable(id char(4), userName char(20), email char(20), birthYear int(15))")

#입력
cur.execute("insert into userTable(id, userName, email, birthYear) values('1833','김도연','kkddy@naver.com','991206')")
cur.execute("insert into userTable(id, userName, email, birthYear) values('1834','김도연','kkddy@naver.com','991206')")

#삭제
cur.execute("delete from userTable where id='1833'")

#검색
cur.execute("select*from userTable")
rows=cur.fetchall()

for r in rows:
    print('{0},{1},{2},{3}'.format(r[0],r[1],r[2],r[3]))


cur.close()
con.close()
