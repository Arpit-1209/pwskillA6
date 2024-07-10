import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

def calculate_exponential_cdf(x, scale):
    """
    Calculate the Cumulative Distribution Function (CDF) of an exponential distribution.

    Parameters:
    - x: The point(s) at which to calculate the CDF.
    - scale: The scale parameter (β) of the exponential distribution (1/λ).

    Returns:
    - cdf_values: The CDF value(s) at point(s) x.
    """
    cdf_values = expon.cdf(x, scale=scale)
    return cdf_values

# Example usage:
scale = 1   # Scale parameter (β) of the exponential distribution

# Generate x values for which to calculate the CDF
x_values = np.linspace(0, 5, 100)
cdf_values = calculate_exponential_cdf(x_values, scale)

# Plotting the CDF
plt.figure(figsize=(8, 6))
plt.plot(x_values, cdf_values, label=f'Exponential CDF (β={scale})')
plt.title('Cumulative Distribution Function (CDF) of Exponential Distribution')
plt.xlabel('x')
plt.ylabel('CDF(x)')
plt.legend()
plt.grid(True)
plt.show()
