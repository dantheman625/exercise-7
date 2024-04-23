import numpy as np
import tsplib95
from tsplib95.distances import pseudo_euclidean

# Class representing the environment of the ant colony
"""
    rho: pheromone evaporation rate
"""
class Environment:
    def __init__(self, rho):
        self.rho = rho
        self.problem = tsplib95.load_problem("att48-specs/att48.tsp")
        self._init_nodes()
        self._init_pheromones()
        self._init_distances()

    def _init_nodes(self):
        self.nodes = list(self.problem.get_nodes())

    def _init_pheromones(self):
        self.pheromones = np.full((len(self.nodes), len(self.nodes)), self._init_pheromone())

    def _init_distances(self):
        self.distances = self._calculate_distances()

    def _init_pheromone(self):
        return 0.5

    def _calculate_distances(self):
        return np.array([[self._calculate_distance(i, j) for j in self.nodes] for i in self.nodes])

    def _calculate_distance(self, i, j):
        start_coord = self.problem.node_coords[i]
        end_coord = self.problem.node_coords[j]
        return pseudo_euclidean(start_coord, end_coord)

    def update_pheromone_map(self, ants):
        self.pheromones *= (1 - self.rho)
        for ant in ants:
            for i in range(len(ant.tour)-1):
                self._update_pheromone(ant.tour[i]-1, ant.tour[i+1]-1)

    def _update_pheromone(self, start_node, end_node):
        distance = self.get_distance(start_node, end_node)
        pheromone_to_add = 1 / distance
        self.pheromones[start_node][end_node] += pheromone_to_add

    def get_pheromone(self, i, j):
        return self.pheromones[i-1][j-1]

    def get_distance(self, i, j):
        return self.distances[i-1][j-1]
        return distance
