import matplotlib.pyplot as plt

#fig 객체
fig=plt.figure()

#서브 슬록 생성 (2행 1열)
ax1=fig.add_subplot(2,1,1) #2행중 1열 1행
ax2=fig.add_subplot(2,1,2) #2행중 1열 2행

#x축
x=range(0,100)

#y축 생성1
y=[v*v for v in x]
print('y : ',y)
#y축 생성2
z=[v*v*2 for v in x]
print('z : ',z)

#멀티라인(1행 1열)
ax1.plot(x,y, 'b', z, 'r')

#멀티라인(2행 1열)
ax2.bar(x,y)

plt.show()
