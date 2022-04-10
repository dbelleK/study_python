def func1():
    a=10
    print("func1()에서 a의 값 %d" % a)
    print("==============================")

def func2():
    print("func2()에서 a의 값 %d" % a)
    print("==============================")

a=20 #전역변수 (func2를 부르기 위한 전역변수)

#메인
func1()
func2()
