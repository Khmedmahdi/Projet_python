# Définition des structures et des fonctions basées sur ibmols.h

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
        ind.d = random.sample(range(num_items), num_items)


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


def max_value(a, b):
    """
    Retourne la valeur maximale entre `a` et `b`.
    """
    return max(a, b)


def calc_add_eps_indicator(ind_a, ind_b, max_bound, num_objectives):
    """
    Calcule l'indicateur epsilon additionnel.
    """
    eps = (ind_a.v[0] / max_bound) - (ind_b.v[0] / max_bound)
    for i in range(1, num_objectives):
        temp_eps = (ind_a.v[i] / max_bound) - (ind_b.v[i] / max_bound)
        if temp_eps > eps:
            eps = temp_eps
    return eps


def tchebycheff(nb, ind):
    """
    Calcule la fonction de Tchebycheff pour un individu.
    """
    return max([abs(ind.f[i]) for i in range(nb)])


def update_reference_point(solutions):
    """
    Met à jour le point de référence à partir des solutions.
    """
    # Exemple basique, nécessite des données supplémentaires pour une implémentation complète
    pass


def compute_ind_fitness(ind, population):
    """
    Calcule la fitness d'un individu en fonction de la population.
    """
    ind.fitness = 0
    for other_ind in population.individuals:
        if other_ind != ind:
            ind.fitness -= calc_add_eps_indicator(other_ind, ind, 1.0, len(ind.f))  # Exemple avec max_bound=1.0


def save_population(population, filename):
    """
    Sauvegarde les individus d'une population dans un fichier.
    """
    with open(filename, 'w') as f:
        for ind in population.individuals:
            f.write(f"{ind.f}\n")


def save_parameters(filename, data):
    """
    Sauvegarde des paramètres dans un fichier.
    """
    with open(filename, 'w') as f:
        f.write(data)