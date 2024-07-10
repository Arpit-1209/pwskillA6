import A1
import numpy as np

def generate_random_samples(dist, size, **kwargs):
    if dist == "binomial":
        samples = np.random.binomial(kwargs["n"], kwargs["p"], size)
    elif dist == "poisson":
        samples = np.random.poisson(kwargs["lam"], size)
    mean = A1.calculate_mean(samples)
    variance = A1.calculate_variance(samples)
    return samples, mean, variance

samples, mean_binom, var_binom = generate_random_samples("binomial", 1000, n=10, p=0.5)
print("Binomial Distribution - Mean:", mean_binom, "Variance:", var_binom)

samples, mean_poisson, var_poisson = generate_random_samples("poisson", 1000, lam=4)
print("Poisson Distribution - Mean:", mean_poisson, "Variance:", var_poisson)
