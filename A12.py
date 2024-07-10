import numpy as np
from statsmodels.stats import weightstats as stests

# Define the data
before_program = np.array([75, 80, 85, 70, 90, 78, 92, 88, 82, 87])
after_program = np.array([80, 85, 90, 80, 92, 80, 95, 90, 85, 88])

# Perform paired z-test for means
stat, pval = stests.ztest(before_program, after_program)

# Print the results
print(f"Z-test statistic: {stat:.4f}")
print(f"P-value: {pval:.4f}")

alpha = 0.05
if pval < alpha:
    print("Reject the null hypothesis: The tutoring program significantly improves exam scores.")
else:
    print("Fail to reject the null hypothesis: There is no significant improvement in exam scores from the tutoring program.")
