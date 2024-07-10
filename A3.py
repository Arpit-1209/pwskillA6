class DiscreteRandomVariable:
    def __init__(self, outcomes, probabilities):
        self.outcomes = outcomes
        self.probabilities = probabilities

    def expected_value(self):
        return sum(p * x for p, x in zip(self.probabilities, self.outcomes))

    def variance(self):
        mean = self.expected_value()
        return sum(p * (x - mean) ** 2 for p, x in zip(self.probabilities, self.outcomes))

outcomes = [1, 2, 3, 4, 5, 6]
probabilities = [1/6] * 6

drv = DiscreteRandomVariable(outcomes, probabilities)
print("Expected Value:", drv.expected_value())
print("Variance:", drv.variance())
