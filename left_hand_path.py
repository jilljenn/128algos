path = "U U R D . U R D . U U . D L L U U U R D D . U R . L U R R R D L . R U R D D L . R D . U U R . L U R R D"
dirs = "UR R DR DL DL DR DR DL DL DR R UR UL UL U UR R R DR DL L DL DR DR DR UR UR DR D D DL UL UL DL DR DR DL L UL UL DL DL DL DR R DR DR UR UR DR D DL"

x, y = -0.5, -0.5
path = path.split()
dirs = dirs.split()
print(len(path), 'VS', len(dirs))
i = 0
sep = 0.2
shifts = {'U': (0, 1), 'R': (1, 0), 'L': (-1, 0), 'D': (0, -1), '.': (0, 0)}
coords = []
with open('path.tex', 'w') as f:
    while i < min(len(dirs), len(path)):
        displayed_node = [x, y]
        for letter in dirs[i]:
            displayed_node[0] += shifts[letter][0] * sep
            displayed_node[1] += shifts[letter][1] * sep
        coords.append(displayed_node)
        x += shifts[path[i]][0]
        y += shifts[path[i]][1]
        i += 1
    print(coords)
    """for x, y in coords:
        f.write(r'\filldraw[black] (%f,%f) circle (2pt);' % (x, y) + '\n')"""
    f.write(r'\draw[red,rounded corners=1mm,very thick,->] ' + ' -- '.join(map(lambda (x, y): '(%f,%f)' % (x, y), coords)) + ';\n')
