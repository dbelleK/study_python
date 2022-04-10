## 변수 선언 부분
inStr, outStr="", ""
ch = ""
count, i = 0,0

# 메인코드
inStr=input("문자열을 입력하세요 : ")
count=len(inStr)

for i in range(0,count):
    ch=inStr[i] #SolDesk
    if(ord(ch) >= ord("A") and ord(ch) <= ord("Z")): #대문자면
        newCh=ch.lower() #소문자로 바꿈
    elif(ord(ch) >= ord("a") and ord(ch) <= ord("z")): #소문자면
        newCh=ch.upper() #대문자로바꿈
    else:
        newCh=ch
    outStr += newCh

print("대소문자 변환 : %s" % outStr)
