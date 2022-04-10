##변수
select, answer, numstr, num1, num2 = 0,0.0,"",0,0

##메인
select = int(input("1. 수식계산기 2. 두 수 사이의 합계 : "))

if select==1 :
    numstr= input("수식을 입력하세요 : ") # 3*87/5
    answer=eval(numstr) # eval : 문자여도 계산가능
    print("%s 결과는 %5.1f 입니다" % (numstr, answer))
elif select==2 :
    num1=int(input("1.시작될 숫자를 입력하세요 : "))
    num2=int(input("2.마지막 숫자를 입력하세요 : "))
    for i in range(num1, num2+1) : #미만으로 나오니까 +1 해주어야한다
        answer = answer+i

    print("%d + ....+ %d 는 %d 입니다" % (num1,num2,answer))
else :
    print("1 또는 2 만 입력하셔야 합니다.")
