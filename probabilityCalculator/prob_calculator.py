import copy
import random

class Hat:
    def __init__(self, **balls):
        # Constructor for the Hat class, initializes the contents based on the input arguments.
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls_to_draw):
        # Simulates drawing balls from the hat without replacement.
        # Returns a list of drawn balls.
        if num_balls_to_draw >= len(self.contents):
            return self.contents  # If requested more balls than available, return all.
        drawn_balls = random.sample(self.contents, num_balls_to_draw)
        for ball in drawn_balls:
            self.contents.remove(ball)  # Remove the drawn balls from the hat.
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Simulates experiments to estimate the probability of drawing expected balls.
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)  # Create a copy of the original hat for each experiment.
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_dict = {}
        for ball in drawn_balls:
            if ball in drawn_dict:
                drawn_dict[ball] += 1
            else:
                drawn_dict[ball] = 1

        success = True
        for color, count in expected_balls.items():
            if color not in drawn_dict or drawn_dict[color] < count:
                success = False
                break

        if success:
            success_count += 1

    probability = success_count / num_experiments
    return probability
