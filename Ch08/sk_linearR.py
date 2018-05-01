import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":

    data = []
    file = open('ex0.txt')
    for line in file.readlines():
        data.append(map(float, line.strip().split()))

    data = np.array(data)

    lr = LinearRegression()
    lr.fit(data[:, 1].reshape(-1, 1), data[:, 2])

    pre = lr.predict(data[:, 1].reshape(-1, 1))

    res = lr.score(data[:, 1].reshape(-1, 1), data[:, 2])
    print("Result: %s" % res)

    plt.scatter(data[:, 1], data[:, 2], color='red', alpha=0.20)
    plt.scatter(data[:, 1], pre, color='green', alpha=0.20)
    plt.show()
