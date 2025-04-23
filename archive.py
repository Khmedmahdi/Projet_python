from utils import dominates

def extractPtoArchive(population, archive):
    """
    Extrait les individus non dominés de la population et les ajoute à l'archive.
    """
    non_dominated_count = 0

    for ind in population.individuals:
        is_dominated = False
        to_remove = []

        # Vérifier si l'individu est dominé par un autre individu de l'archive
        for archive_ind in archive.individuals:
            if dominates(archive_ind, ind, len(ind.f)):
                is_dominated = True
                break
            elif dominates(ind, archive_ind, len(ind.f)):
                to_remove.append(archive_ind)

        # Si l'individu n'est pas dominé, l'ajouter à l'archive
        if not is_dominated:
            archive.individuals.append(ind)
            archive.size += 1
            non_dominated_count += 1

        # Supprimer les individus dominés de l'archive
        for dominated_ind in to_remove:
            archive.individuals.remove(dominated_ind)
            archive.size -= 1

    # Retourner le taux de convergence
    return non_dominated_count / float(population.size) if population.size > 0 else 0