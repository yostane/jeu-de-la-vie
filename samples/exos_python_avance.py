import random


def run_q1():
    """Créer une matrice de 3 lignes et 5 colonnes ne contenant que des False."""
    return [[False for j in range(5)] for i in range(3)]


def run_q2():
    """Créer une matrice de 5 lignes et 5 colonnes contenant aléatoirement True ou False"""
    return [[bool(random.getrandbits(1)) for j in range(5)] for i in range(3)]


def run_q3():
    """Créer une matrice de 6 lignes et 4 colonnes qui contient les lettres de l'alphabet de gauche à droite et de haut en bas."""
    m = []
    current_letter = "a"
    for i in range(6):
        line_items = []
        for j in range(4):
            line_items.append(current_letter)
            current_letter = chr(ord(current_letter) + 1)
        m.append(line_items)


def run_q4(m, n):
    """Définir une fonction define_life_grid(m, n) qui génère une grille de m lignes et n colonnes contenant aléatoirement True ou False."""
    return [[bool(random.getrandbits(1)) for j in range(m)] for i in range(n)]


def run_q5(m, n, p):
    """Définir une fonction define_life_grid(m, n, p) qui génère une grille de m lignes et n colonnes contenant aléatoirement True ou False, avec la probabilité p d'avoir True. (astuce: `True if random.random() < p else False`)"""
    return [
        [True if random.random() < p else False for j in range(n)] for i in range(m)
    ]


print("q1", run_q1())
print("q2", run_q2())
print("q3", run_q3())
print("q4", run_q4(10, 3))
print("q5", run_q5(6, 7, 0.44))
