import matplotlib.pyplot as plt

#리스트 범위(x축)
x=range(0,256)
#리스트 범위(y축)
'''
y=[]
for v in x:
    y.append(v*v)
'''
y=[v*v for v in x]

#출력
#print(y)

#차트 설정
#plt.plot(x,y)
plt.plot(x,y,'ro')
plt.show()
