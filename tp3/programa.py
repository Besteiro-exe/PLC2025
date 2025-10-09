
import sys
import re

def tokenize(input_string,linha):
    reconhecidos = []
    mo = re.finditer(r'(?P<CA>\{)|(?P<CF>\})|(?P<SELECT>SELECT|select)|(?P<WHERE>WHERE|where)|(?P<LIMIT>LIMIT|limit)|(?P<variavel>\?\w+)|(?P<idioma>@\w+)|(?P<String>"[\w ]+")|(?P<prefix_string>\w*:\w+)|(?P<PONTO>\.)|(?P<rdf_type>a)|(?P<INT>\d+)|(?P<SKIP>[ \t]|(?:^#.*?$))|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
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
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['variavel']:
            t = ("variavel", dic['variavel'], linha, m.span())
    
        elif dic['idioma']:
            t = ("idioma", dic['idioma'], linha, m.span())
    
        elif dic['String']:
            t = ("String", dic['String'], linha, m.span())
    
        elif dic['prefix_string']:
            t = ("prefix_string", dic['prefix_string'], linha, m.span())
    
        elif dic['PONTO']:
            t = ("PONTO", dic['PONTO'], linha, m.span())
    
        elif dic['rdf_type']:
            t = ("rdf_type", dic['rdf_type'], linha, m.span())
    
        elif dic['INT']:
            t = ("INT", dic['INT'], linha, m.span())
    
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
linhacounter=1
for linha in sys.stdin:
    for tok in tokenize(linha,linhacounter):
        print(tok)    
    linhacounter+=1

