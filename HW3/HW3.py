import numpy as np
import os
import glob
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.linalg import norm
sns.set()

#Import data with numpy
data = np.loadtxt("data.txt")

#Split data into 100 files and create a directory and save text data to a corresponding directory
splited_data = np.array_split(data, 100)  

def top_hat(x):
    """Top-Hat kernel

    Args:
        x (float)

    Returns:
        integer: 1 or 0
    """
    if abs(x) < 1:
        return 1
    else:
        return 0
    

#vectorize top_hat function
top_hat = np.vectorize(top_hat)

def kde(x, X, dx):
    """kernel density estimation unisng top-hat kernel

    Args:
        x (array)
        X (array): data that want pdf
        dx (float)

    Returns:
        array: pdf of data
    """
    n = len(X)
    s = 0
    for i in X:
        s += top_hat((x - i)/dx)
    return (1/(n*dx))* s


def sigma(p, N, dx):
    """error estimation

    Args:
        p (float): pdf
        N (int): number of data
        dx (foat)

    Returns:
        float: error of pdf
    """
    return np.sqrt(1-p) /(N*dx)
#vectorize sigma
#sigma = np.vectorize(sigma)

def B(x, s):
    """guassian function

    Args:
        x (array)
        s (float): sigma of guassian function

    Returns:
        array
    """
    return np.exp(-x**2/(2*s))

def conv(sig1, sig2):
    """calculate convolution of two signal

    Args:
        sig1 (array): signal 1 that we want be smooth
        sig2 (array): signal 2 

    Returns:
        array: convolve function
    """
    # Pre-allocate correlation array
    conv = (len(sig1) - len(sig2)) * [0]
    # Go through lag components one-by-one
    for l in range(len(conv)):
        for i in range(len(sig2)):
            conv[l] += sig1[l-i+len(sig2)] * sig2[i]

        conv[l] /= len(sig2) # Normalize

    return conv

#parent path 
parent = "/home/mohaddeseh/Documents/Programing/Computational/HW3"
#define x for plot pdf of data
x = np.linspace(-6,6,1000)
#define y for quassian convolution
y = np.linspace(-6,6,200)


for i,d in enumerate(splited_data):
    #change directory to parent path
    os.chdir(parent)
    #creat directory for ith data
    os.mkdir(str(i))
    path = os.path.join(parent, str(i))
    #cahnge directory to ith directory
    os.chdir(path)
    #save ith data to a text file 
    np.savetxt(f"{i}.txt",d)


    DX = [0.1, 0.01, 0.001]
    for n,dx in enumerate(DX):
        #calculate pdf of data
        p = kde(x, d, dx)
        #Normalize p
        p /= norm(p)

        #calculate error of data
        s = sigma(p, len(d), dx)

        #calculate convolution of pdf and guassian func with sigma are 2 and 0.2
        conv1 = conv(p, B(y, 2))  #sigma is 2
        conv2 = conv(p, B(y, 0.2))  #sigma is 0.2
        #Normalize the function
        conv1 = np.array(conv1)/norm(conv1)
        conv2 = np.array(conv2)/norm(conv2)

        #plot
        fig, ax = plt.subplots(figsize=(12,10))
        plt.plot(x, p, label="Simple")
        plt.plot(x[100:900], conv1, label=r"$\sigma = 2$")
        plt.plot(x[100:900], conv2, label=r"$\sigma = 0.2$")

        #choose random index to show errors of some points in pdf
        index = np.random.choice(range(100,900), 20)
        #show errors in plot
        ax.errorbar(x[index], p[index], yerr=s[index], ls="", label=r"$\sigma_m$")
        #add title
        ax.set_title(f"PDF usuing Top-Hat kernel with error for dx = {dx}")
        ax.set_xlabel("x")
        ax.set_ylabel("P(x)")
        plt.legend()
        #save pdf file in ith directory
        plt.savefig(f"PDF_with_dx_{n}")


