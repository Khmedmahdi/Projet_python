class Individual:
    def __init__(self, num_items, num_objectives):
        self.nombr_nonpris = 0
        self.nombr = 0
        self.rank = 0
        self.fitness = -1.0
        self.fitnessbest = -1.0
        self.explored = 0
        self.f = [0.0] * num_objectives
        self.capa = [0.0] * num_objectives
        self.v = [0.0] * num_objectives
        self.d = list(range(num_items))
        self.Items = [0] * num_items

class Population:
    def __init__(self, maxsize, num_objectives, num_items):
        self.size = 0
        self.maxsize = maxsize
        self.individuals = [Individual(num_items, num_objectives) for _ in range(maxsize)]