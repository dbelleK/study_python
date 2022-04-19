import matplotlib.pyplot as plt;
import numpy as np;
#fig 객체

fig = plt.figure();

#서브 슬롯 생성(2행 1열)

ax1 = fig.add_subplot(1,2,1)    #1행 2열 중 첫번째
ax2 = fig.add_subplot(1,2,2)    #1행 2열 중 첫번째

PI = 3.14159265358979;

t = np.linspace(0.0, 2*PI, 100);
print(t);
#x축
x1 = 5*np.cos(2*t) +2*np.cos(3*t);
x2 = 16*(np.sin(t)**3);
#y축
y1 = 2*np.sin(3*t) - 5*np.sin(2*t);
y2 = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) -np.cos(4*t);
ax1.plot(x1, y1);
ax2.plot(x2, y2, "r");

# ax1.show();
plt.show();
