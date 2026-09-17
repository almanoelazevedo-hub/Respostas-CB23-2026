'''
16/09
Nome: Manoel Felipe Macena de Azevedo  
Matrícula: 3524  
import unittest
'''

import unittest
from P06_3524_pilha_encadeada import PilhaEncadeada
from P06_3524_fila_encadeada import FilaEncadeada


class TestPilhaEncadeada(unittest.TestCase):

    def setUp(self):
        self.pilha = PilhaEncadeada()

    def test_ordem_lifo(self):
        """Verifica a ordem LIFO (Last-In, First-Out)."""
        elementos = [10, 20, 30, 40]
        for elem in elementos:
            self.pilha.push(elem)

        for elem in reversed(elementos):
            self.assertEqual(self.pilha.pop(), elem)

    def test_excecao_pilha_vazia(self):
        """Verifica se pop() e topo() levantam IndexError em pilha vazia."""
        with self.assertRaises(IndexError):
            self.pilha.pop()

        with self.assertRaises(IndexError):
            self.pilha.topo()

    def test_coerencia_len(self):
        """Verifica a coerência do contador len()."""
        self.assertEqual(len(self.pilha), 0)
        self.assertTrue(self.pilha.esta_vazia())

        self.pilha.push("A")
        self.pilha.push("B")
        self.assertEqual(len(self.pilha), 2)
        self.assertFalse(self.pilha.esta_vazia())

        self.pilha.pop()
        self.assertEqual(len(self.pilha), 1)

    def test_alternancia_operacoes(self):
        """Verifica o comportamento com inserções e remoções alternadas."""
        self.pilha.push(1)
        self.assertEqual(self.pilha.pop(), 1)
        self.pilha.push(2)
        self.pilha.push(3)
        self.assertEqual(self.pilha.topo(), 3)
        self.assertEqual(self.pilha.pop(), 3)
        self.assertEqual(self.pilha.pop(), 2)
        self.assertTrue(self.pilha.esta_vazia())

    def test_tipos_diversos_e_none(self):
        """Verifica suporte a tipos heterogêneos, repetições e None."""
        itens = [None, "texto", 3.14, None, [1, 2]]
        for item in itens:
            self.pilha.push(item)

        for item in reversed(itens):
            self.assertEqual(self.pilha.pop(), item)

    def test_repr_pilha(self):
        """Verifica a representação textual repr()."""
        self.pilha.push(1)
        self.pilha.push(2)
        self.assertEqual(repr(self.pilha), "PilhaEncadeada([2, 1])")


class TestFilaEncadeada(unittest.TestCase):

    def setUp(self):
        self.fila = FilaEncadeada()

    def test_ordem_fifo(self):
        """Verifica a ordem FIFO (First-In, First-Out)."""
        elementos = [100, 200, 300, 400]
        for elem in elementos:
            self.fila.enfileirar(elem)

        for elem in elementos:
            self.assertEqual(self.fila.desenfileirar(), elem)

    def test_excecao_fila_vazia(self):
        """Verifica se desenfileirar() e frente() levantam IndexError em fila vazia."""
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()

        with self.assertRaises(IndexError):
            self.fila.frente()

    def test_intercalacao_operacoes(self):
        """Verifica o correto funcionamento com inserções e remoções intercaladas."""
        self.fila.enfileirar("A")
        self.fila.enfileirar("B")
        self.assertEqual(self.fila.desenfileirar(), "A")

        self.fila.enfileirar("C")
        self.assertEqual(self.fila.frente(), "B")
        self.assertEqual(self.fila.desenfileirar(), "B")
        self.assertEqual(self.fila.desenfileirar(), "C")
        self.assertTrue(self.fila.esta_vazia())

    def test_esvaziar_e_reutilizar(self):
        """Verifica se a fila funciona corretamente após ser esvaziada e reutilizada."""
        self.fila.enfileirar(1)
        self.fila.desenfileirar()
        self.assertTrue(self.fila.esta_vazia())

        self.fila.enfileirar(2)
        self.assertEqual(len(self.fila), 1)
        self.assertEqual(self.fila.frente(), 2)
        self.assertEqual(self.fila.desenfileirar(), 2)

    def test_coerencia_len_fila(self):
        """Verifica a coerência do tamanho len()."""
        self.assertEqual(len(self.fila), 0)
        self.fila.enfileirar("X")
        self.fila.enfileirar("Y")
        self.assertEqual(len(self.fila), 2)
        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 1)

    def test_repr_fila(self):
        """Verifica a representação textual repr()."""
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.assertEqual(repr(self.fila), "FilaEncadeada([1, 2])")


if __name__ == "__main__":
    unittest.main()
