import sys
from Parser import Parser
from SymbolTable import SymbolTable


def main():
    #src = open(sys.argv[1]).read()
    src = open("test.txt").read()
    parser = Parser()
    parser.run(src).evaluate(SymbolTable())


if __name__ == "__main__":
    main()
