import numpy as np
from scipy import stats

# Define the data
branch_a_scores = np.array([4, 5, 3, 4, 5, 4, 5, 3, 4, 4, 5, 4, 4, 3, 4, 5, 5, 4, 3, 4, 5, 4, 3, 5, 4, 4, 5, 3, 4, 5, 4])
branch_b_scores = np.array([3, 4, 2, 3, 4, 3, 4, 2, 3, 3, 4, 3, 3, 2, 3, 4, 4, 3, 2, 3, 4, 3, 2, 4, 3, 3, 4, 2, 3, 4, 3])

def independent_t_test(data1, data2):
    # Perform two-sample independent t-test
    t_statistic, p_value = stats.ttest_ind(data1, data2, equal_var=False)
    
    return t_statistic, p_value

# Perform two-sample independent t-test on the given data
t_statistic, p_value = independent_t_test(branch_a_scores, branch_b_scores)

# Print the results
print(f"t-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference in customer satisfaction between the two branches.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant difference in customer satisfaction between the two branches.")
