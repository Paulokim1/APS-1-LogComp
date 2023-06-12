from Token import Token
import re

# Variáveis globais
reserved = ["IMPRIMA", "SE", "SENAO", "ENQUANTO", "FIM", "INTEIRO", "CARACTERES", "FUNCAO", "RETORNE"]


class Tokenizer:
    def __init__(self, source):
        self.source = re.findall(
            r'\b\w+\b|==|\|\||&&|::|,|[^\s\w()+\-*/"]|(?<=\d)[-+*/](?=\d)|\n|"[^"\n]*"|\'[^\n\']*\'|[^\w\s]', source)
        #print(self.source)
        self.position = 0

    def selectNext(self):
        allowed_variables = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')
        if self.position < len(self.source):
            if self.source[self.position].isdigit():
                self.next = Token("INT", self.source[self.position])
            elif self.source[self.position][0] == '"' and self.source[self.position][-1] == '"':
                self.next = Token("STRING", self.source[self.position])
            elif self.source[self.position] == "MAIS":
                self.next = Token("PLUS", "+")
            elif self.source[self.position] == "MENOS":
                self.next = Token("MINUS", "-")
            elif self.source[self.position] == "MULTIPLICADO":
                self.next = Token("MULT", "*")
            elif self.source[self.position] == "DIVIDIDO":
                self.next = Token("DIV", "/")
            elif self.source[self.position] == "{":
                self.next = Token("LPAREN", "(")
            elif self.source[self.position] == "}":
                self.next = Token("RPAREN", ")")
            elif self.source[self.position] == "IGUAL":
                self.next = Token("ASSIGN", "=")
            elif self.source[self.position] == "\n":
                self.next = Token("SPACE", "\n")
            elif self.source[self.position] == "IDENTICO":
                self.next = Token("EQUAL", "==")
            elif self.source[self.position] == "MAIOR":
                self.next = Token("GREATER", ">")
            elif self.source[self.position] == "MENOR":
                self.next = Token("LESS", "<")
            elif self.source[self.position] == "OU":
                self.next = Token("OR", "||")
            elif self.source[self.position] == "E":
                self.next = Token("AND", "&&")
            elif self.source[self.position] == "CONTRARIO":
                self.next = Token("NOT", "!")
            elif self.source[self.position] == "COMO":
                self.next = Token("TYPEAS", "::")
            elif self.source[self.position] == ",":
                self.next = Token("COMMA", ",")
            elif self.source[self.position] in reserved:
                if self.source[self.position] == "INTEIRO" or self.source[self.position] == "CARACTERES":
                    if self.source[self.position] == "INTEIRO": 
                        type = "Int"
                    else:
                        type = "String"
                    self.next = Token("TYPE", type)
                else:
                    self.next = Token(
                        self.source[self.position].upper(), self.source[self.position])
            elif allowed_variables.match(self.source[self.position]) and self.source[self.position] not in reserved:
                self.next = Token("IDEN", self.source[self.position])
            self.position += 1
        else:
            self.next = Token("EOF", None)
