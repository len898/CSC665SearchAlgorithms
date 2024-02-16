class Node:
    def __init__(self, city_name):
        self.city_name = city_name
        self.neighbors = []  # Represents the neighboring cities

    def add_neighbor(self, neighbor_city):
        self.neighbors.append(neighbor_city)

    def __repr__(self):
        return self.city_name
    
