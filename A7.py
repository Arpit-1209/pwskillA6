import seaborn as sns
import pandas as pd
from scipy.stats import skew, pearsonr

# Load the tips dataset
tips = sns.load_dataset('tips')

# Display the first few rows to understand the structure
print(tips.head())

# Function to calculate skewness
def calculate_skewness(data):
    return skew(data)

# Calculate skewness for 'total_bill' and 'tip'
skew_total_bill = calculate_skewness(tips['total_bill'])
skew_tip = calculate_skewness(tips['tip'])

print(f"Skewness of 'total_bill': {skew_total_bill}")
print(f"Skewness of 'tip': {skew_tip}")

# Determine skewness type
def skewness_type(skew_value):
    if skew_value > 0:
        return "Positive skewness"
    elif skew_value < 0:
        return "Negative skewness"
    else:
        return "Approximately symmetric"

print(f"Skewness type of 'total_bill': {skewness_type(skew_total_bill)}")
print(f"Skewness type of 'tip': {skewness_type(skew_tip)}")

# Function to calculate covariance between two columns
def calculate_covariance(data, col1, col2):
    return data[col1].cov(data[col2])

covariance_total_bill_tip = calculate_covariance(tips, 'total_bill', 'tip')
print(f"Covariance between 'total_bill' and 'tip': {covariance_total_bill_tip}")

# Function to calculate Pearson correlation coefficient
def calculate_correlation(data, col1, col2):
    return data[col1].corr(data[col2])

correlation_total_bill_tip = calculate_correlation(tips, 'total_bill', 'tip')
print(f"Pearson correlation coefficient between 'total_bill' and 'tip': {correlation_total_bill_tip}")

import matplotlib.pyplot as plt

# Scatter plot to visualize correlation
def visualize_correlation(data, col1, col2):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=col1, y=col2, data=data)
    plt.title(f'Scatter plot of {col1} vs {col2}')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()

# Visualize correlation between 'total_bill' and 'tip'
visualize_correlation(tips, 'total_bill', 'tip')


