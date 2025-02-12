import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, n in kwargs.items():
           self.contents.extend([color] * n)

    def draw(self, number):
        if number >= len(self.contents):
            balls = self.contents
            self.contents = []
            return balls
            
        balls = []
        for i in range(number):
            ball = random.choice(self.contents)
            balls.append(ball)
            self.contents.remove(ball)
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0

    for i in range(num_experiments):

        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)

        test = {}
        for ball in balls:
            if ball in test:
                test[ball] += 1
            else:
                test[ball] = 1
        
        success = all(test.get(ball, 0) >= expected_balls[ball] for ball in expected_balls)
      
        if success:
            M += 1
            
    return M / num_experiments
