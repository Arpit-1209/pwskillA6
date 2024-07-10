import numpy as np
from scipy.stats import f_oneway

# Define the data
standard_scores = np.array([80, 85, 90, 78, 88, 82, 92, 78, 85, 87])
premium_scores = np.array([90, 92, 88, 92, 95, 91, 96, 93, 89, 93])
deluxe_scores = np.array([95, 98, 92, 97, 96, 94, 98, 97, 92, 99])

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(standard_scores, premium_scores, deluxe_scores)

# Print the results
print(f"One-way ANOVA")
print(f"F-statistic: {f_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("\nReject the null hypothesis: There is a significant difference in customer satisfaction scores among the three product versions.")
else:
    print("\nFail to reject the null hypothesis: There is no significant difference in customer satisfaction scores among the three product versions.")
