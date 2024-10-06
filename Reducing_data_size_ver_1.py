import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
import glob



def cut_out_no_signal(X, Y):
    treshold = 0.02 * max(Y)
    print(treshold)
    i = 0
    X, Y = list(X), list(Y)
    while i<len(X):
        if abs(Y[i])<treshold:
            del Y[i]
            del X[i]
        else:
            i += 1
    X, Y = np.array(X), np.array(Y)
    return X, Y



path = os.getcwd()
dd = "\S12_GradeB"

files = os.listdir(path+dd)
data = pd.read_csv(path+dd+'\\'+files[0])
data = np.array(data)
data = data.transpose()
X, Y = data[1], data[2]

L0 = len(X)
# plt.plot(X, Y, '-k', linewidth = 1)
X, Y = cut_out_no_signal(X, Y)

L = len(X)
plt.plot(X, Y, '-b', linewidth = 1)
# print(L0, L, (L0-L)/L0)

fig = plt.figure(1)
fig.set_size_inches(16, 9)
plt.xlabel('Relative time, s', fontsize = 16)
plt.ylabel('Measurements, m/s', fontsize = 16)
matplotlib.rc('xtick', labelsize = 16)
matplotlib.rc('ytick', labelsize = 16)
plt.title('Number of data points = '+str(L0), fontsize = 20)
plt.tight_layout()