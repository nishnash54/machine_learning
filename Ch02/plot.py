import matplotlib
import matplotlib.pyplot as plt
import parser
import numpy as np

datingDataMat, datingLabels = parser.file2matrix('datingTestSet.txt')
print(datingDataMat[:5], datingLabels[:5])
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*np.array(datingLabels), 15.0*np.array(datingLabels))
plt.show()
