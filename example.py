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
program2 = """
PROGRAMA leitura de lista
INICIO
    { DECLARACOES }
    INTEIRO n, i, k, x
    LISTA_INT A[100]
    { ALGORITMO }
        { armazena os dados da lista }
    ESCREVA 'quantos números vai armazenar?'
    LEIA n
    x := 0
    k := 1
    ENQUANTO n .M. k
        LEIA A[k]
        x := x + A[k]
        k := k + 1
    FIM_ENQUANTO
        { escreve a lista de numeros }
    ESCREVA 'Numeros armazenados: '
    k := 1
    ENQUANTO n .M. k
        ESCREVA A[k], ' '
        k := k+1
    FIM-ENQUANTO
    ESCREVA ' soma dos valores armazenados = ' , x
FIM
"""
