import random

class Individual:
    """
    Représente un individu avec les propriétés nécessaires.
    """
    def __init__(self, num_items, num_objectives):
        self.nombr_nonpris = 0
        self.nombr = 0
        self.rank = 0
        self.fitness = -1.0
        self.fitnessbest = -1.0
        self.explored = 0
        self.f = [0.0] * num_objectives  # Valeurs des objectifs
        self.capa = [0.0] * num_objectives
        self.v = [0.0] * num_objectives
        self.d = list(range(num_items))  # Liste des items
        self.Items = [0] * num_items
        self.solution = self.Items  # Synchronisation avec Items

    def copy(self):
        """
        Crée une copie de l'individu.
        """
        new_ind = Individual(len(self.d), len(self.f))
        new_ind.__dict__.update(self.__dict__)
        return new_ind


class Population:
    """
    Représente une population avec une taille maximale et une liste d'individus.
    """
    def __init__(self, maxsize, num_objectives, num_items):
        self.size = 0
        self.maxsize = maxsize
        self.individuals = [Individual(num_items, num_objectives) for _ in range(maxsize)]


def create_population(maxsize, num_objectives, num_items):
    """
    Crée une population avec une taille maximale donnée.
    """
    return Population(maxsize, num_objectives, num_items)


def random_initialize_population(population, num_items):
    """
    Initialise aléatoirement une population.
    """
    for ind in population.individuals:
        ind.Items = [1 if random.random() > 0.5 else 0 for _ in range(num_items)]
        ind.solution = ind.Items  # Synchronisez solution avec Items
        ind.d = random.sample(range(num_items), num_items)
        print(f"Individu initialisé : {ind.Items}")


def dominates(ind_a, ind_b, num_objectives):
    """
    Détermine si l'individu `ind_a` domine l'individu `ind_b`.
    """
    a_is_worse = False
    equal = True

    for i in range(num_objectives):
        if ind_a.f[i] > ind_b.f[i]:
            a_is_worse = True
        if ind_a.f[i] != ind_b.f[i]:
            equal = False

    return not a_is_worse and not equal