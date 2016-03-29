% tryalgo : des labyrinthes jusqu'à Paris
% Jill-Jênn Vie
% 29 mars 2016

# Un labyrinthe

\centering
![Un labyrinthe](laby.pdf)\ 

# Parcours main gauche

\centering
![Un labyrinthe](laby-left-hand.pdf)\ 

# Parcours main gauche ?

\centering
![Un labyrinthe](laby-left-hand-bad.pdf)\ 

# Parcours en profondeur (DFS) avec une pile

\centering
![Un labyrinthe résolu](laby-solved.pdf)\ 

```python
from tryalgo.dfs import dfs
prec = dfs(laby_graph)
```

# Parcours en profondeur (DFS) optimal ?

\centering
![Un labyrinthe résolu](laby-dfs.pdf)\ 
\qquad
![Un labyrinthe résolu](laby-dfs-bad.pdf)\ 

```python
from tryalgo.dfs import dfs
prec = dfs(laby_graph)
```

# Parcours en largeur (BFS) avec une file

\centering
![Un labyrinthe résolu](laby-bfs.pdf)\ 
\qquad
![Un labyrinthe résolu](laby-bfs-good.pdf)\ 

```python
from tryalgo.bfs import bfs
dist, prec = bfs(laby_graph)
```

# Le graphe de Paris

![Paris](paris.png)\ 

# Google Hash Code 2014

## Énoncé original

- On vous donne \alert{8 voitures} partant de Google Paris sur le graphe de Paris à 11348 intersections, 17958 rues.
- Chaque rue est étiquetée par une \alert{distance} en mètres et un \alert{temps} de parcours en secondes.
- Certaines rues sont à \alert{double sens}, d'autres ne le sont pas.
- Comment explorer un \alert{maximum} de km de Paris en \alert{15 heures} ?

## Notre version

Même chose pour une seule voiture partant de NUMA en \alert{2 heures}.

# La meilleure solution : graphes eulériens

\centering
![Euler](euler.pdf)\ 

\vspace{1cm}

\raggedright
\textbf{Condition :} 0 ou 2 nœuds ayant un nombre \alert{impair} de voisins.

# Eulérianiser Paris par des plus courts chemins

\centering
![Eulérianiser Paris](euler-paris.pdf)\ 

\vspace{1cm}

\raggedright
Certains nœuds ont \alert{trop} d'arcs entrants, d'autres en \alert{manquent}.  
\textbf{Idée :} les \alert{coupler} par des \textcolor{blue}{plus courts chemins}.
