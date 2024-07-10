import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Define the data
old_purchases = 50
old_visitors = 1000
old_layout = np.array([1] * old_purchases + [0] * (old_visitors - old_purchases))

new_purchases = 70
new_visitors = 1000
new_layout = np.array([1] * new_purchases + [0] * (new_visitors - new_purchases))

# Perform z-test for proportions
count = np.array([old_purchases, new_purchases])
nobs = np.array([old_visitors, new_visitors])

stat, pval = proportions_ztest(count, nobs, alternative='larger')

# Print the results
print(f"Z-test statistic: {stat:.4f}")
print(f"P-value: {pval:.4f}")

alpha = 0.05
if pval < alpha:
    print("Reject the null hypothesis: The new layout leads to a significantly higher conversion rate.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in conversion rates between the layouts.")
