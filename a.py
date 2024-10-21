import re

from example import program

tokens = [
    ("PROGRAMA", r"PROGRAMA"),
    ("INICIO", r"INICIO"),
    ("FIM_SE", r"FIM_SE"),
    ("FIM_ENQUANTO", r"FIM_ENQUANTO"),
    ("FIM", r"FIM"),
    ("DECLARACOES", r"DECLARACOES"),
    ("ALGORITMO", r"ALGORITMO"),
    ("INTEIRO", r"INTEIRO"),
    ("REAL", r"REAL"),
    ("CARACTER", r"CARACTER"),
    ("CADEIA", r"CADEIA"),
    ("LISTA_INT", r"LISTA_INT"),
    ("LISTA_REAL", r"LISTA_REAL"),
    ("LEIA", r"LEIA"),
    ("ESCREVA", r"ESCREVA"),
    ("SE", r"SE"),
    ("ENTAO", r"ENTAO"),
    ("ENQUANTO", r"ENQUANTO"),
    ("ATRIBUICAO", r":="),
    ("MAIOR", r"\.M\."),
    ("IGUAL", r"\.I\."),
    ("NUMERO_INTEIRO", r"\d+"),
    ("NUMERO_REAL", r"\d+\.\d+"),
    ("IDENTIFICADOR", r"[A-Za-z_]\w*"),
    ("OPERADOR_ARITMETICO", r"[+\-*/]"),
    ("PARENTESE_ESQ", r"\("),
    ("PARENTESE_DIR", r"\)"),
    ("VIRGULA", r","),
    ("CADEIA_CARACTERES", r"'[^']*'"),
    ("COMENTARIO", r"\{[^}]*\}"),
    ("NOVALINHA", r"\n"),
    ("ESPACO", r"[ \t]+"),
]

token_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in tokens)


def lex_analyzer(code):
    tokens = []
    line_num = 0
    line_start = 0
    pos = 0
    while pos < len(code):
        match = re.match(token_regex, code[pos:])
        if match:
            token_type = match.lastgroup
            token_value = match.group(token_type)  # type: ignore
            if token_type == "NOVALINHA":
                line_num += 1
                line_start = pos + len(token_value)
            elif token_type != "ESPACO" and token_type != "COMENTARIO":
                column = pos - line_start
                tokens.append((token_type, token_value, line_num, column))
            pos += len(token_value)
        else:
            column = pos - line_start
            raise Exception(
                f"Erro léxico na linha {line_num}, coluna {column}: '{code[pos]}'"
            )
    return tokens


if __name__ == "__main__":
    tokens = lex_analyzer(program)
    for i, token in enumerate(tokens):
        print(i, token)
