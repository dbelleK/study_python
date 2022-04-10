'''
hap=0
a,b=0,0

while True :
    a = int(input("더할 첫 번째 수 입력 : "))
    b = int(input("더할 두 번째 수 입력 : "))
    hap=a+b
    print("%d + %d = %d" % (a, b, hap))
'''

ch=0
a,b=0,0

while True :
    a = int(input("더할 첫 번째 수 입력(종료시 0입력) : "))
    if a==0:
        break
    b = int(input("더할 두 번째 수 입력 : "))
    ch=input("연산자를 입력하세요 : ")

    if(ch=="+"):
        print("%d + %d = %d입니다" % (a,b,a+b))
    elif(ch=="-"):
        print("%d - %d = %d입니다" % (a,b,a-b))
    elif(ch=="*"):
        print("%d * %d = %d입니다" % (a,b,a*b))
    elif(ch=="/"):
        print("%d / %d = %d입니다" % (a,b,a/b))
    elif(ch=="%"):
        print("%d %% %d = %d입니다" % (a,b,a%b))
    elif(ch=="//"): #몫만
        print("%d // %d = %d입니다" % (a,b,a//b))
    elif(ch=="**"): #제곱근
        print("%d ** %d = %d입니다" % (a,b,a**b))
    else:
        print("연산자를 잘못 입력하셨습니다.")

print("프로그램이 종료됩니다.")
