import random
import A1

def simulate_dice_rolls(n):
    rolls = [random.randint(1, 6) for _ in range(n)]
    mean = A1.calculate_mean(rolls)
    variance = A1.calculate_variance(rolls)
    return mean, variance

mean_roll, var_roll = simulate_dice_rolls(1000)
print("Expected Value (Mean):", mean_roll)
print("Variance:", var_roll)
