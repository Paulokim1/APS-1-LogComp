# APS-1-LogComp

```python
receita ::= "Receita:" titulo ingredientes passos
ingredientes ::= ingrediente*
ingrediente ::= "Ingrediente:" quantidade nome_ingrediente comentario?
quantidade ::= numero unidade
unidade ::= "g" | "kg" | "ml" | "L" | "colher de sopa" | "colher de chá"
nome_ingrediente ::= string
comentario ::= "(" string ")"
passos ::= passo*
passo ::= "Passo" numero ":" instrucao
numero ::= digito+
instrucao ::= string
string ::= '"' ([a-zA-Z0-9\s])* '"'
titulo ::= string
digito ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

Aqui, cada programa consiste em zero ou mais receitas. Cada receita começa com a palavra "Receita:" seguida de um título. Depois do título, pode haver zero ou mais ingredientes e zero ou mais passos. Cada ingrediente começa com a palavra "Ingrediente:", seguida da quantidade, nome do ingrediente e um comentário opcional. A quantidade é um número seguido de uma unidade, que pode ser "g", "kg", "ml", "L", "colher de sopa" ou "colher de chá". O nome do ingrediente é uma string. O comentário é uma string opcional entre parênteses. Cada passo começa com a palavra "Passo" seguida de um número e uma instrução que é uma string. O número é um inteiro. A string é delimitada por aspas duplas.

```python
G = (V, T, P, S)
```

```python
V = { programa, receita, titulo, ingrediente, quantidade, unidade, nome_ingrediente, comentario, passo, instrucao, numero, digito, string, letra }
T = { ":", "Ingrediente:", "Passo", "g", "kg", "ml", "L", "colher de sopa", "colher de chá", "\"", "(", ")" }
```

```python
P = {
programa -> receita programa | ε,
receita -> "Receita:" titulo ingredientes passos,
ingredientes -> ingrediente*,
ingrediente -> "Ingrediente:" quantidade nome_ingrediente comentario?,
quantidade -> numero unidade,
unidade -> "g" | "kg" | "ml" | "L" | "colher de sopa" | "colher de chá",
nome_ingrediente -> string,
comentario -> "(" string ")",
passos -> passo*,
passo -> "Passo" numero ":" instrucao,
instrucao -> string,
numero -> digito+,
digito -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9",
string -> "\"" (letra | digito | " ")* "\"",
letra -> "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
}
```

```python
S = programa
```

Nessa notação, **`V` r**epresenta o conjunto de símbolos não-terminais da gramática, **`T`** representa o conjunto de símbolos terminais da gramática, **`P`** representa as regras de produção da gramática e **`S`** é o símbolo inicial da gramática.