
# Perfil:

![](../profile%20um.png)

Pedro Besteiro Silva

Mestrado em Engenharia Física

pg60422

# Resolução do TPC


[Programa a correr](./programa.py)
[analisador léxico](./analex.py)
[enalisador sintático](./anasin.py)

1. Este código é um analisador sintático recursivo descendente que verifica se uma expressão matemática está escrita corretamente de acordo com uma gramática pré-definida. è usado um analisador léxico (lexer) para ler os tokens da expressão (como números, operadores e parênteses).
2. O parser usa funções recursivas para reconhecer partes da expressão: números, operadores e subexpressões entre parênteses. Cada função representa uma regra da gramática, e o programa mostra a regra a ser aplicada.
3. Se a expressão estiver correta, o parser percorre tudo até o final; caso contrário, exibe uma mensagem de erro sintático, indicando que a sequência de tokens não segue as regras esperadas.

