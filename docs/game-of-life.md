# Jeu de la vie

## Règles

-   Soit une grille de `n` lignes et `n` colonnes
-   Chaque cellule vaut soit `True` (vivant) ou `False` (mort)
-   A chaque itération les cellules évoluent selon l'état de leurs voisons directs.
    -   Le voisinage considéré est un voisinage de Moore (8 voisins).
-   Les règles de transition sont fonction de l’état de la cellule et du nombre `v` de voisins vivants :
    -   si `v < 2` l’état suivant est : Mort
    -   si `v == 2` la cellule ne change pas d’état
    -   si `v == 3` l’état suivant est : Vivant
    -   si `v > 3` l’état suivant est : Mort

## Travail demandé

-   Développer un script python qui affiche le déroulement du jeu de la vie sur une grille de dimension n x n. n sera fixé au début du script et pourra être modifié d'une exécution à une autre. **(4 pts)**
    -   Les cellules de la grille initiale auront une chance de 80% de valoir `True`.
    -   Cette tâche est requise pour noter le reste du travail.
-   Permettre à l'utilisateur de changer la durée entre deux générations (ou itérations) avec les touches **+** et **-** de son clavier. **(2 pts)**
    -   Ne pas utiliser de `sleep` mais utiliser plutôt l'argument `frame` de la fonction `update`
-   Afficher sur le graphique les informations sur le programme. **(3 pts)**
    -   Nombre de vivants et de morts total.
    -   Nombre de naissance et de décès lors de la dernière l'itération.
    -   Vitesse de l'animation (ou temps entre deux itérations).
-   Permettre à l'utilisateur de mettre en pause / reprendre l'animation avec **p**. **(2 pts)**
-   Permettre à l'utilisateur de sauvegarder dans un fichier l'état courant du programme et de le recharger. **(3 pts)**
    -   Sauvegarde via la touche **s** du clavier. Le programme se termine ou continue quand on sauvegarde (faire au plus simple).
    -   Rechargement via la touche **r** du clavier ou au démarrage du programme.
    -   Informations à enregistrer: grille actuelle, informations affichées à l'écran ainsi que les réglages (vitesse, etc.)
-   Ajouter un état au jeu de la vie: "**naissance**". **(4 pts)**
    -   Une cellule morte bascule vers l'état naissance avant de passer vers l'état "vivant" pendant **b** itérations.
    -   Si **b** vaut 0, cela revient au jeu de la vie initial.
    -   Une cellule en état **naissance** n'est pas comprise dans les règles de transition.
    -   Permettre à l'utilisateur d'incrémenter / décrémenter la valeur de **b** en appuyant sur les touches **b** et **n** respectivement.
-   Ajouter une fonctionnalité utile de votre part. **(2 pts)**

## Astuces et conseils

??? "Ce script montre comment capter un pression sur le clavier et comment afficher à l'utilisateur des informations sur le graphique"
`py --8<-- animation.py --8<-- `

??? "Ce script montre comment sauvegarder des données dans un fichier"
`py --8<-- save_file.py --8<-- `

??? "Ce script montre comment charger des données depuis un fichier"
`py --8<-- load_file.py --8<-- `
