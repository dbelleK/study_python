# 클래스
class Car :
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

## ====================================================================================
#메인
# Car myCar1 = new Car();
myCar1 = Car() #객체생성
myCar1.color="빨간색"
myCar1.speed=0

myCar2 = Car() #객체생성
myCar2.color="파란색"
myCar2.speed=0

myCar3 = Car() #객체생성
myCar3.color="노란색"
myCar3.speed=0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s 이며, 현재속도는 %d km입니다" % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s 이며, 현재속도는 %d km입니다" % (myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print("자동차3의 색상은 %s 이며, 현재속도는 %d km입니다" % (myCar3.color, myCar3.speed))







a='10'
