import numpy as np
from scipy.stats import chi2_contingency

# Define the contingency table (observed frequencies)
data = np.array([[50, 30, 20],
                 [30, 40, 30],
                 [20, 30, 40]])

# Perform Chi-Square test for independence
chi2, p_value, dof, expected = chi2_contingency(data)

# Print the results
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("\nReject the null hypothesis: There is a significant difference between job performance levels before and after the training.")
else:
    print("\nFail to reject the null hypothesis: There is no significant difference between job performance levels before and after the training.")
