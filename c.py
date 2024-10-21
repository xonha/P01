from a import lex_analyzer
from example import program


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    @property
    def token(self):
        return self.tokens[self.pos][0]

    @property
    def value(self):
        return self.tokens[self.pos][1]

    def eat(self, token_type):
        if self.pos < len(self.tokens) and self.token == token_type:
            self.pos += 1
        else:
            raise Exception(
                f"Esperado {token_type} na posição {self.pos}, mas encontrado {self.token}"
            )

    def parse(self):
        # <programa> ::= "PROGRAMA" <nome_do_programa> "INICIO" <corpo_do_programa> "FIM"
        self.eat("PROGRAMA")
        self.eat("IDENTIFICADOR")
        self.eat("INICIO")
        self.corpo_do_programa()
        self.eat("FIM")
        print("Programa válido")

    def corpo_do_programa(self):
        # <corpo_do_programa> ::= <declaracoes> <algoritmo>
        self.declaracoes()
        self.lista_comandos()

    def declaracoes(self):
        # <lista_declaracoes> ::= <declaracao> | <declaracao> <lista_declaracoes>
        self.declaracao()
        while self.token in (
            "INTEIRO",
            "REAL",
            "CARACTER",
            "CADEIA",
            "LISTA_INT",
            "LISTA_REAL",
        ):
            self.declaracao()

    def declaracao(self):
        # <declaracao> ::= <tipo> <identificador> [ "," <identificador> ]
        self.tipo()
        self.eat("IDENTIFICADOR")
        while self.token == "VIRGULA":
            self.eat("VIRGULA")
            self.eat("IDENTIFICADOR")

    def tipo(self):
        # <tipo> ::= "INTEIRO" | "REAL" | "CARACTER" | "CADEIA" | "LISTA_INT" "[" <numero> "]" | "LISTA_REAL" "[" <numero> "]"
        if self.token in ("INTEIRO", "REAL", "CARACTER", "CADEIA"):
            self.eat(self.token)
        elif self.token == "LISTA_INT":
            self.eat("LISTA_INT")
            self.eat("PARENTESE_ESQ")
            self.eat("NUMERO_INTEIRO")
            self.eat("PARENTESE_DIR")
        elif self.token == "LISTA_REAL":
            self.eat("LISTA_REAL")
            self.eat("PARENTESE_ESQ")
            self.eat("NUMERO_INTEIRO")
            self.eat("PARENTESE_DIR")
        else:
            raise Exception(
                f"Tipo inválido na posição {self.pos}, mas encontrado {self.token}"
            )

    def lista_comandos(self):
        # <lista_comandos> ::= <comando> | <comando> <lista_comandos>
        self.comando()
        while self.token in (
            "LEIA",
            "ESCREVA",
            "IDENTIFICADOR",
            "SE",
            "ENQUANTO",
        ):
            self.comando()

    def comando(self):
        # <comando> ::= <atribuicao> | <entrada> | <saida> | <selecao> | <repeticao>
        if self.token == "IDENTIFICADOR":
            self.atribuicao()
        elif self.token == "LEIA":
            self.entrada()
        elif self.token == "ESCREVA":
            self.saida()
        elif self.token == "SE":
            self.selecao()
        elif self.token == "ENQUANTO":
            self.repeticao()
        else:
            raise Exception(
                f"Comando inválido na posição {self.pos}, mas encontrado {self.token}"
            )

    def atribuicao(self):
        # <atribuicao> ::= <identificador> ":=" <expressao>
        self.eat("IDENTIFICADOR")
        self.eat("ATRIBUICAO")
        self.expressao()

    def entrada(self):
        # <entrada> ::= "LEIA" <identificador> [ "," <identificador> ]
        self.eat("LEIA")
        self.eat("IDENTIFICADOR")
        while self.token == "VIRGULA":
            self.eat("VIRGULA")
            self.eat("IDENTIFICADOR")

    def saida(self):
        # <saida> ::= "ESCREVA" <valor_escrever> [ "," <valor_escrever> ]
        self.eat("ESCREVA")
        self.eat("CADEIA_CARACTERES")
        while self.token == "VIRGULA":
            self.eat("VIRGULA")
            self.eat("IDENTIFICADOR")

    def selecao(self):
        # <selecao> ::= "SE" <expressao_relacional> "ENTAO" <lista_comandos> "FIM_SE"
        self.eat("SE")
        self.expressao_relacional()
        self.eat("ENTAO")
        self.lista_comandos()
        self.eat("FIM_SE")

    def repeticao(self):
        # <repeticao> ::= "ENQUANTO" <expressao_relacional> <lista_comandos> "FIM_ENQUANTO"
        self.eat("ENQUANTO")
        self.expressao_relacional()
        self.lista_comandos()
        self.eat("FIM_ENQUANTO")

    def expressao(self):
        # <expressao> ::= <termo> | <termo> "+" <expressao> | <termo> "-" <expressao>
        self.fator()
        while self.token == "OPERADOR_ARITMETICO":
            self.eat(self.token)
            self.expressao()

    def fator(self):
        # <fator> ::= <numero> | <identificador> | "(" <expressao> ")"
        if self.token in ("NUMERO_INTEIRO", "NUMERO_REAL"):
            self.eat(self.token)
        elif self.token == "IDENTIFICADOR":
            self.eat("IDENTIFICADOR")
        elif self.token == "PARENTESE_ESQ":
            self.eat("PARENTESE_ESQ")
            self.expressao()
            self.eat("PARENTESE_DIR")
        else:
            raise Exception(
                f"Fator inválido na posição {self.pos}, mas encontrado {self.token}"
            )

    def expressao_relacional(self):
        # <expressao_relacional> ::= <expressao> ".M." <expressao> | <expressao> ".I." <expressao>
        self.expressao()
        if self.token in ("MAIOR", "IGUAL"):
            self.eat(self.token)
            self.expressao()
        else:
            raise Exception(
                f"Operador relacional esperado na posição {self.pos}, mas encontrado {self.token}"
            )


tokens = lex_analyzer(program)
for i, token in enumerate(tokens):
    print(i, token)

parser = Parser(tokens).parse()
