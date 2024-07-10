import numpy as np
from scipy import stats

# Generate synthetic salary data for male and female employees
np.random.seed(0)  # For reproducibility
male_salaries = np.random.normal(loc=50000, scale=10000, size=20)
female_salaries = np.random.normal(loc=55000, scale=9000, size=20)

def independent_t_test(data1, data2):
    # Perform two-sample independent t-test
    t_statistic, p_value = stats.ttest_ind(data1, data2, equal_var=False)
    
    return t_statistic, p_value

# Perform two-sample independent t-test on the synthetic data
t_statistic, p_value = independent_t_test(male_salaries, female_salaries)

# Print the results
print(f"t-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference in average salaries between male and female employees.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant difference in average salaries between male and female employees.")
