import random
import numpy as np


def run_q1():
    """Créer une matrice de 3 lignes et 5 colonnes ne contenant que des False."""
    return np.zeros((3, 5))


def run_q2():
    """Créer une matrice de 5 lignes et 5 colonnes contenant aléatoirement True ou False"""
    vals = [False, True]
    return np.random.choice(vals, (5, 5), p=[0.5, 0.5])


def run_q3():
    """Créer une matrice de 6 lignes et 4 colonnes qui contient les lettres de l'alphabet de gauche à droite et de haut en bas."""
    m = np.chararray((6, 4))
    current_letter = "a"
    for i in range(6):
        for j in range(4):
            m[i][j] = current_letter
            current_letter = chr(ord(current_letter) + 1)
    return m


def run_q4(m, n):
    """Définir une fonction define_life_grid(m, n) qui génère une grille de m lignes et n colonnes contenant aléatoirement True ou False."""
    return np.random.choice([False, True], (m, n), p=[0.5, 0.5])


def run_q5(m, n, p):
    """Définir une fonction define_life_grid(m, n, p) qui génère une grille de m lignes et n colonnes contenant aléatoirement True ou False, avec la probabilité p d'avoir True. (astuce: `True if random.random() < p else False`)"""
    return np.random.choice([False, True], (m, n), p=[1 - p, p])


print("q1", run_q1())
print("q2", run_q2())
print("q3", run_q3())
print("q4", run_q4(10, 3))
print("q5", run_q5(6, 7, 0.44))
