15/09/2026
Nome: Manoel Felipe Macena de Azevedo
Matrícula: 3524

Questão 1

 É possível identificar três hierarquias pelas classes dadas:
 1- Indivíduos
  * Superclasse: Pessoa
   * Subclasse: Funcionário
   -Herda nome e idade e adiciona salário e carga horária
    * Sub²classe: Garçom, Chefe de cozinha e Gerente
    -Herda salário, carga horário e os atributos das classes superiores, nome e idae.
 Todo Garcom/chefe/gerente é funcionário e todo funcionário é uma pessoa. Comida não é nem chefe, nem funcionário e nem pessoa. Assim como os estabelecimentos
 2- Comida
  * Superclasse: Iguaria
   * Subclasse: Pizza
   ou
   * Subclasse: Bolo
 Todo bolo ou pizza herda nome e preço. Pizza adiciona borda recheada e bolo, formato.
 3- Estabelecimentos
  * Superclasse: Restaurante
   * Subclasse: Pizzaria
    -Herda nome, endereço e telefone, e adiciona rodízio
 Lembrando de esbalecimento não é comida e nem pessoa para ter hierarquia com eles.

Questão 2
 A relação entre restaurante e iguaria é do tipo agregação(de todo parte). A comida pode existir sem o restaurante, logo é independente. Para implementar, basta criar uma classe chamada cardápio que é subclasse de restaurante.

Questão 3
 O argumento 1 poderia ser do tipo cardápio, pois qualquer pedido feito pelo cliente vai estar no dicionário do cardápio. Entretanto o dicionário possui a iguaria como chave e o valor como preço, porém se o cliente quiser pedir uma quantidade específica, não funciona. Logo deve ser uma nova classe chamada pedido com a lista de iguarias, por exemplo, que agrupe as informações: mesa, cliente. Vai representar as iguarias escolhidas pelo cliente e suas quantidades. Um dicionário serviria.
 O argumento 2 deve ser o pedido, que é o que o chefe cuzinha.
 O argumento 3 Deve ser funcionário, pois só se demite funcionários.