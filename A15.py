import numpy as np
from scipy import stats

def ab_test(layout_a_clicks, layout_b_clicks):
    # Calculate sample statistics
    mean_a = np.mean(layout_a_clicks)
    mean_b = np.mean(layout_b_clicks)
    var_a = np.var(layout_a_clicks, ddof=1)
    var_b = np.var(layout_b_clicks, ddof=1)
    n_a = len(layout_a_clicks)
    n_b = len(layout_b_clicks)
    
    # Calculate pooled standard deviation
    pooled_std = np.sqrt((var_a/n_a) + (var_b/n_b))
    
    # Calculate t-statistic
    t_statistic = (mean_a - mean_b) / pooled_std
    
    # Degrees of freedom
    dof = n_a + n_b - 2
    
    # Calculate p-value
    p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), dof))
    
    return t_statistic, dof, p_value

# Define the data
layout_a_clicks = np.array([28, 32, 33, 29, 31, 34, 30, 35, 36, 37])
layout_b_clicks = np.array([40, 41, 38, 42, 39, 44, 43, 41, 45, 47])

# Perform A/B test analysis
t_statistic, dof, p_value = ab_test(layout_a_clicks, layout_b_clicks)

# Print the results
print(f"t-statistic: {t_statistic:.4f}")
print(f"Degrees of freedom: {dof}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in click-through rates between the two layouts.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in click-through rates between the two layouts.")
