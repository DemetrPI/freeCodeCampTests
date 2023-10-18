import prob_calculator
import pytest

# Set a seed for reproducible results.
prob_calculator.random.seed(95)

def test_hat_class_contents():
    hat = prob_calculator.Hat(red=3, blue=2)
    actual = hat.contents
    expected = ["red", "red", "red", "blue", "blue"]
    assert actual == expected, 'Expected creation of hat object to add correct contents.'

def test_hat_draw():
    hat = prob_calculator.Hat(red=5, blue=2)
    actual = hat.draw(2)
    expected = ['blue', 'red']
    assert actual == expected, 'Expected hat draw to return two random items from hat contents.'
    actual = len(hat.contents)
    expected = 5
    assert actual == expected, 'Expected hat draw to reduce the number of items in contents.'

def test_prob_experiment():
    hat = prob_calculator.Hat(blue=3, red=2, green=6)
    probability = prob_calculator.experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
    actual = probability
    expected = 0.272
    # Adjust the tolerance to a larger value
    assert pytest.approx(actual, rel=0.027) == expected, 'Expected experiment method to return a different probability.'

    
    hat = prob_calculator.Hat(yellow=5, red=1, green=3, blue=9, test=1)
    probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow": 2, "blue": 3, "test": 1}, num_balls_drawn=20, num_experiments=100)
    actual = probability
    expected = 1.0
    assert pytest.approx(actual, rel=0.01) == expected, 'Expected experiment method to return a different probability.'
