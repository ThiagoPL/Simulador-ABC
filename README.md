# Simulador-ABC

## Motivação

O simulador em questão está sendo desenvolvido para poder aprimorar o ABC para inferência de dinamica de miscigenação.

Testes realizados mostraram que o simulador utilizado previamente não fornecia bons resultados, sendo basicamente decidido pelo último pulso de miscigenação.

Nosso simulador se baseia nos operadores de AG para gerar uma população e permitir cruzamento entre os indivíduos, gerando uma opulação miscigenada


## Ideias para implementar
Modificação para cromossomos sexuais

Uso do mapa de recombinação para fazer os crossing over no nosso modelo

Acasalamento preferencial baseado na ancestralidade

## Decisões a serem tomadas 
Selecionaremos W indivíduos miscigenados de uma mesma corrida ou faremos corridas diferentes?

População aumentará de tamanho?

Fazer classe cromossomo para indivíduo?


## Implementados
Getopt no modelo do multipulses

Algoritmo para tamanho "fixo" implementado (ie, só cresce com migração)

Conversão vetor ao final da execução -> cM


## A implementar
Converter ID Getopt -> ID para posterior ID -> ID Getopt. (atualmente usamos 1,2 e 3 no get opt para representar AFR, EUR, NAT. Quero que usemos qualquer ID)
