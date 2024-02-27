# Exercices

Utiliser numpy pour faire ces exercices:

1. Créer une matrice de 3 lignes et 5 colonnes ne contenant que des False.
1. Créer une matrice de 5 lignes et 5 colonnes contenant aléatoirement True ou False. (astuce: `bool(random.getrandbits(1))`)
1. Créer une matrice de 6 lignes et 4 colonnes qui contient les lettres de l'alphabet de gauche à droite et de haut en bas.
1. Définir une fonction define_life_grid(m, n) qui génère une grille de m lignes et n colonnes contenant aléatoirement True ou False.
1. Définir une fonction define_life_grid(m, n, p) qui génère une grille de m lignes et n colonnes contenant aléatoirement True ou False, avec la probabilité p d'avoir True. (astuce: `True if random.random() < p else False`)

Bonus: faire ces mêmes exercices sans utiliser numpy.

??? "Solution avec numpy"

    ```py
    --8<-- "exos_avec_numpy.py"
    ```

??? "Solution sans numpy"

    ```py
    --8<-- "exos_python_avance.py"
    ```
