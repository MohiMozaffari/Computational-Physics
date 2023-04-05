import numpy as np
import matplotlib.pyplot as plt

#Load 5 arbitary data set
data1 = np.loadtxt("/home/mohaddeseh/Documents/Programing/Computational/HW3/89/89.txt")
data2 = np.loadtxt("/home/mohaddeseh/Documents/Programing/Computational/HW3/75/75.txt")
data3 = np.loadtxt("/home/mohaddeseh/Documents/Programing/Computational/HW3/51/51.txt")
data4 = np.loadtxt("/home/mohaddeseh/Documents/Programing/Computational/HW3/33/33.txt")
data5 = np.loadtxt("/home/mohaddeseh/Documents/Programing/Computational/HW3/12/12.txt")

def autocorr(x, t):
    """calculate autocorrelation of data

    Args:
        x (1darray): data set
        t (integer): time delay of data

    Returns:
        float: autocorrelation of data
    """
    n = x.shape[0]
    y = []
    for i in range(n-t):
        y.append(x[i+t])
    x = x[:n-t]
    hist_x = np.histogram(x, bins=100, density=True)[0]
    hist_y = np.histogram(y, bins=100, density=True)[0]
    hist_xy = np.histogram2d(x, y, bins=100, normed=True)[0]
    deltatau = hist_xy - (hist_x*hist_y)
    return np.linalg.norm(deltatau)

#define tau
tau = range(1000)
delta1 , delta2, delta3, delta4, delta5= [], [], [], [], []
for t in tau:
    delta1.append(autocorr(data1, t))
    delta2.append(autocorr(data2, t))
    delta3.append(autocorr(data3, t))
    delta4.append(autocorr(data4, t))
    delta5.append(autocorr(data5, t))


# Plot delta for each set
plt.plot(delta1, label='Set 1', ls="", marker=".")
plt.plot(delta2, label='Set 2', ls="", marker=".")
plt.plot(delta3, label='Set 3', ls="", marker=".")
plt.plot(delta4, label='Set 4', ls="", marker=".")
plt.plot(delta5, label='Set 5', ls="", marker=".")
plt.xlabel('τ')
plt.ylabel('∆(τ)')
plt.legend()
plt.ylim(4.5,6)
plt.savefig("Autocorrelation")