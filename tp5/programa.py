import re
import json
import ply.lex as lex
from datetime import datetime

def verificar_data_hora():
    agora = datetime.now()
    return re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2})",str(agora)).group(0)



#stock = [
#{"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
#{"cod": "B34", "nome": "maca", "quant": 2, "preco": 1.2},
#{"cod": "A22", "nome": "qwerty", "quant": 9, "preco": 0.5},
#{"cod": "A76", "nome": "sumo", "quant": 1, "preco": 1.6}
#]  


tokens = (
   'LISTAR',
   'MOEDA',
   'SELECIONAR',
   'SAIR'
)

t_LISTAR = r'LISTAR'
#t_MOEDA = r'MOEDA\s+((\s*((1|2|5|10|20|50)c|\s*(1|2)e))+)'
#t_SELECIONAR = r'SELECIONAR\s([A-Z][0-9]{2})'
t_SAIR = r'SAIR'

def t_MOEDA(t):
    r'MOEDA\s+((\s*((1|2|5|10|20|50)c|\s*(1|2)e))+)'
    valores = re.findall(r'((1|2|5|10|20|50)c|(1|2)e)', t.value)
    t.value = [v[0] for v in valores]
    return t


def t_SELECIONAR(t):
    r'SELECIONAR\s([A-Z][0-9]{2})'
    t.value = re.match(r'SELECIONAR\s([A-Z][0-9]{2})', t.value).group(1)
    return t

t_ignore = " \t"

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()


with open('stock.json', 'r', encoding='utf-8') as f:
    stocking = json.load(f)

stock = stocking['stock']
print(f"{verificar_data_hora()}. Stock carregado, Estado atualizado.")
print("Bom dia. Estou disponível para atender o seu pedido.")


euros=0
centimos=0
dinheiro=0

linha = input(">>")
while(linha!="SAIR"):
    lexer.input(linha)
    for tok in lexer:
        if tok.type == 'LISTAR':
            print(" cod  |     nome     |  quantidade  | preço")
            print("============================================")
            for item in stock:
                print(f"{item['cod']:<5} | {item['nome']:<12} | {item['quant']:<12} | {item['preco']}")

        elif tok.type == 'MOEDA':
            for moeda in tok.value:
                m= re.compile(r'(\d+)(c|e)')
                if m.match(moeda).group(2) == 'c':
                    centimos += int(m.match(moeda).group(1))
                else:
                    euros += int(m.match(moeda).group(1))
            print(f"Saldo: {euros}e{centimos}c")
            dinheiro = euros*100 + centimos

        elif tok.type == 'SELECIONAR':
            codigo = tok.value
            encontrado = False
            for item in stock:
                if item['cod'] == codigo:
                    encontrado = True
                    if item['quant']>0:
                        if dinheiro >= item['preco']*100:
                            item['quant'] = item['quant'] - 1
                            dinheiro = dinheiro - item['preco']*100
                            euros = int(dinheiro // 100)
                            centimos = int(dinheiro % 100)
                            print(f"Pode retirar o produto dispensado: \"{item['nome']}\".\nSaldo: {euros}e{centimos}c")
                        else:
                            print("Saldo insuficiente")
                    else:
                        print("Produto esgotado")
            if encontrado==False:
                print("Produto não encontrado")
    linha = input(">>")

print("Pode retirar o troco:",end=' ')

for moeda in [200, 100]:
    numero_moedas = 0
    while dinheiro >= moeda:
        dinheiro -= moeda
        numero_moedas += 1
    if numero_moedas > 0:
        print(f"{numero_moedas}x {moeda//100}e", end=' ')

for moeda in [50, 20, 10, 5, 2, 1]:
    numero_moedas = 0
    while dinheiro >= moeda:
        dinheiro -= moeda
        numero_moedas += 1
    if numero_moedas > 0:
        print(f"{numero_moedas}x {moeda}c", end=' ')
print("\nAté à proxima")        

with open('stock.json', 'w', encoding='utf-8') as f:
    json.dump(stocking, f, indent=4)
