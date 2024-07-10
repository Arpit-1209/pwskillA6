import numpy as np
import A1
import A1.A1

def gaussian_distribution(mean, std_dev, size):
    samples = np.random.normal(mean, std_dev, size)
    mean_value = A1.calculate_mean(samples)
    variance_value = A1.calculate_variance(samples)
    std_dev_value = A1.calculate_std_dev(samples)
    return samples, mean_value, variance_value, std_dev_value

samples, mean_gauss, var_gauss, std_gauss = gaussian_distribution(0, 1, 1000)
print("Gaussian Distribution - Mean:", mean_gauss, "Variance:", var_gauss, "Standard Deviation:", std_gauss)
