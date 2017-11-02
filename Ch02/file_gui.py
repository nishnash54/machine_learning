import matplotlib.pyplot as plt

xdata = []
ydata = []
data = []
filename = "testDigits/8_0.txt"
with open(filename) as f:
    while True:
        line = f.readline().strip()
        if not line :
            break
        data.append(line)
f.close()

y = 32
for each in data:
    for i in range(len(each)):
        if each[i]=='1':
            xdata.append(i)
            ydata.append(y)
    y -= 1

plt.plot(xdata, ydata, 'ro')
plt.axis([-3, 35, -3, 35])
plt.show()
