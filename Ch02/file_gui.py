import matplotlib.pyplot as plt

def retdata(name):

    xdata = []
    ydata = []
    data = []

    filename = name
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

    return xdata, ydata

f, (ax1, ax2, ax3) = plt.subplots(3)
ret1 = retdata("testDigits/5_0.txt")
ax1.plot(ret1[0], ret1[1], 'ro')
ax1.axis([-3, 35, -3, 35])
ret2 = retdata("testDigits/5_2.txt")
ax2.plot(ret2[0], ret2[1], 'bo')
ax2.axis([-3, 35, -3, 35])

lst1 = [(ret1[0][i], ret1[1][i]) for i in range(len(ret1[0]))]
lst2 = [(ret2[0][i], ret2[1][i]) for i in range(len(ret2[0]))]

x = []
y = []
for each in lst1:
    if each in lst2:
        x.append(each[0])
        y.append(each[1])
ax3.plot(x, y, 'go')
ax3.axis([-3, 35, -3, 35])
plt.show()
