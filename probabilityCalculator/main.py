import prob_calculator
from pytest import main

# Seed the random number generator for reproducibility.
prob_calculator.random.seed(95)

# Create a Hat object with a specified distribution of balls.
hat = prob_calculator.Hat(blue=6, red=5, green=2,brown=3, yellow=8)

# Use the experiment function to estimate the probability of drawing specific balls.
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 4, "red": 3, "green": 2, "brown": 2, "yellow":4},
    num_balls_drawn=15,
    num_experiments=3000)

# Print the estimated probability.
print("Probability:", probability)

# Run unit tests automatically to validate the code.
main(['-vv'])
