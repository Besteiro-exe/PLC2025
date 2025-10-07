
import sys
import re

def tokenize(input_string,linha):
    reconhecidos = []
    mo = re.finditer(r'(?P<CA>\{)|(?P<CF>\})|(?P<SELECT>\bSELECT\b)|(?P<WHERE>\bWHERE\b)|(?P<variavel>\?\w+\b)|(?P<String>\w*:\w+\b)|(?P<PONTO>\.)|(?P<SKIP>[ \t])|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['CA']:
            t = ("CA", dic['CA'], linha, m.span())

        elif dic['CF']:
            t = ("CF", dic['CF'], linha, m.span())
    
        elif dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())
    
        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], linha, m.span())
    
        elif dic['variavel']:
            t = ("variavel", dic['variavel'], linha, m.span())
    
        elif dic['String']:
            t = ("String", dic['String'], linha, m.span())
    
        elif dic['PONTO']:
            t = ("PONTO", dic['PONTO'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

linhacounter=0
for linha in sys.stdin:
    linhacounter+=1
    for tok in tokenize(linha,linhacounter):
        print(tok)    

