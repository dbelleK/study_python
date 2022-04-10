parking=[]
top, carName, outCar = 0, "A", ""
select = 9

#메인
while(select !=3):
    select = int(input("<1>입차 <2>출차 <3>종료 :"))

    if(select ==1):
        if(top >=5):
            print("만차입니다")
        else:
            parking.append(carName) #추가
            print("%s 자동차 들어감. 주차장 상태 ==> %s" % (parking[top],parking))
            top += 1 #입차
            carName=chr(ord(carName)+1) #ord:ASCII코드로 변경 / chr:문자로 변경

    elif(select ==2):
            if(top<=0):
                print("출차할 차가 없습니다.")
            else :
                outCar=parking.pop() #리스트에서 출력
                print("%s 자동차 나감. 주차장 상태 ==> %s" % (outCar, parking))
                top -=1 #출차
                carName=chr(ord(carName)-1) #ord:ASCII코드로 변경 / chr:문자로 변경
    elif(select ==3):
        break
    else :
        print("잘못 입력하셨습니다. 다시 입력하세요")

print("현재 주차장에 %d대가 있습니다" % top)
print("주차장 영업을 종료합니다")
