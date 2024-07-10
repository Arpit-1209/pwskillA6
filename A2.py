import random, math
int_list2 = [random.randint(200, 300) for _ in range(500)]
print(int_list2)

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Frequency & Gaussian distribution
sns.histplot(int_list2, kde=False, stat="density")
sns.kdeplot(int_list2)
plt.title("Frequency & Gaussian Distribution")
plt.show()

# Frequency smoothened KDE plot
sns.histplot(int_list2, kde=True, stat="density")
plt.title("Frequency Smoothened KDE Plot")
plt.show()

# Gaussian distribution & smoothened KDE plot
sns.kdeplot(int_list2)
sns.kdeplot(np.random.normal(np.mean(int_list2), np.std(int_list2), 1000), linestyle="--")
plt.title("Gaussian Distribution & Smoothened KDE Plot")
plt.show()

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_range(numbers):
    return max(numbers) - min(numbers)

range_value = calculate_range(int_list2)
print("Range:", range_value)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std_dev(numbers):
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

variance_value = calculate_variance(int_list2)
std_dev_value = calculate_std_dev(int_list2)
print("Variance:", variance_value)
print("Standard Deviation:", std_dev_value)

def calculate_iqr(numbers):
    numbers.sort()
    q1 = np.percentile(numbers, 25)
    q3 = np.percentile(numbers, 75)
    return q3 - q1

iqr_value = calculate_iqr(int_list2)
print("Interquartile Range (IQR):", iqr_value)

def coefficient_of_variation(numbers):
    return (calculate_std_dev(numbers) / calculate_mean(numbers)) * 100

cv_value = coefficient_of_variation(int_list2)
print("Coefficient of Variation:", cv_value)

def mean_absolute_deviation(numbers):
    mean = calculate_mean(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

mad_value = mean_absolute_deviation(int_list2)
print("Mean Absolute Deviation (MAD):", mad_value)

def quartile_deviation(numbers):
    numbers.sort()
    q1 = np.percentile(numbers, 25)
    q3 = np.percentile(numbers, 75)
    return (q3 - q1) / 2

qd_value = quartile_deviation(int_list2)
print("Quartile Deviation:", qd_value)

def range_based_coefficient_of_dispersion(numbers):
    return (calculate_range(numbers) / (max(numbers) + min(numbers))) * 100

rbcd_value = range_based_coefficient_of_dispersion(int_list2)
print("Range-Based Coefficient of Dispersion:", rbcd_value)


