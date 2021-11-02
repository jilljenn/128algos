% D'autres problèmes algorithmiques
% Jill-Jênn Vie; Christoph Dürr
% 29 mars 2016

# Recherches avec le moteur d'ElasticSearch

- Robuste aux fautes de frappe
- Comment formaliser la notion de *mot proche* ?

. . .

## Distance d'édition de Levenshtein

- l'\alert{addition} d'une lettre : ``arbre -> arbore``
- la \alert{délétion} d'une lettre : ``globe -> lobe``
- la \alert{substitution} d'une lettre par une autre : ``barbe -> barre``.

Ces opérations ont chacune un coût de 1.

```python
from tryalgo.levenshtein import levenshtein
print(levenshtein('ALGO', 'LEGO'))  # Renvoie 2
```

# Est-ce un plus court chemin dans un graphe ?

\centering
![Levenshtein](levenshtein.pdf)\ 

. . .

Non, le nombre de voisins (plus de 50) exploserait à chaque nœud.

# Se ramener à des sous-problèmes

$dist(ALGO, LEGO) = dist(ALG, LEG) = dist(AL, LE) = \ldots$

## Si l'un des mots est vide

La distance est la longueur de l'autre.

## Sinon, trois cas possibles

- soit une addition : on se ramène à ALGO et LEG + 1
- soit une délétion : on se ramène à ALG et LEGO + 1
- soit une substitution : on se ramène à ALG et LEG  
\+ (0 si même dernière lettre, 1 sinon)

Ce procédé \alert{termine} puisqu'on a des mots plus petits à chaque fois.  
… Autant \alert{stocker} les distances des préfixes !

# Programmation dynamique

- 1950 : Richard Bellman invente la programmation dynamique
- 1957 : FORTRAN, le premier langage de programmation de haut niveau compilé

. . .

## Stocker les réponses aux sous-problèmes dans un tableau

\raggedleft
$dist[i][j]$ : \alert{distance d'édition} des $i$ premières lettres de $x$  
avec les $j$ premières lettres de $y$.

\begin{columns}
\begin{column}{0.5\textwidth}
\centering
\includegraphics{prog-dyn}
\end{column}
\begin{column}{0.5\textwidth}
$\begin{array}{cccccc}
& & L & E & G & O\\
& 0 & 1 & 2 & 3 & 4\\
A & 1 & 1 & 2 & 3 & 4\\
L & 2 & 1 & 2 & 3 & 4\\
G & 3 & 2 & 2 & 2 & 3\\
O & 4 & 3 & 3 & 3 & \alert2
\end{array}$
\end{column}
\end{columns}

# Le code dans tryalgo

```python
def levenshtein(x, y):
  n = len(x)
  m = len(y)
  # initialisation ligne 0 et colonne 0
  A = [[i + j for j in range(m + 1)]
              for i in range(n + 1)]
  for i in range(n):
    for j in range(m):
      A[i + 1][j + 1] = min(A[i][j + 1] + 1,  # addition
                            A[i + 1][j] + 1,  # deletion
                            A[i][j] + int(x[i] != y[j]))
                            # substitution
  return A[n][m]
```
