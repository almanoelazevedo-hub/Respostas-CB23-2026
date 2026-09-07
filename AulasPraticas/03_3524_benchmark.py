"""
Atividade Prática - Aula 3 (17/08)
Aluno: Manoel Felipe Macena de Azevedo / 3524
"""
import time
import random
import sys
import AP_03_ordenacao as ap3
sys.setrecursionlimit(5000)
#Funções Auxiliares

def caso_medio(n):
    #Lista aleatória 
    return [random.randint(-100000, 100000) for _ in range(n)]

def pior_caso(n, m="nothing"):
    #Lista em ordem decrescente ou no caso do quicksort, cria a lista normal para dificultar as divisões
    if m == "quick_sort":
        return list(range(n))
    else:
        return list(range(n, 0, -1))

#Casos a serem testatos, variáveis para os tempos dos algorítimos e dicionário para armazenar
testes = [100, 500, 1000]

tempos_totais = {
    ("Selection Sort", "Caso Médio"): 0.0,
    ("Selection Sort", "Pior Caso"): 0.0,
    ("Merge Sort", "Caso Médio"): 0.0,
    ("Merge Sort", "Pior Caso"): 0.0,
    ("Quick Sort", "Caso Médio"): 0.0,
    ("Quick Sort", "Pior Caso"): 0.0,
}

#Crianda a tabela para o caso n
print(f"\nResultados para 50 execuções:")
print("-" * 67)
print(f"{'Algoritmo':<18} | {'Cenário':<12} | {'Tempo Médio (s)':<18} | {'N':<8} |")
print("-" * 67)
for i in testes:
    #Reiniciando os tempos da tabela
    for chave in tempos_totais:
        tempos_totais[chave] = 0.0
    for _ in range(50):
        #criando as listas
        casomed=caso_medio(i)
        piorcaso= pior_caso(i)
        piocasoquicksort= pior_caso(i, "quick_sort")

        #testando os tempos pro selectionsort
        #caso médio
        um= time.perf_counter()
        ap3.selection_sort(casomed.copy())
        tempos_totais[("Selection Sort", "Caso Médio")] += time.perf_counter() - um
        #caso ruim
        um= time.perf_counter()
        ap3.selection_sort(piorcaso.copy())
        tempos_totais[("Selection Sort", "Pior Caso")] += time.perf_counter() - um

        #testando os tempos pro divide and conquer sort que também é chamado de merge sort
        #caso médio
        um= time.perf_counter()
        ap3.divide_and_conquer_sort(casomed.copy())
        tempos_totais[("Merge Sort", "Caso Médio")] += time.perf_counter() - um
        #caso ruim
        um= time.perf_counter()
        ap3.divide_and_conquer_sort(piorcaso.copy())
        tempos_totais[("Merge Sort", "Pior Caso")] += time.perf_counter() - um

        #testando os tempos pro quick sort
        #caso médio
        um= time.perf_counter()
        ap3.quick_sort(casomed.copy())
        tempos_totais[("Quick Sort", "Caso Médio")] += time.perf_counter() - um
        #caso ruim
        um= time.perf_counter()
        ap3.quick_sort(piorcaso.copy())
        tempos_totais[("Quick Sort", "Pior Caso")] += time.perf_counter() - um

    for alg in ["Selection Sort", "Merge Sort", "Quick Sort"]:
        for cenario in ["Caso Médio", "Pior Caso"]:
            t_medio = tempos_totais[(alg, cenario)] / 50
            print(f"{alg:<18} | {cenario:<12} | {t_medio:.6f} s         | {i:<8} |")
    print("-" * 67)