def evaluate(ind, weights, profits, capacities, num_objectives):
    """
    Évalue un individu en calculant les deux objectifs.
    :param ind: Individu à évaluer
    :param weights: Liste des poids des items
    :param profits: Liste des profits des items
    :param capacities: Liste des capacités des sacs
    :param num_objectives: Nombre d'objectifs
    """
    ind.f = [0.0] * num_objectives  # Initialiser les objectifs à zéro

    for i in range(num_objectives):
        total_weight = 0
        total_profit = 0

        # Calculer le poids total et le profit total pour l'objectif i
        for j in range(len(ind.solution)):
            if ind.solution[j] == 1:  # Si l'item est sélectionné
                total_weight += weights[i][j]
                total_profit += profits[i][j]

        # Vérifier les contraintes de poids
        if total_weight <= capacities[i]:
            ind.f[i] = total_profit  # Assigner le profit si la contrainte est respectée
        else:
            ind.f[i] = 0.0  # Si la contrainte est violée, objectif = 0

    print(f"Évaluation de l'individu : Objectif 1 = {ind.f[0]}, Objectif 2 = {ind.f[1]}")