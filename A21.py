import numpy as np
from scipy.stats import chi2_contingency

# Generate synthetic data
np.random.seed(0)
age_groups = np.random.choice(['18-30', '31-50', '51+'], size=500)
voter_preferences = np.random.choice(['Candidate A', 'Candidate B'], size=500)

# Create a contingency table (observed frequencies)
contingency_table = np.zeros((3, 2), dtype=int)

for i, age_group in enumerate(['18-30', '31-50', '51+']):
    for j, preference in enumerate(['Candidate A', 'Candidate B']):
        contingency_table[i, j] = np.sum((age_groups == age_group) & (voter_preferences == preference))

print("Contingency Table:")
print(contingency_table)

# Perform Chi-Square test for independence
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the results
print(f"\nChi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("\nReject the null hypothesis: There is a significant association between age groups and voter preferences.")
else:
    print("\nFail to reject the null hypothesis: There is no significant association between age groups and voter preferences.")
