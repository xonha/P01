# Item B - Gramática e Estrutura de Árvore Sintática para CalcBasica

## 1. Gramática da Linguagem CalcBasica

Abaixo está a gramática da linguagem CalcBasica usando a notação BNF (Backus-Naur Form), conforme a descrição da linguagem fornecida no enunciado.

### 1.1 Programa

```
<programa> ::= "PROGRAMA" <nome_do_programa> "INICIO" <corpo_do_programa> "FIM"
<corpo_do_programa> ::= <declaracoes> <algoritmo>
```

### 1.2 Declarações de Variáveis

As variáveis podem ser declaradas de diferentes tipos. A área de declarações pode conter uma ou mais declarações:

```
<declaracoes> ::= "DECLARACOES" <lista_declaracoes>
<lista_declaracoes> ::= <declaracao> | <declaracao> <lista_declaracoes>
<declaracao> ::= <tipo> <identificador> [ "," <identificador> ]
<tipo> ::= "INTEIRO" | "REAL" | "CARACTER" | "CADEIA" | "LISTA_INT" "[" <numero> "]" | "LISTA_REAL" "[" <numero> "]"
```

### 1.3 Algoritmo

A área de algoritmo contém uma sequência de comandos:

```
<algoritmo> ::= "ALGORITMO" <lista_comandos>
<lista_comandos> ::= <comando> | <comando> <lista_comandos>
```

### 1.4 Comandos

Os comandos disponíveis incluem atribuição, entrada, saída, seleção condicional e repetição:

```
<comando> ::= <atribuicao> | <entrada> | <saida> | <selecao> | <repeticao>
```

#### Atribuição:

```
<atribuicao> ::= <identificador> ":=" <expressao>
```

#### Entrada:

```
<entrada> ::= "LEIA" <identificador> [ "," <identificador> ]
```

#### Saída:

```
<saida> ::= "ESCREVA" <valor_escrever> [ "," <valor_escrever> ]
<valor_escrever> ::= <identificador> | <cadeia_caracteres>
```

#### Seleção Condicional (SE):

```
<selecao> ::= "SE" <expressao_relacional> "ENTAO" <lista_comandos> "FIM_SE"
```

#### Repetição (ENQUANTO):

```
<repeticao> ::= "ENQUANTO" <expressao_relacional> <lista_comandos> "FIM_ENQUANTO"
```

### 1.5 Expressões

#### Expressão Aritmética:

```
<expressao> ::= <termo> | <termo> "+" <expressao> | <termo> "-" <expressao>
<termo> ::= <fator> | <fator> "*" <termo> | <fator> "/" <termo>
<fator> ::= <numero> | <identificador> | "(" <expressao> ")"
```

#### Expressão Relacional:

```
<expressao_relacional> ::= <expressao> ".M." <expressao> | <expressao> ".I." <expressao>
```

---

## 2. Estrutura de Árvore Sintática

A árvore sintática é uma representação hierárquica da estrutura do código com base na gramática. Abaixo está a estrutura de árvore sintática genérica para a linguagem CalcBasica.

### 2.1 Estrutura de Árvore para um Programa

No nível mais alto, temos o nó raiz representando o **programa**. O nó do programa possui subnós para o nome do programa, as **declarações** e o **algoritmo**:

```
Programa
├── Nome do Programa (ex: fatorial_exemplo)
├── Declarações
│   ├── Declaração (INTEIRO, argumento)
│   ├── Declaração (INTEIRO, fatorial)
├── Algoritmo
    ├── Comando: LEIA argumento
    ├── Comando: Atribuição (fatorial := argumento)
    ├── Seleção: SE (argumento .I. 0)
    │   ├── Comando: Atribuição (fatorial := 1)
    ├── Repetição: ENQUANTO (argumento .M. 1)
    │   ├── Comando: Atribuição (fatorial := fatorial * argumento)
    │   ├── Comando: Atribuição (argumento := argumento - 1)
    └── Comando: ESCREVA ('fatorial = ', fatorial)
```

### 2.2 Estrutura de Árvore para Declarações

A área de declarações é representada por um nó que agrupa todas as variáveis declaradas:

```
Declarações
├── Declaração (INTEIRO, var1)
├── Declaração (REAL, var2)
```

### 2.3 Estrutura de Árvore para Algoritmo e Comandos

Cada comando no algoritmo tem sua própria subárvore. Por exemplo, uma atribuição teria uma subárvore como esta:

```
Comando: Atribuição
├── Identificador (var1)
└── Expressão
    ├── Identificador (var2)
    └── Operador Aritmético (+)
        └── Número (10)
```

Para comandos condicionais e laços, a árvore inclui a condição e os comandos executados:

```
Comando: SE
├── Condição
│   ├── Identificador (var1)
│   └── Operador Relacional (.M.)
│       └── Número (100)
└── Comandos
    └── Comando: ESCREVA ('maior que 100')
```

### 2.4 Estrutura para Expressões

As expressões são subárvores que seguem a hierarquia de operadores:

```
Expressão
├── Termo
│   └── Identificador (var1)
├── Operador Aritmético (+)
└── Termo
    └── Número (5)
```

---

Essa gramática e árvore sintática definem a estrutura formal da linguagem CalcBasica e serão utilizadas pelo analisador sintático para verificar a correção estrutural de programas.
