import random

def perturbation(ind, weights, profits, capacities, perturbation_rate, num_objectives):
    """
    Applique une perturbation aléatoire à un individu en modifiant une fraction de ses items.
    """
    bruit_rate = round(perturbation_rate * ind.nombr)
    for _ in range(bruit_rate):
        # Sélectionner un item pris aléatoire
        objet = random.choice([i for i, val in enumerate(ind.Items) if val == 1])
        # Retirer cet item
        ind.Items[objet] = 0
        ind.nombr -= 1
        ind.nombr_nonpris += 1
        # Mettre à jour les objectifs et les capacités
        for k in range(num_objectives):
            ind.f[k] -= profits[k][objet]
            ind.capa[k] -= weights[k][objet]