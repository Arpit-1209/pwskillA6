import numpy as np
from scipy import stats

def paired_t_test(pre_scores, post_scores):
    # Perform paired sample t-test
    t_statistic, p_value = stats.ttest_rel(post_scores, pre_scores)
    
    return t_statistic, p_value

# Define the data
pre_intervention_scores = np.array([80, 85, 90, 75, 88, 82, 92, 78, 85, 87])
post_intervention_scores = np.array([90, 88, 92, 95, 91, 96, 93, 89, 93])

# Perform paired sample t-test
t_statistic, p_value = paired_t_test(pre_intervention_scores, post_intervention_scores)

# Print the results
print(f"t-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The intervention had a significant impact on math scores.")
else:
    print("Fail to reject the null hypothesis: There is no sufficient evidence that the intervention had a significant impact on math scores.")
