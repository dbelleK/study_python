import random

num1 = random.random()
print(num1)

# uniform() 함수의 두번째 인자값은 난수 생성범위에 들어가지 않음
num2=random.uniform(1,2) #2미만
print(num2)

#randint() 두번째 인자값은 난수 생성범위에 들어감
num3=random.randint(1,5) #5포함
print(num3)
