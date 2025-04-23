import time
import random
from ibmols import create_population, random_initialize_population
from indicators import calc_indicator_value
from search import Indicator_local_search1
from archive import extractPtoArchive
from evaluation import evaluate
from perturbation import perturbation


def main():
    print("=== Début de l'exécution ===")

    # Paramètres du problème
    print("Chargement des paramètres du problème...")
    num_objectives = 2  # Nombre de fonctions objectifs
    num_items = 250  # Nombre d'items
    max_population_size = 15000  # Taille maximale de la population
    alpha = 10  # Nombre d'individus dans la population initiale

    # Définition des capacités, poids et profits (exemple fictif)
    print("Génération des données fictives (capacités, poids, profits)...")
    capacities = [100, 200]  # Exemple
    weights = [[random.randint(1, 10) for _ in range(num_items)] for _ in range(num_objectives)]
    profits = [[random.randint(1, 10) for _ in range(num_items)] for _ in range(num_objectives)]
    print("Données générées avec succès.")

    # Initialisation des populations et archives
    print("Initialisation des populations et de l'archive...")
    population = create_population(max_population_size, num_objectives, num_items)
    archive = create_population(max_population_size, num_objectives, num_items)
    random_initialize_population(population, num_items)
    print("Population initialisée avec succès.")

    # Évaluation initiale des individus
    print("Évaluation initiale des individus dans la population...")
    for ind in population.individuals:
        evaluate(ind, weights, profits, capacities, num_objectives)
        print(f"Individu évalué : Objectif 1 = {ind.f[0]}, Objectif 2 = {ind.f[1]}")
    print("Évaluation terminée.")

    # Extraction des solutions non dominées
    print("Extraction des solutions non dominées vers l'archive...")
    convergence_rate = extractPtoArchive(population, archive)
    print(f"Taux de convergence : {convergence_rate:.2f}")

    # Sauvegarde des résultats dans un fichier
    print("Sauvegarde des résultats dans 'results.txt'...")
    with open("results.txt", "w") as f:
        for ind in archive.individuals:
            f.write(f"{ind.f[0]}\t{ind.f[1]}\n")
            print(f"Écriture dans le fichier : {ind.f[0]}\t{ind.f[1]}")
    print("Résultats sauvegardés avec succès.")

    # Mesure de la durée totale d'exécution
    end_time = time.time()
    print(f"Durée totale d'exécution : {end_time - start_time:.2f} secondes")

    print("=== Fin de l'exécution ===")


if __name__ == "__main__":
    main()