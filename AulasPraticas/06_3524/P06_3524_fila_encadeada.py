'''
16/09
Nome: Manoel Felipe Macena de Azevedo  
Matrícula: 3524  
import unittest
'''

from P06_3524_pilha_encadeada import PilhaEncadeada


class FilaEncadeada:
    def __init__(self):
        self._pilha_entrada = PilhaEncadeada()
        self._pilha_saida = PilhaEncadeada()

    def _transferir_se_necessario(self):
        #Transfere elementos da entrada para a saída apenas se a saída estiver vazia.
        if self._pilha_saida.esta_vazia():
            while not self._pilha_entrada.esta_vazia():
                self._pilha_saida.push(self._pilha_entrada.pop())

    def enfileirar(self, item):
        """Insere o item no fim da fila. Complexidade: O(1)."""
        self._pilha_entrada.push(item)

    def desenfileirar(self):
        #Remove e retorna o item da frente da fila. Complexidade: O(1) amortizada.
        if self.esta_vazia():
            raise IndexError("A fila está vazia. Não é possível remover elementos.")
        
        self._transferir_se_necessario()
        return self._pilha_saida.pop()

    def frente(self):
        #Retorna o item da frente sem removê-lo. Complexidade: O(1) amortizada.
        if self.esta_vazia():
            raise IndexError("A fila está vazia. Não é possível consultar a frente.")
        
        self._transferir_se_necessario()
        return self._pilha_saida.topo()

    def esta_vazia(self):
        #Retorna True se a fila estiver vazia. Complexidade: O(1).
        return self._pilha_entrada.esta_vazia() and self._pilha_saida.esta_vazia()

    def __len__(self):
        #Retorna o número total de elementos da fila. Complexidade: O(1).
        return len(self._pilha_entrada) + len(self._pilha_saida)

    def __repr__(self):
        #Representação textual legível, da frente para o fim. Complexidade: O(N).
        if self.esta_vazia():
            return "FilaEncadeada([])"

        elementos_frente_fim = []
        temp_saida = PilhaEncadeada()

        # Coleta os elementos da pilha de saída (já na ordem de saída / frente da fila)
        while not self._pilha_saida.esta_vazia():
            val = self._pilha_saida.pop()
            elementos_frente_fim.append(repr(val))
            temp_saida.push(val)

        # Restaura a pilha de saída
        while not temp_saida.esta_vazia():
            self._pilha_saida.push(temp_saida.pop())

        # Coleta os elementos da pilha de entrada na ordem da frente para o fim
        temp_entrada_inversao = PilhaEncadeada()
        temp_entrada_restauracao = PilhaEncadeada()

        while not self._pilha_entrada.esta_vazia():
            val = self._pilha_entrada.pop()
            temp_entrada_inversao.push(val)
            temp_entrada_restauracao.push(val)

        # Restaura a pilha de entrada
        while not temp_entrada_restauracao.esta_vazia():
            self._pilha_entrada.push(temp_entrada_restauracao.pop())

        # Adiciona elementos da entrada invertidos para manter a ordem FIFO
        while not temp_entrada_inversao.esta_vazia():
            elementos_frente_fim.append(repr(temp_entrada_inversao.pop()))

        return f"FilaEncadeada([{', '.join(elementos_frente_fim)}])"
