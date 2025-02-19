import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = []
        for key, value in args.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls
        
        drawn_balls = []
        for _ in range(num_balls):
            index = random.randint(0, len(self.contents) - 1)
            drawn_balls.append(self.contents.pop(index))
        
        return drawn_balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_drawn_dict = {}
        for ball in balls_drawn:
            if ball in balls_drawn_dict:
                balls_drawn_dict[ball] += 1
            else:
                balls_drawn_dict[ball] = 1
        flag = True
        for key, value in expected_balls.items():
            if key not in balls_drawn_dict or balls_drawn_dict[key] < value:
                flag = False
                break
        if flag:
            M += 1
    return M / num_experiments
