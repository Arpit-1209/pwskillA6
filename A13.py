import numpy as np
from statsmodels.stats import weightstats as stests

# Define the data
before_drug = np.array([145, 150, 140, 135, 155, 160, 152, 148, 130, 138])
after_drug = np.array([130, 140, 132, 128, 145, 148, 138, 136, 125, 130])

# Perform paired z-test for means
stat, pval = stests.ztest(before_drug, after_drug)

# Print the results
print(f"Z-test statistic: {stat:.4f}")
print(f"P-value: {pval:.4f}")

alpha = 0.05
if pval < alpha:
    print("Reject the null hypothesis: The drug significantly reduces blood pressure.")
else:
    print("Fail to reject the null hypothesis: There is no significant reduction in blood pressure from the drug.")
