# Jeu de la vie

## Règles

- Soit une grille de `m` lignes et `n` colonnes
- Chaque cellule vaut soit `True` (vivant) ou `False` (mort)
- A chaque itération les celulles évoluent selong l'état de leurs voisons directs.
  - Le voisinage considéré est un voisinage de Moore (8 voisins). 
- Les règles de transition sont fonction de l’état de la cellule et du nombre `v` de voisins vivants :
  - si `v < 2` l’état suivant est : Mort
  - si `n == 2` la cellule ne change pas d’état
  - si `n == 3` l’état suivant est : Vivant
  - si `n > 3` l’état suivant est : Mort

## Travail demandé

- 