from a import lex_analyzer
from example import program


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def eat(self, token_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == token_type:
            self.pos += 1
        else:
            raise Exception(
                f"Esperado {token_type} na posição {self.pos}, mas encontrado {self.tokens[self.pos][0]}"
            )

    def parse(self):
        self.programa()

    def programa(self):
        # <programa> ::= "PROGRAMA" <nome_do_programa> "INICIO" <corpo_do_programa> "FIM"
        self.eat("PROGRAMA")
        self.eat("IDENTIFICADOR")
        self.eat("INICIO")
        self.corpo_do_programa()
        self.eat("FIM")

    def corpo_do_programa(self):
        # <corpo_do_programa> ::= <declaracoes> <algoritmo>
        self.declaracoes()
        self.algoritmo()

    def declaracoes(self):
        # <declaracoes> ::= "DECLARACOES" <lista_declaracoes>
        self.lista_declaracoes()

    def lista_declaracoes(self):
        # <lista_declaracoes> ::= <declaracao> | <declaracao> <lista_declaracoes>
        self.declaracao()
        while self.tokens[self.pos][0] in (
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
        while self.tokens[self.pos][0] == "VIRGULA":
            self.eat("VIRGULA")
            self.eat("IDENTIFICADOR")

    def tipo(self):
        # <tipo> ::= "INTEIRO" | "REAL" | "CARACTER" | "CADEIA" | "LISTA_INT" "[" <numero> "]" | "LISTA_REAL" "[" <numero> "]"
        if self.tokens[self.pos][0] in ("INTEIRO", "REAL", "CARACTER", "CADEIA"):
            self.eat(self.tokens[self.pos][0])
        elif self.tokens[self.pos][0] == "LISTA_INT":
            self.eat("LISTA_INT")
            self.eat("PARENTESE_ESQ")
            self.eat("NUMERO_INTEIRO")
            self.eat("PARENTESE_DIR")
        elif self.tokens[self.pos][0] == "LISTA_REAL":
            self.eat("LISTA_REAL")
            self.eat("PARENTESE_ESQ")
            self.eat("NUMERO_INTEIRO")
            self.eat("PARENTESE_DIR")
        else:
            raise Exception(
                f"Tipo inválido na posição {self.pos}, mas encontrado {self.tokens[self.pos][0]}"
            )

    def algoritmo(self):
        # <algoritmo> ::= "ALGORITMO" <lista_comandos>
        self.lista_comandos()

    def lista_comandos(self):
        # <lista_comandos> ::= <comando> | <comando> <lista_comandos>
        self.comando()
        print(self.tokens[self.pos][0])
        while self.tokens[self.pos][0] in (
            "LEIA",
            "ESCREVA",
            "IDENTIFICADOR",
            "SE",
            "ENQUANTO",
        ):
            self.comando()

    def comando(self):
        # <comando> ::= <atribuicao> | <entrada> | <saida> | <selecao> | <repeticao>
        if self.tokens[self.pos][0] == "IDENTIFICADOR":
            self.atribuicao()
        elif self.tokens[self.pos][0] == "LEIA":
            self.entrada()
        elif self.tokens[self.pos][0] == "ESCREVA":
            self.saida()
        elif self.tokens[self.pos][0] == "SE":
            self.selecao()
        elif self.tokens[self.pos][0] == "ENQUANTO":
            self.repeticao()
        else:
            raise Exception(
                f"Comando inválido na posição {self.pos}, mas encontrado {self.tokens[self.pos][0]}"
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
        while self.tokens[self.pos][0] == "VIRGULA":
            self.eat("VIRGULA")
            self.eat("IDENTIFICADOR")

    def saida(self):
        # <saida> ::= "ESCREVA" <valor_escrever> [ "," <valor_escrever> ]
        self.eat("ESCREVA")
        self.valor_escrever()  # type: ignore
        while self.tokens[self.pos][0] == "VIRGULA":
            self.eat("VIRGULA")
            self.valor_escrever()  # type: ignore

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
        print("lista_comandos")
        self.lista_comandos()
        self.eat("FIM_ENQUANTO")

    def expressao(self):
        # <expressao> ::= <termo> | <termo> "+" <expressao> | <termo> "-" <expressao>
        self.termo()
        while self.tokens[self.pos][0] in ("+", "-"):
            self.eat(self.tokens[self.pos][0])
            self.expressao()

    def termo(self):
        # <termo> ::= <fator> | <fator> "*" <termo> | <fator> "/" <termo>
        self.fator()
        while self.tokens[self.pos][0] in ("*", "/"):
            self.eat(self.tokens[self.pos][0])
            self.termo()

    def fator(self):
        # <fator> ::= <numero> | <identificador> | "(" <expressao> ")"
        if self.tokens[self.pos][0] in ("NUMERO_INTEIRO", "NUMERO_REAL"):
            self.eat(self.tokens[self.pos][0])
        elif self.tokens[self.pos][0] == "IDENTIFICADOR":
            self.eat("IDENTIFICADOR")
        elif self.tokens[self.pos][0] == "PARENTESE_ESQ":
            self.eat("PARENTESE_ESQ")
            self.expressao()
            self.eat("PARENTESE_DIR")
        else:
            raise Exception(
                f"Fator inválido na posição {self.pos}, mas encontrado {self.tokens[self.pos][0]}"
            )

    def expressao_relacional(self):
        # <expressao_relacional> ::= <expressao> ".M." <expressao> | <expressao> ".I." <expressao>
        self.expressao()
        if self.tokens[self.pos][0] in ("MAIOR", "IGUAL"):
            self.eat(self.tokens[self.pos][0])
            self.expressao()
        else:
            raise Exception(
                f"Operador relacional esperado na posição {self.pos}, mas encontrado {self.tokens[self.pos][0]}"
            )


tokens = lex_analyzer(program)


for i, token in enumerate(tokens):
    print(i, token)

parser = Parser(tokens).parse()
