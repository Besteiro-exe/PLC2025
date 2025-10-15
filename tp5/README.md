
# Perfil:

![](../profile%20um.png)

Pedro Besteiro Silva

Mestrado em Engenharia Física

pg60422

# Resolução do TPC


[Resolução do TPC](./programa.py)


1. Neste programa são declarados os tokens léxicos (LISTAR, MOEDA, SELECIONAR, SAIR) e suas expressões regulares correspondentes. As funções t_MOEDA() e t_SELECIONAR() utiliza expressões regulares para que o valor dos tokens reconhecidos sejam apenas as moedas e os códigos, respetivamente. O token t_error() lida com caracteres inválidos, e o lexer é criado através de lex.lex().
2. No ciclo while, o programa lê comandos do utilizador e usa o lexer para processá-los. Usa-se então o tok.type para ver os comandos e fazer as ações de LISTAR, MOEDA e SELECIONAR.
3. Quando a linha indicar SAIR, o ciclo termina e o programa calcula o troco com base nas moedas disponíveis, imprime a quantidade de cada uma e exibe uma mensagem final, começando das moedas maiores para as mais pequenas.
4. No início, o programa lê o ficheiro stock.json, armazena os dados na variável stock, e no final do programa coloca os dados da variável stock no stock.json, sendo que a única coisa que pode ser alterada é a quantidade dos produtos. 

