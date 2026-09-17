"""
Atividade Prática - Aula 7 (14/09)
Aluno: Manoel Felipe Macena de Azevedo / 3524
"""

import random
import maze_builder as mb

def dfs_iterativo(lab, inicio):
    lin, col = len(lab), len(lab[0])
    pilha = [inicio]
    vis = {inicio}
    pai = {inicio: None}
    queijo = None

    while pilha:
        curr = pilha.pop()
        r, c = curr
        if lab[r][c] == '*':
            queijo = curr
            break
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < lin and 0 <= nc < col:
                if lab[nr][nc] != 'W' and (nr, nc) not in vis:
                    vis.add((nr, nc))
                    pai[(nr, nc)] = curr
                    pilha.append((nr, nc))

    if not queijo:
        return []

    caminho = []
    curr = queijo
    while curr:
        caminho.append(curr)
        curr = pai[curr]
    return caminho[::-1]

m, n = 10, 14
random.seed(42)
lab = mb.generate_maze(m, n, room=' ', wall='W', cheese='*')
lab[1][1] = 'S'

caminho = dfs_iterativo(lab, (1, 1))

for r, c in caminho:
    if lab[r][c] not in ('S', '*'):
        lab[r][c] = '.'

print("Labirinto resolvido:")
mb.print_maze(lab)