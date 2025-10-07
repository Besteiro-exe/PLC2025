
# Perfil:

![](../profile%20um.png)

Pedro Besteiro Silva

Mestrado em Engenharia Física

pg60422

# Resolução do TPC


[Resolução do TPC](./tpc2.py)

1. Para usar o programa, deve usar algum texto em markdown através de algum comando como por exemplo "cat texto.md|python3 ./tpc2.py".
2. O programa começa por usar re.compile() para guardar todas as expressões regulares necessárias para reconhecer as expressões em markdown. Usa-se então o sys.stdin para receber o texto linha a linha e aplicar as mudanças. No caso das expressões em itálico, negrito, imagens e URLs, é usada a função "re.sub()". Para os títulos, verifica a quantidade de cardinais e traduz isso no número da tag correspondente (&lt;h1>,&lt;h2>,&lt;h3>). Para as listas numeradas, usa-se o a variável counter para verificar se é o primeiro elemento da lista de forma a inserir a tag "&lt;ol>", e usa-se ainda a variável counter2 de para indicar se a linha que está prestes a ser imprimida é um elemento de uma lista. Caso ambas as variáveis se verifiquem positivas(=1), significa que acabou a lista a insere-se então a tag "&lt;/ol>" antes de imprimir a linha seguinte.




