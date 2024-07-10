import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def calculate_normal_pdf(x, mean, std_dev):
    """
    Calculate the Probability Density Function (PDF) of a normal distribution.

    Parameters:
    - x: The point(s) at which to calculate the PDF.
    - mean: The mean (μ) of the normal distribution.
    - std_dev: The standard deviation (σ) of the normal distribution.

    Returns:
    - pdf_values: The PDF value(s) at point(s) x.
    """
    pdf_values = norm.pdf(x, loc=mean, scale=std_dev)
    return pdf_values

# Example usage:
mean = 0   # Mean of the normal distribution
std_dev = 1   # Standard deviation of the normal distribution

# Generate x values for which to calculate the PDF
x_values = np.linspace(-5, 5, 100)
pdf_values = calculate_normal_pdf(x_values, mean, std_dev)

# Plotting the PDF
plt.figure(figsize=(8, 6))
plt.plot(x_values, pdf_values, label=f'Normal PDF (μ={mean}, σ={std_dev})')
plt.title('Probability Density Function (PDF) of Normal Distribution')
plt.xlabel('x')
plt.ylabel('PDF(x)')
plt.legend()
plt.grid(True)
plt.show()
