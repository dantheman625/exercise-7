import numpy as np

from environment import Environment
from ant import Ant

# Class representing the ant colony
"""
    ant_population: the number of ants in the ant colony
    iterations: the number of iterations 
    alpha: a parameter controlling the influence of the amount of pheromone during ants' path selection process
    beta: a parameter controlling the influence of the distance to the next node during ants' path selection process
    rho: pheromone evaporation rate
"""
class AntColony:
    def __init__(self, ant_population: int, alpha: float, beta: float, rho: float):
        self.ant_population = ant_population
        self.alpha = alpha
        self.beta = beta
        self.rho = rho

        # Initialize the environment of the ant colony
        self.env = Environment(rho)

        # Initilize the list of ants of the ant colony
        self.ants = []

        # Initialize the ants of the ant colony
        for i in range(ant_population):
            # Initialize an ant on a random initial location
            ant = Ant(self.alpha, self.beta, np.random.choice(self.env.nodes))

            # Position the ant in the environment of the ant colony so that it can move around
            ant.join(self.env)

            # Add the ant to the ant colony
            self.ants.append(ant)

    # Solve the ant colony optimization problem
    def solve(self):

        # The solution will be a list of the visited cities
        solution = []

        # Initially, the shortest distance is set to infinite
        shortest_distance = np.inf

        for ant in self.ants:
            ant.run()
            tour_length = 0
            for i in range(len(ant.tour) - 1):
                single_length = self.env.get_distance(ant.tour[i], ant.tour[i + 1])
                tour_length += single_length
            if tour_length < shortest_distance:
                shortest_distance = tour_length
                solution = ant.tour
        self.env.update_pheromone_map(self.ants)
        return solution, shortest_distance

def main():
    # if one ant is located at each node then number of nodes = population
    population = 48
    # initial values
    alpha = 1
    beta = 5
    rho = 0.5

    ant_colony = AntColony(population, alpha, beta, rho)
    solution, distance = ant_colony.solve()
    print("Solution: ", solution)
    print("Distance: ", distance)

if __name__ == '__main__':
    main()