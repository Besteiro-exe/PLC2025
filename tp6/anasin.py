from analex import lexer

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb is None:
       # fim da linha, épsilon
       return
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)



def rec_coisa():
    global prox_simb
    if prox_simb is None:
       # fim da linha, épsilon
       return    
    if prox_simb.type == 'NUM':
        print("Derivando por P2: coisa --> num op")
        rec_term('NUM')
        rec_op()
        print("Reconheci P2: coisa --> num op")
    elif prox_simb.type == 'PA':
        print("Derivando por P3: coisa --> '(' exp ')'")
        rec_term('PA')
        rec_exp()
        rec_term('PF')
        print("Reconheci P3: coisa --> '(' exp ')'")
    else:
        parserError(prox_simb)

def rec_op():
    global prox_simb
    if prox_simb is None:
        # fim da linha, épsilon
       return
    if prox_simb.type == 'SOMA':
        print("Derivando por P4: op --> '+' coisa")
        rec_term('SOMA')
        rec_coisa()
        print("Reconheci P4: op --> '+' coisa")
    elif prox_simb.type == 'MULT':
        print("Derivando por P5: op --> '*' coisa")
        rec_term('MULT')
        rec_coisa()
        print("Reconheci P5: op --> '*' coisa")
    elif prox_simb.type == 'DIV':
        print("Derivando por P6: op --> '/' coisa")
        rec_term('DIV')
        rec_coisa()
        print("Reconheci P6: op --> '/' coisa")
    elif prox_simb.type == 'SUB':
        print("Derivando por P7: op --> '-' coisa")
        rec_term('SUB')
        rec_coisa()
        print("Reconheci P7: op --> '-' coisa")
    else:
        print("Derivando por P8: op --> épsilon")
        print("Reconheci P8: op --> épsilon")


#p1:exp --> coisa op
#p2:coisa --> num op
#p3:        | '(' exp ')'
#p4:op --> '+' coisa
#p5:     | '*' coisa
#p6:     | '/' coisa
#p7:     | '-' coisa
#p8:     | épsilon


def rec_exp():
    global prox_simb
    print("Derivando por P1: exp --> '(' coisa ')' op")
    rec_term('PA')
    rec_coisa()
    rec_term('PF')
    rec_op()
    print("Reconheci P1: exp --> coisa op")



def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_exp()
    print("That's all folks!")





