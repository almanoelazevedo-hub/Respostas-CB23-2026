'''
16/09
Nome: Manoel Felipe Macena de Azevedo  
Matrícula: 3524  
import unittest
'''

class _No:
    #Nó interno da lista encadeada
    __slots__ = ('valor', 'proximo')

    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class PilhaEncadeada:
    #Pilha baseada em encadeamento manual de nós.
    #Operações principais possuem complexidade O(1).

    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        #Insere o item no topo da pilha. Complexidade: O(1).
        novo_no = _No(item, self._topo)
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        #Remove e retorna o item do topo. Complexidade: O(1).
        if self.esta_vazia():
            raise IndexError("pilha igual minha conta bancária")
        
        item = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return item

    def topo(self):
        #Retorna o item do topo sem removê-lo. Complexidade: O(1).
        if self.esta_vazia():
            raise IndexError("pilha igual minha conta bancária")
        return self._topo.valor

    def esta_vazia(self):
        #Retorna True se a pilha estiver vazia. Complexidade: O(1).
        return self._tamanho == 0

    def __len__(self):
        #Retorna o número de elementos armazenados. Complexidade: O(1).
        return self._tamanho

    def __repr__(self):
        #Representação textual legível, do topo para a base. Complexidade: O(N)
        elementos = []
        atual = self._topo
        while atual is not None:
            elementos.append(repr(atual.valor))
            atual = atual.proximo
        return f"PilhaEncadeada([{', '.join(elementos)}])"
