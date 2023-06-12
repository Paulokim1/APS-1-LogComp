from SymbolTable import SymbolTable
from FuncTable import FuncTable


class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbol):
        pass


class NoOp(Node):
    pass


class IntVal(Node):
    def evaluate(self, symbol):
        return ("Int", int(self.value))


class StrVal(Node):
    def evaluate(self, symbol):
        return ("String", self.value.strip('"'))


class UnOp(Node):
    def evaluate(self, symbol):
        child = self.children[0].evaluate(symbol)
        if self.value == "-":
            return ("Int", -child[1])
        elif self.value == "+":
            return ("Int", child[1])
        elif self.value == "!":
            return ("Int", not child[1])
        raise Exception("Invalid expression")


class BinOp(Node):
    def evaluate(self, symbol):
        left = self.children[0].evaluate(symbol)
        right = self.children[1].evaluate(symbol)

        if self.value == "+":
            if (left[0] != "Int" or right[0] != "Int"):
                raise Exception(
                    "Cannot perform addition operation on non-integer values.")
            else:
                return ("Int", left[1] + right[1])
        elif self.value == "-":
            if (left[0] != "Int" or right[0] != "Int"):
                raise Exception(
                    "Cannot perform subtraction operation on non-integer values.")
            else:
                return ("Int", left[1] - right[1])
        elif self.value == "*":
            if (left[0] != "Int" or right[0] != "Int"):
                raise Exception(
                    "Cannot perform multiplication operation on non-integer values.")
            else:
                return ("Int", left[1] * right[1])
        elif self.value == "/":
            if (left[0] != "Int" or right[0] != "Int"):
                raise Exception(
                    "Cannot perform division operation on non-integer values.")
            else:
                return ("Int", left[1] // right[1])
        elif self.value == ".":
            return ("String", f"{left[1]}" + f"{right[1]}")
        elif self.value == "==":
            if (left[0] != right[0]):
                raise Exception(
                    "Cannot perform equality comparison on variables of different types.")
            else:
                if (left[1] == right[1]):
                    return ("Int", 1)
                else:
                    return ("Int", 0)
        elif self.value == ">":
            if (left[0] != right[0]):
                raise Exception(
                    "Cannot perform greater than comparison on variables of different types.")
            else:
                if (left[1] > right[1]):
                    return ("Int", 1)
                else:
                    return ("Int", 0)
        elif self.value == "<":
            if (left[0] != right[0]):
                raise Exception(
                    "Cannot perform less than comparison on variables of different types.")
            else:
                if (left[1] < right[1]):
                    return ("Int", 1)
                else:
                    return ("Int", 0)
        elif self.value == "||":
            if (left[1] or right[1]):
                return ("Int", 1)
            else:
                return ("Int", 0)
        elif self.value == "&&":
            if (left[1] and right[1]):
                return ("Int", 1)
            else:
                return ("Int", 0)


class Println(Node):
    def evaluate(self, symbol):
        child = self.children[0].evaluate(symbol)
        print(child[1])


class Readline(Node):
    def evaluate(self, symbol):
        return ("Int", int(input()))


class Block(Node):
    def evaluate(self, symbol):
        for child in self.children:
            if child.value == "return":
                return child.evaluate(symbol)
            else:
                child.evaluate(symbol)


class Identifier(Node):
    def evaluate(self, symbol):
        return symbol.getter(self.value)


class Assigment(Node):
    def evaluate(self, symbol):
        left = self.children[0]
        right = self.children[1].evaluate(symbol)
        symbol.setter(left.value, right[0], right[1])


class If(Node):
    def evaluate(self, symbol):
        if self.children[0].evaluate(symbol)[1] == 1:
            self.children[1].evaluate(symbol)
        elif len(self.children) > 2:
            self.children[2].evaluate(symbol)


class While(Node):
    def evaluate(self, symbol):
        while self.children[0].evaluate(symbol)[1] == 1:
            self.children[1].evaluate(symbol)


class VarDec(Node):
    def evaluate(self, symbol):
        left = self.children[0]
        if len(self.children) > 1:
            right = self.children[1]
            symbol.setter(
                left.value, self.value, right.evaluate(symbol)[1])
        else:
            if self.value == "Int":
                symbol.create(left.value, self.value, 0)
            elif self.value == "String":
                symbol.create(left.value, self.value, "")
            else:
                raise Exception("Invalid expression")


class FuncDec(Node):
    def evaluate(self, symbol):
        iden = self.children[0].value
        FuncTable.create(iden, self)


class FuncCall(Node):
    def evaluate(self, symbol):
        # Tem que ser duas vezes pq o primeiro é o identifier e o segundo é o valor do identifier
        func_name = self.value.value
        func_dec = FuncTable.getter(func_name)
        new_symbolTable = SymbolTable()
        for var_dec in func_dec.children[1]:
            var_dec.evaluate(new_symbolTable)
        for index, arg in enumerate(self.children):
            vars = list(new_symbolTable.table.keys())
            variable = arg.evaluate(symbol)
            new_symbolTable.setter(vars[index], variable[0], variable[1])
        return func_dec.children[2].evaluate(new_symbolTable)


class Return(Node):
    def evaluate(self, symbol):
        return (self.children[0].evaluate(symbol))
