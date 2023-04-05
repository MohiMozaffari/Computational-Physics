import numpy as np
import glob
import os
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def mean(x):
    """mean of data

    Args:
        x (list): list of data

    Returns:
        float: mean
    """
    return (np.sum(x)/len(x))

def var(x):
    """variance of data

    Args:
        x (narray): list of data

    Returns:
        float: variance
    """
    mean = (np.sum(x)/len(x))
    mean2 = (np.sum(x**2)/len(x))
    return (mean2 - mean)

Mu = []
Sigma2 = []
Sigma = []

for foldername in glob.iglob('x*'):
    #go to the directory that contain data
    os.chdir(foldername)
    #load data
    data = np.loadtxt(f'{foldername}.txt')

    #calculate mean, variance, and mean standard deviation of data
    mu = mean(data)
    sigma2 = var(data)
    sigma = np.sqrt(sigma2/len(data))

    #append them to a list for plotting
    Mu.append(mu)
    Sigma2.append(sigma2)
    Sigma.append(sigma)

    #creat a txt file for save mean, variance, and mean standard deviation of data
    file = open(f'{foldername}_mean.txt', 'w')
    #write them in the file
    file.write(f"the mean is {str(mu)}")
    file.write("\n")
    file.write(f"the variance is {str(sigma2)}")
    file.write("\n")
    file.write(f"the mean standard deviation is {str(sigma)}")
    file.close()

    #change the data directory to root directory
    os.chdir("/home/mohaddeseh/Documents/Programing/Computational/HW2/HW2_Q1/")


#plot mean, variance, and mean standard deviation of data

fig, axs = plt.subplots(3, 1, figsize=(12,10))

axs[0].plot(range(100), Mu,".", color = "red")
axs[0].set_xlabel('Label of data')
axs[0].set_ylabel('Mean')

axs[1].plot(range(100), Sigma2, ".", color = "blue")
axs[1].set_xlabel('Label of data')
axs[1].set_ylabel('Variance')

axs[2].plot(range(100), Sigma,".", color = "magenta")
axs[2].set_xlabel('Label of data')
axs[2].set_ylabel('Mean standard deviation')
plt.tight_layout()

plt.savefig("mean_data")