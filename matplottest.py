import matplotlib.pyplot as plt

x = [1,2,3]
y = [4,7,6]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x,y,label='FirstLine')
plt.plot(x2,y2,label='SecondLine')
plt.xlabel('Plot Number')
plt.ylabel('Y')
plt.title('SelfLearningMatplotlib\nCheck it out')
plt.legend()
plt.show()
