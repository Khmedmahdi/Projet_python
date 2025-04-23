def evaluate(ind, weights, profits, capacities, num_objectives):
    """
    Évalue un individu en calculant les deux objectifs.
    """
    ind.f = [0.0] * num_objectives  # Initialiser les objectifs à zéro

    for i in range(num_objectives):
        total_weight = 0
        total_profit = 0

        # Utilisez ind.Items au lieu de ind.solution
        for j in range(len(ind.Items)):
            if ind.Items[j] == 1:  # Si l'item est sélectionné
                total_weight += weights[i][j]
                total_profit += profits[i][j]

        # Vérifier les contraintes de poids
        if total_weight <= capacities[i]:
            ind.f[i] = total_profit  # Assigner le profit si la contrainte est respectée
        else:
            ind.f[i] = 0.0  # Si la contrainte est violée, objectif = 0

    print(f"Évaluation de l'individu : Objectif 1 = {ind.f[0]}, Objectif 2 = {ind.f[1]}")