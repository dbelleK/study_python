import matplotlib.pyplot as plt #pip install matplotlib

# 2차 함수 정의
# f(x) = x^2
f=lambda x : x**2

x= [x for x in range(-10, 10)]
y= [f(y) for y in range(-10, 10)] #y는 lambda x : x**2인 x의 제곱

print('X축', x)
print('Y축', y)

#그래프
plt.plot(x,y)
plt.show()
