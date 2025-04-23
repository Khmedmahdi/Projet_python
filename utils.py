def dominates(ind_a, ind_b, num_objectives):
    """
    Vérifie si l'individu `ind_a` domine l'individu `ind_b`.
    """
    better_in_all = True
    strictly_better = False

    for i in range(num_objectives):
        if ind_a.f[i] > ind_b.f[i]:
            better_in_all = False
        if ind_a.f[i] < ind_b.f[i]:
            strictly_better = True

    return better_in_all and strictly_better