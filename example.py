program = """
PROGRAMA fatorial_exemplo
INICIO
    { DECLARACOES }
    INTEIRO argumento, fatorial
    { ALGORITMO }
    { Calcula o fatorial de um número inteiro }
    LEIA argumento
    fatorial := argumento
    SE argumento .I. 0
        ENTAO fatorial := 1
    FIM_SE
    ENQUANTO argumento .M. 1
        fatorial := fatorial * argumento
        argumento := argumento - 1
    FIM_ENQUANTO
    ESCREVA 'fatorial = ', fatorial
FIM 
"""
