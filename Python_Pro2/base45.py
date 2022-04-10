import matplotlib.pyplot as plt #pip install matplotlib

x=[a for a in range(0,11)]
y=list(range(0,11))

print('x축', x)
print('y축', y)

#출력
plt.plot(x,y)
plt.show()
