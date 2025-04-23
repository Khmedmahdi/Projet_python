def Indicator_local_search1(population, archive, max_size):
    """
    Effectue une recherche locale sur une population en utilisant un indicateur donné.
    """
    # Parcourir tous les individus de la population
    for ind in population.individuals:
        # Effectuer des modifications locales pour améliorer les objectifs
        for i in range(len(ind.Items)):
            if ind.Items[i] == 0:  # Si l'item n'est pas pris
                # Tenter de l'ajouter
                ind.Items[i] = 1
                feasible = all(ind.capa[k] + ind.v[k] <= 1.0 for k in range(len(ind.f)))  # Exemple avec max_bound = 1.0
                if feasible:
                    # Mise à jour de l'individu
                    for k in range(len(ind.f)):
                        ind.capa[k] += ind.v[k]
                        ind.f[k] += ind.v[k]
                else:
                    # Revenir en arrière si ce n'est pas faisable
                    ind.Items[i] = 0

        # Ajouter l'individu amélioré à l'archive s'il est non dominé
        add_to_archive_if_non_dominated(archive, ind, max_size)


def add_to_archive_if_non_dominated(archive, ind, max_size):
    """
    Ajoute un individu à l'archive s'il n'est dominé par aucun autre individu.
    """
    # Vérifier si l'individu est non dominé
    is_non_dominated = True
    for other_ind in archive.individuals:
        if dominates(other_ind, ind, len(ind.f)):
            is_non_dominated = False
            break

    # Ajouter l'individu s'il est non dominé
    if is_non_dominated:
        archive.individuals.append(ind)
        archive.size += 1

        # Si l'archive dépasse la taille maximale, supprimer le pire individu
        if archive.size > max_size:
            archive.individuals.pop()
            archive.size -= 1