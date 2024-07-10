import numpy as np
from scipy import stats

def independent_t_test(data1, data2):
    # Calculate sample statistics
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    var1 = np.var(data1, ddof=1)
    var2 = np.var(data2, ddof=1)
    n1 = len(data1)
    n2 = len(data2)
    
    # Calculate pooled standard deviation
    pooled_std = np.sqrt((var1/n1) + (var2/n2))
    
    # Calculate t-statistic
    t_statistic = (mean1 - mean2) / pooled_std
    
    # Degrees of freedom (approximated using Welch's formula)
    dof = ((var1/n1 + var2/n2)**2) / ((var1**2 / (n1**2 * (n1 - 1))) + (var2**2 / (n2**2 * (n2 - 1))))
    
    # Calculate p-value
    p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), dof))
    
    return t_statistic, dof, p_value

# Define the data
existing_drug_levels = np.array([180, 182, 175, 185, 178, 176, 172, 184, 179, 183])
new_drug_levels = np.array([170, 172, 165, 168, 175, 173, 170, 178, 172, 176])

# Perform two-sample independent t-test
t_statistic, dof, p_value = independent_t_test(existing_drug_levels, new_drug_levels)

# Print the results
print(f"t-statistic: {t_statistic:.4f}")
print(f"Degrees of freedom: {dof:.2f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The new drug is more effective than the existing drug in reducing cholesterol levels.")
else:
    print("Fail to reject the null hypothesis: There is no sufficient evidence that the new drug is more effective than the existing drug.")
