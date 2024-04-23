import numpy as np
import environment as env

# Class representing an artificial ant of the ant colony
"""
    alpha: a parameter controlling the influence of the amount of pheromone during ants' path selection process
    beta: a parameter controlling the influence of the distance to the next node during ants' path selection process
"""
class Ant:
    def __init__(self, alpha: float, beta: float, initial_location):
        self.alpha = alpha
        self.beta = beta
        self.current_location = initial_location
        self.travelled_distance = 0
        self.tour = []
        

    # The ant runs to visit all the possible locations of the environment
    def run(self):
        self.tour = [self.current_location]
        while len(set(self.tour)) < len(self.environment.nodes):
            self.select_path()
        self.tour.append(self.tour[0])

    # Select the next path based on the random proportional rule of the ACO algorithm
    def select_path(self):
        unvisited = set(self.environment.nodes) - set(self.tour)
        total = sum(pheromone ** self.alpha * (1.0 / self.environment.get_distance(self.current_location, node)) ** self.beta
                    for node in unvisited
                    for pheromone in (self.environment.get_pheromone(self.current_location, node),))
        probabilities = np.array([(self.environment.get_pheromone(self.current_location, node) ** self.alpha *
                                  (1.0 / self.environment.get_distance(self.current_location, node)) ** self.beta / total)
                                 for node in unvisited])
        next_node = np.random.choice(list(unvisited), p=probabilities)
        self.tour.append(next_node)
        self.current_location = next_node

    # Position an ant in an environment
    def join(self, environment):
        self.environment = environment
