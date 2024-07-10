import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def calculate_poisson_pmf(k, mu):
    """
    Calculate the Probability Mass Function (PMF) of a Poisson distribution.

    Parameters:
    - k: The point(s) at which to calculate the PMF (can be a scalar or an array-like).
    - mu: The mean (λ) of the Poisson distribution.

    Returns:
    - pmf_values: The PMF value(s) at point(s) k.
    """
    pmf_values = poisson.pmf(k, mu)
    return pmf_values

# Example usage:
mu = 3   # Mean (λ) of the Poisson distribution

# Generate k values for which to calculate the PMF
k_values = np.arange(0, 10)
pmf_values = calculate_poisson_pmf(k_values, mu)

# Plotting the PMF
plt.figure(figsize=(8, 6))
plt.stem(k_values, pmf_values, linefmt='b-', markerfmt='bo', basefmt=' ', label=f'Poisson PMF (λ={mu})')
plt.title('Probability Mass Function (PMF) of Poisson Distribution')
plt.xlabel('k')
plt.ylabel('PMF(k)')
plt.legend()
plt.grid(True)
plt.show()
