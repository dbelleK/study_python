'''
ss = '아이브짱!'

sslen = len(ss) #5
for i  in range(0 , sslen) :
    print(ss[i] + '$' , end='')
'''
'''
#변수
inStr, outStr="", ""
count, i = 0,0

#메인
inStr = input("문자열을 입력하세요 : ") #아이브
count = len(inStr) #3

for i in range(0, count) : #3번돔 #0 1 2
    outStr += inStr[count - (i+1)] #2 1 0
print("내용을 거꾸로 출력 ==> %s" % outStr)

ss = input("문자열 입력 ==> ")
print("출력 문자열 ==> ", end='')

if ss.startswith('(') == False : #가로가 있으면 또 붙여지진 않는다
    print("(", end='')

print(ss, end='')

if ss.endswith(')') == False :
    print(")", end='')
'''
'''
inStr = "   한글    Python    프로그래밍   "
outStr = ""

#공백제거
for i in range(0, len(inStr)) :
    if inStr[i] != ' ' :
        outStr += inStr[i]

print("원  문자열 ==> " + '[' + inStr + ']')
print("공백 제거, ==> " + '[' + outStr + ']')
print("-------------------------------------")
'''
ss=input("문자열 입력 ==> ")

print("출력 문자열 ==> ", end='')
for i in range(0, len(ss)):
    if ss[i] != 'o':
        print(ss[i], end='')
    else :
        print('$', end='')
