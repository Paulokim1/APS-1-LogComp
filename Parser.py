from Tokenizer import Tokenizer
from PrePro import PrePro
from Nodes import *

# Variáveis globais
reserved = ["IMPRIMA", "SE", "SENAO", "ENQUANTO", "FIM", "INTEIRO", "CARACTERES", "FUNCAO", "RETORNE"]

class Parser:
    def __init__(self):
        self.tokenizer = None

    def parseBlock(self):
        children = []
        while self.tokenizer.next.type != "EOF":
            children.append(self.parseStatement())
        return Block(None, children)

    def parseStatement(self):
        if self.tokenizer.next.type == "SPACE":
            self.tokenizer.selectNext()
            return NoOp(None, [])
        elif self.tokenizer.next.type == "IDEN":
            iden = Identifier(self.tokenizer.next.value, [])
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "ASSIGN":
                self.tokenizer.selectNext()
                value = self.parseRelExpression()
                return Assigment(None, [iden, value])
            elif self.tokenizer.next.type == "TYPEAS":
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == "TYPE":
                    var_type = self.tokenizer.next.value
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == "ASSIGN":
                        self.tokenizer.selectNext()
                        value = self.parseRelExpression()
                        return VarDec(var_type, [iden, value])
                    elif self.tokenizer.next.type == "SPACE":
                        return VarDec(var_type, [iden])
                    else:
                        raise Exception("Invalid statement")
                else:
                    raise Exception("Invalid type")
            elif self.tokenizer.next.type == "LPAREN":
                self.tokenizer.selectNext()
                func_args = []
                while self.tokenizer.next.type != "RPAREN":
                    func_args.append(self.parseRelExpression())
                    if self.tokenizer.next.type != "COMMA":
                        if self.tokenizer.next.type == "RPAREN":
                            self.tokenizer.selectNext()
                            break
                        else:
                            raise Exception("Missing ','")
                    self.tokenizer.selectNext()
                return FuncCall(iden, func_args)
            else:
                raise Exception("Invalid statement")
        elif self.tokenizer.next.type == "RETORNE":
            self.tokenizer.selectNext()
            value = self.parseRelExpression()
            return Return("return", [value])
        elif self.tokenizer.next.type == "IMPRIMA":
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "LPAREN":
                self.tokenizer.selectNext()
                value = self.parseRelExpression()
                if self.tokenizer.next.type == "RPAREN":
                    self.tokenizer.selectNext()
                    return Println(None, [value])
                else:
                    raise Exception("Missing ')'")
            else:
                raise Exception("Missing '('")
        elif self.tokenizer.next.type == "ENQUANTO":
            self.tokenizer.selectNext()
            condition = self.parseRelExpression()
            if self.tokenizer.next.type == "SPACE":
                blocks = []
                self.tokenizer.selectNext()
                while self.tokenizer.next.type != "FIM":
                    blocks.append(self.parseStatement())
                self.tokenizer.selectNext()
                return While(None, [condition, Block(None, blocks)])
            else:
                raise Exception("Missing 'end'")
        elif self.tokenizer.next.type == "SE":
            self.tokenizer.selectNext()
            condition = self.parseRelExpression()
            if self.tokenizer.next.type == "SPACE":
                blocks = []
                self.tokenizer.selectNext()
                while self.tokenizer.next.type != "FIM" and self.tokenizer.next.type != "SENAO":
                    blocks.append(self.parseStatement())
                if self.tokenizer.next.type == "SENAO":
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == "SPACE":
                        self.tokenizer.selectNext()
                        elseBlocks = []
                        while self.tokenizer.next.type != "FIM":
                            elseBlocks.append(self.parseStatement())
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.type == "SPACE" or self.tokenizer.next.type == "EOF":
                            self.tokenizer.selectNext()
                            return If(None, [condition, Block(None, blocks), Block(None, elseBlocks)])
                    else:
                        raise Exception("Missing 'end'")
                elif self.tokenizer.next.type == "SPACE":
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == "FIM":
                        self.tokenizer.selectNext()
                        return If(None, [condition, Block(None, blocks)])
                    else:
                        raise Exception("Missing 'end'")
                elif self.tokenizer.next.type == "FIM":
                    self.tokenizer.selectNext()
                    return If(None, [condition, Block(None, blocks)])
                else:
                    raise Exception("Missing 'end'")
        elif self.tokenizer.next.type == "FUNCAO":
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "IDEN":
                func_name = Identifier(self.tokenizer.next.value, [])
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == "LPAREN":
                    self.tokenizer.selectNext()
                    func_args = []
                    while self.tokenizer.next.type != "RPAREN":
                        if self.tokenizer.next.type == "IDEN":
                            iden = Identifier(self.tokenizer.next.value, [])
                            self.tokenizer.selectNext()
                            if self.tokenizer.next.type == "TYPEAS":
                                self.tokenizer.selectNext()
                                if self.tokenizer.next.type == "TYPE":
                                    var_type = self.tokenizer.next.value
                                    func_args.append(VarDec(var_type, [iden]))
                                    self.tokenizer.selectNext()
                                    if self.tokenizer.next.type != "COMMA":
                                        if self.tokenizer.next.type == "RPAREN":
                                            self.tokenizer.selectNext()
                                            break
                                        else:
                                            raise Exception("Missing ','")
                                    self.tokenizer.selectNext()
                                else:
                                    raise Exception("Invalid type")
                            else:
                                raise Exception("Missing ::")
                        else:
                            raise Exception("Invalid identifier")
                else:
                    raise Exception("Missing '('") 
                if self.tokenizer.next.type == "RPAREN":
                    self.tokenizer.selectNext()
                if self.tokenizer.next.type == "TYPEAS":
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == "TYPE":
                        func_type = self.tokenizer.next.value
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.type == "SPACE":
                            self.tokenizer.selectNext()
                            blocks = []
                            while self.tokenizer.next.type != "FIM":
                                blocks.append(self.parseStatement())
                            self.tokenizer.selectNext()
                            if self.tokenizer.next.type == "SPACE" or self.tokenizer.next.type == "EOF":
                                self.tokenizer.selectNext()
                                return FuncDec(func_type, [func_name, func_args, Block(None, blocks)])
                        else:
                            raise Exception("Missing 'end'")
                    else:
                        raise Exception("Invalid type")
                else:
                    raise Exception("Missing ::")
        else:
            raise Exception("Invalid statement")

    def parseRelExpression(self):
        result = self.parseExpression()
        while self.tokenizer.next.type == "EQUAL" or self.tokenizer.next.type == "GREATER" or self.tokenizer.next.type == "LESS" or self.tokenizer.next.type == "CONCAT":
            if self.tokenizer.next.type == "EQUAL":
                self.tokenizer.selectNext()
                result = BinOp("==", [result, self.parseExpression()])
            elif self.tokenizer.next.type == "GREATER":
                self.tokenizer.selectNext()
                result = BinOp(">", [result, self.parseExpression()])
            elif self.tokenizer.next.type == "LESS":
                self.tokenizer.selectNext()
                result = BinOp("<", [result, self.parseExpression()])
            elif self.tokenizer.next.type == "CONCAT":
                self.tokenizer.selectNext()
                result = BinOp(".", [result, self.parseExpression()])
            else:
                raise Exception("Invalid expression")
        return result

    def parseExpression(self):
        result = self.parseTerm()
        while self.tokenizer.next.type == "PLUS" or self.tokenizer.next.type == "MINUS" or self.tokenizer.next.type == "OR":
            if self.tokenizer.next.type == "PLUS":
                self.tokenizer.selectNext()
                result = BinOp("+", [result, self.parseTerm()])
            elif self.tokenizer.next.type == "MINUS":
                self.tokenizer.selectNext()
                result = BinOp("-", [result, self.parseTerm()])
            elif self.tokenizer.next.type == "OR":
                self.tokenizer.selectNext()
                result = BinOp("||", [result, self.parseTerm()])
            else:
                raise Exception("Invalid expression")
        return result

    def parseTerm(self):
        result = self.parseFactor()
        while self.tokenizer.next.type == "MULT" or self.tokenizer.next.type == "DIV" or self.tokenizer.next.type == "AND":
            if self.tokenizer.next.type == "MULT":
                self.tokenizer.selectNext()
                result = BinOp("*", [result, self.parseFactor()])
            elif self.tokenizer.next.type == "DIV":
                self.tokenizer.selectNext()
                result = BinOp("/", [result, self.parseFactor()])
            elif self.tokenizer.next.type == "AND":
                self.tokenizer.selectNext()
                result = BinOp("&&", [result, self.parseFactor()])
            else:
                raise Exception("Invalid expression")
        return result

    def parseFactor(self):
        result = 0
        if self.tokenizer.next.type == "INT":
            result = IntVal(self.tokenizer.next.value, [])
            self.tokenizer.selectNext()
        elif self.tokenizer.next.type == "STRING":
            result = StrVal(self.tokenizer.next.value, [])
            self.tokenizer.selectNext()
        elif self.tokenizer.next.type == "MINUS":
            self.tokenizer.selectNext()
            result = UnOp("-", [self.parseFactor()])
        elif self.tokenizer.next.type == "PLUS":
            self.tokenizer.selectNext()
            result = UnOp("+", [self.parseFactor()])
        elif self.tokenizer.next.type == "NOT":
            self.tokenizer.selectNext()
            result = UnOp("!", [self.parseFactor()])
        elif self.tokenizer.next.type == "LPAREN":
            self.tokenizer.selectNext()
            temp = self.parseRelExpression()
            if self.tokenizer.next.type == "RPAREN":
                self.tokenizer.selectNext()
                return temp
            else:
                raise Exception("Missing ')'")
        elif self.tokenizer.next.type == "IDEN":
            if self.tokenizer.next.value in reserved:
                raise Exception(
                    "Reserved word cannot be used as an identifier")
            result = Identifier(self.tokenizer.next.value, [])
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "LPAREN":
                self.tokenizer.selectNext()
                args = []
                while self.tokenizer.next.type != "RPAREN":
                    args.append(self.parseRelExpression())
                    if self.tokenizer.next.type == "COMMA":
                        self.tokenizer.selectNext()
                self.tokenizer.selectNext()
                return FuncCall(result, args)
        else:
            raise Exception("Invalid factor")
        return result

    def run(self, code):
        code_no_comments = PrePro.filter(code)
        self.tokenizer = Tokenizer(code_no_comments)
        self.tokenizer.selectNext()
        result = self.parseBlock()

        if self.tokenizer.next.type != "EOF":
            raise Exception("Invalid expression")
        return result