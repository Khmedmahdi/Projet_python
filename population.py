from common import Individual, Population

def create_population(maxsize, num_objectives, num_items):
    return Population(maxsize, num_objectives, num_items)

def create_individual(num_items, num_objectives):
    return Individual(num_items, num_objectives)

def random_initialize_population(population, num_items):
    for ind in population.individuals:
        ind.Items = [1 if random.random() > 0.5 else 0 for _ in range(num_items)]
        ind.d = random.sample(range(num_items), num_items)