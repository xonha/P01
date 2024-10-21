# 2018003703 - HENRIQUE CASTRO OLIVEIRA
# 2018005655 - WALDOMIRO BARBOSA ROMÃO

from a import lex_analyzer
from example import program_00, program_01, program_02


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
        self.eat("PROGRAMA")
        while self.token == "IDENTIFICADOR":
            self.eat(self.token)
        self.eat("INICIO")
        self.corpo_do_programa()
        self.eat("FIM")
        print("Programa válido")

    def corpo_do_programa(self):
        self.declaracoes()
        self.lista_comandos()

    def declaracoes(self):
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
        if self.token in ("INTEIRO", "REAL", "CARACTER", "CADEIA"):
            self.eat(self.token)
            self.eat("IDENTIFICADOR")
            while self.token == "VIRGULA":
                self.eat("VIRGULA")
                self.eat("IDENTIFICADOR")
        elif self.token == "LISTA_INT":
            self.eat("LISTA_INT")
            self.eat("IDENTIFICADOR")
            self.eat("COLCHETE_ESQ")
            self.eat("NUMERO_INTEIRO")
            self.eat("COLCHETE_DIR")
        elif self.token == "LISTA_REAL":
            self.eat("LISTA_REAL")
            self.eat("IDENTIFICADOR")
            self.eat("COLCHETE_ESQ")
            self.eat("NUMERO_INTEIRO")
            self.eat("COLCHETE_DIR")
        else:
            raise Exception(
                f"Tipo inválido na posição {self.pos}, mas encontrado {self.token}"
            )

    def lista_comandos(self):
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
        self.eat("IDENTIFICADOR")
        self.eat("ATRIBUICAO")
        self.expressao()

    def entrada(self):
        self.eat("LEIA")
        self.identificador_ou_array()
        while self.token == "VIRGULA":
            self.eat("VIRGULA")
            self.identificador_ou_array()

    def identificador_ou_array(self):
        self.eat("IDENTIFICADOR")
        if self.token == "COLCHETE_ESQ":
            self.eat("COLCHETE_ESQ")
            self.eat("IDENTIFICADOR")
            self.eat("COLCHETE_DIR")

    def saida(self):
        self.eat("ESCREVA")
        if self.token == "CADEIA_CARACTERES":
            self.eat("CADEIA_CARACTERES")
        elif self.token == "IDENTIFICADOR":
            self.identificador_ou_array()
        while self.token == "VIRGULA":
            self.eat("VIRGULA")
            if self.token == "CADEIA_CARACTERES":
                self.eat("CADEIA_CARACTERES")
            elif self.token == "IDENTIFICADOR":
                self.identificador_ou_array()

    def selecao(self):
        self.eat("SE")
        self.expressao_relacional()
        self.eat("ENTAO")
        self.lista_comandos()
        self.eat("FIM_SE")

    def repeticao(self):
        self.eat("ENQUANTO")
        self.expressao_relacional()
        self.lista_comandos()
        self.eat("FIM_ENQUANTO")

    def expressao(self):
        self.fator()
        while self.token == "OPERADOR_ARITMETICO":
            self.eat(self.token)
            self.expressao()

    def fator(self):
        if self.token in ("NUMERO_INTEIRO", "NUMERO_REAL"):
            self.eat(self.token)
        elif self.token == "IDENTIFICADOR":
            self.identificador_ou_array()
        elif self.token == "COLCHETE_ESQ":
            self.eat("COLCHETE_ESQ")
            self.expressao()
            self.eat("COLCHETE_DIR")
        else:
            raise Exception(
                f"Fator inválido na posição {self.pos}, mas encontrado {self.token}"
            )

    def expressao_relacional(self):
        self.expressao()
        if self.token in ("MAIOR", "IGUAL"):
            self.eat(self.token)
            self.expressao()
        else:
            raise Exception(
                f"Operador relacional esperado na posição {self.pos}, mas encontrado {self.token}"
            )


if __name__ == "__main__":
    tokens_00 = lex_analyzer(program_00)
    for i, token in enumerate(tokens_00):
        print(i, token)
    parser = Parser(tokens_00).parse()

    tokens_01 = lex_analyzer(program_01)
    for i, token in enumerate(tokens_01):
        print(i, token)
    parser = Parser(tokens_01).parse()

    tokens_02 = lex_analyzer(program_02)
    for i, token in enumerate(tokens_02):
        print(i, token)
    parser = Parser(tokens_02).parse()
