import numpy as np
from statsmodels.stats import weightstats as stests

# Define the data
response_times = np.array([4.3, 3.8, 5.1, 4.9, 4.7, 4.2, 5.2, 4.5, 4.6, 4.41])

# Population mean under the null hypothesis
pop_mean = 5

# Perform one-sample z-test for mean
stat, pval = stests.ztest(response_times, value=pop_mean, alternative='smaller')

# Print the results
print(f"Z-test statistic: {stat:.4f}")
print(f"P-value: {pval:.4f}")

alpha = 0.05
if pval < alpha:
    print("Reject the null hypothesis: The average response time is less than 5 minutes.")
else:
    print("Fail to reject the null hypothesis: There is no sufficient evidence that the average response time is less than 5 minutes.")
