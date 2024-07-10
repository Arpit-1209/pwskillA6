import random

int_list = [random.randint(90, 130) for _ in range(100)]
print(int_list)

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

mean_value = calculate_mean(int_list)
print("Mean:", mean_value)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

median_value = calculate_median(int_list)
print("Median:", median_value)

from collections import Counter

def calculate_mode(numbers):
    counter = Counter(numbers)
    max_count = max(counter.values())
    mode = [num for num, count in counter.items() if count == max_count]
    return mode

mode_value = calculate_mode(int_list)
print("Mode:", mode_value)

def weighted_mean(values, weights):
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

values = int_list
weights = [random.randint(1, 10) for _ in range(100)]
w_mean_value = weighted_mean(values, weights)
print("Weighted Mean:", w_mean_value)

import math

def geometric_mean(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product ** (1/len(numbers))

geom_mean_value = geometric_mean([x for x in int_list if x > 0])
print("Geometric Mean:", geom_mean_value)

def harmonic_mean(numbers):
    return len(numbers) / sum(1/x for x in numbers if x != 0)

harm_mean_value = harmonic_mean(int_list)
print("Harmonic Mean:", harm_mean_value)

def midrange(numbers):
    return (min(numbers) + max(numbers)) / 2

midrange_value = midrange(int_list)
print("Midrange:", midrange_value)

def trimmed_mean(numbers, percentage):
    numbers.sort()
    n = len(numbers)
    trim = int(n * percentage)
    trimmed_list = numbers[trim:-trim]
    return sum(trimmed_list) / len(trimmed_list)

trim_mean_value = trimmed_mean(int_list, 0.1)
print("Trimmed Mean:", trim_mean_value)
