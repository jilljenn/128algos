from tryalgo.kruskal import kruskal
from tryalgo.bfs import bfs
from tryalgo.dfs import dfs
from random import randint

def make_grid(n, m, edges=None):
    if edges:
        access = [[False] * (n * m) for _ in range(n * m)]
        for u, v in edges:
            access[u][v] = True
    else:
        access = [[True] * (n * m) for _ in range(n * m)]
    graph = {u: [] for u in range(n * m)}
    weight = [[float('inf')] * (n * m) for _ in range(n * m)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(n):
        for j in range(m):
            for di, dj in dirs:
                if 0 <= i + di < n and 0 <= j + dj < m and (access[i * m + j][(i + di) * m + j + dj] or access[(i + di) * m + j + dj][i * m + j]):
                    graph[i * m + j].append((i + di) * m + j + dj)
                    weight[i * m + j][(i + di) * m + j + dj] = randint(1, 100)
    return graph, weight

def plot_grid(m, graph):
    with open('coords.tex', 'w') as f:
        for u in graph:
            for v in graph[u]:
                f.write(r'\draw (%d,%d) -- (%d,%d);' % (u % m, u // m, v % m, v // m) + '\n')

def plot_frame(n, m):
    with open('frame.tex', 'w') as f:
        f.write(r'\draw[ultra thick] (-0.5,-0.5) -- ++(0,%d) -- ++(%d,0);' % (n, m) + '\n')
        f.write(r'\draw[ultra thick] (0.5,-0.5) -- ++(%d,0) -- ++(0,%d);' % (m - 1, n - 1) + '\n')
        f.write(r'\draw[->,ultra thick] (0,-1) -- ++(0,1);' + '\n')
        f.write(r'\draw[->,ultra thick] (%d,%d) -- ++(1,0);' % (m - 1, n - 1))

def plot_edges(n, m, edges):
    access = [[False] * (n * m) for _ in range(n * m)]
    for u, v in edges:
        access[u][v] = True
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    with open('coords.tex', 'w') as f:
        """
        f.write(r'\draw[ultra thick] (-0.5,-0.5) -- ++(0,%d) -- ++(%d,0);' % (n, m) + '\n')
        f.write(r'\draw[ultra thick] (0.5,-0.5) -- ++(%d,0) -- ++(0,%d);' % (m - 1, n - 1) + '\n')
        f.write(r'\draw[->,ultra thick] (0,-1) -- ++(0,1);')
        f.write(r'\draw[->,ultra thick] (%d,%d) -- ++(1,0);' % (m - 1, n - 1))
        """
        for i in range(n):
            for j in range(m):
                for di, dj in dirs:
                    if 0 <= i + di < n and 0 <= j + dj < m and not access[i * m + j][(i + di) * m + j + dj] and not access[(i + di) * m + j + dj][i * m + j]:
                        f.write(r'\draw[ultra thick,rotate around={90:(%f,%f))}] (%d,%d) -- (%d,%d);' % (j + dj / 2, i + di / 2, j, i, j + dj, i + di) + '\n')

def plot_path(n, m, prec):
    node = (n - 1) * m + m - 1
    with open('path.tex', 'w') as f:
        while True:
            if node is None:
                break
            f.write(r'\filldraw[cyan!20!white] (%f,%f) rectangle ++(1,1);' % (node % m - 0.5, node // m - 0.5) + '\n')
            print(node, prec[node])
            node = prec[node]

n, m = 5, 7
# grid_graph, weight = make_grid(n, m)
# laby_edges = kruskal(grid_graph, weight)
# plot_grid(m, grid_graph)

n, m = 5, 3
worst_case = [
    'R', 'RU', 'U',
    'U', 'L', 'U',
    'R', 'U', 'U',
    'U', 'L', 'U',
    'R', 'R', ''
]
worst_case_graph = {u: [] for u in range(n * m)}
worst_case_edges = []
for u in range(n * m):
    if 'L' in worst_case[u]:
        worst_case_edges.append((u, u - 1))
        worst_case_graph[u].append(u - 1)
    if 'R' in worst_case[u]:
        worst_case_edges.append((u, u + 1))
        worst_case_graph[u].append(u + 1)
    if 'U' in worst_case[u]:
        worst_case_edges.append((u, u + 3))
        worst_case_graph[u].append(u + m)

plot_edges(n, m, worst_case_edges)

# plot_edges(n, m, laby_edges)
"""laby_graph, _ = make_grid(n, m, laby_edges)
print(laby_graph)
_, prec = bfs(laby_graph)
plot_path(n, m, prec)"""

prec = dfs(worst_case_graph)
_, prec = bfs(worst_case_graph)
plot_path(n, m, prec)

plot_frame(n, m)
