16/09
Nome: Manoel Felipe Macena de Azevedo  
Matrícula: 3524  
 
1. Distinção entre Tipo Abstrato de Dados (TAD) e Estrutura de Dados

  TDA uma especificação matemática/conceitual que define um conjunto de dados e as operações permitidas sobre eles (sua interface pública e comportamento esperado), sem se preocupar com os detalhes de armazenamento em memória. É a implementação concreta do TAD na memória do computador. Define como os dados são organizados, ponteiros/encadeamentos utilizados e como os algoritmos executam fisicamente as operações.

2. Justificativa da Complexidade Amortizada O(1) na Fila sobre Duas Pilhas

O Comportamento de desenfileirar() e frente():

* Toda operação enfileirar(item) insere diretamente na _pilha_entrada em tempo estritamente O(1).
* A remoção desenfileirar() consulta a _pilha_saida:
  * Se a _pilha_saida não estiver vazia, o elemento do topo é removido em tempo O(1).
  * Se a _pilha_saida estiver vazia, ocorre a transferência: todos os N elementos presentes na _pilha_entrada são removidos um a um e empilhados na _pilha_saida. Isso inverte a ordem dos elementos, preparando a _pilha_saida para saídas na ordem correta FIFO (First-In, First-Out).

Por que uma chamada isolada pode custar O(N)
Em uma chamada específica de desenfileirar(), se a _pilha_saida estiver vazia e houver N elementos acumulados na _pilha_entrada, a rotina de transferência executará N operações de pop() na entrada e $N$ operações de push() na saída. Logo, essa operação isolada terá custo de pior caso igual aO(N)

Por que a complexidade é O(1) Amortizada (Caso Médio)?
A análise amortizada avalia o custo médio por operação ao longo de uma sequência inteira de operações de vida de um elemento na estrutura.

Considere o ciclo de vida completo de um único elemento que passa pela fila:
1. É empilhado na _pilha_entrada durante o enfileirar() \rightarrow 1 operação de push
2. É desempilhado da _pilha_entrada durante a transferência \rightarrow 1 operação de pop.
3. É empilhado na _pilha_saida durante a transferência \rightarrow 1 operação de push
4. É desempilhado da _pilha_saida no desenfileirar() final \rightarrow 1 operação de pop.

Portanto, ao longo de toda a sua existência na fila, um elemento é manipulado por no máximo 4 operações fundamentais de pilha, todas de custo unitário O(1).

Para uma sequência de N inserções e N remoções, o custo total de todas as transferências e remoções combinadas é de exatamente 4N operações de pilha.

Como o custo total para processar $N$ elementos é diretamente proporcional a N, o custo médio repartido por operação é O(1) amortizado.