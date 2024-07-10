import numpy as np
from scipy import stats

# Define the data
version1_scores = np.array([85, 88, 82, 89, 87, 84, 90, 88, 85, 86, 91, 83, 87, 84, 89, 86, 84, 88, 85, 86, 89, 90, 87, 88, 85])
version2_scores = np.array([80, 78, 83, 81, 79, 82, 76, 80, 78, 81, 77, 82, 80, 79, 82, 79, 80, 81, 79, 82, 79, 78, 80, 81, 82])

def independent_t_test(data1, data2):
    # Perform two-sample independent t-test
    t_statistic, p_value = stats.ttest_ind(data1, data2, equal_var=False)
    
    return t_statistic, p_value

# Perform two-sample independent t-test on the given data
t_statistic, p_value = independent_t_test(version1_scores, version2_scores)

# Print the results
print(f"t-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference in quality scores between the two versions.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant difference in quality scores between the two versions.")
