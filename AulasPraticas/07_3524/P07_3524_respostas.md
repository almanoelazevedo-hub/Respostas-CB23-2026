16/09/2026
Nome: Manoel Felipe Macena de Azevedo
Matrícula: 3524

Questão 1 e 2 - Discussão sobre a Busca no Labirinto

Para achar o caminho da posição (1,1) até o queijo ('*'), foi implementada a Busca em Profundidade (DFS) de forma iterativa, ultilizando uma pilha explícita.
Escolha da abordagem (DFS vs BFS):
* DFS (Busca em Profundidade): Explora um caminho o máximo que puder até encontrar um beco sem saída e depois faz o backtracking. Como usa uma pilha (LIFO), casa direto com o que vimos na aula anterior sobre pilhas.
* BFS (Busca em Largura): Usaria uma fila (FIFO) para explorar o labitinto em camadas/níveis a partir da origem.

Por que usou o DFS?
1. Era o requisito direto da questão 1 (adaptar o DFS do maze_builder.py para a forma iterativa).
2. A versão iterativa com pilha explícita é melhor que a recursiva porque não estoura o limite de recursão do Python (sys.setrecursionlimit).
3. Sobre caminho minimo: Em grafos gerais o DFS não garante o menor caminho, mas como o maze_builder gera um labirinto perfeito (uma árvore sem ciclos), existe só um caminho único entre a entrada e o queijo. Logo, o DFS encontra esse caminho sem problemas.