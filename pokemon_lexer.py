
from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Tokens
        self.lexer.add("NEWLINE", r'\n')
        self.lexer.add("TRAINER", r'Red|Blue|Green')
        self.lexer.add("CHOSE", r'chose')
        self.lexer.add("AS", r'as')
        self.lexer.add("POKEMON", r'Charmander|Squirtle|Bulbasaur')
        self.lexer.add("STATS_DECLARATION", r'stats:')
        self.lexer.add("STAT", r'Level|HP|AS|DS')
        self.lexer.add("ASSIGN", r'=')
        self.lexer.add("VALUE", r'\d+')
        self.lexer.add("WHILE", r'while')
        self.lexer.add("CONDITION", r'\(|\)')
        self.lexer.add("GREATER_THAN", r'>')
        self.lexer.add("LESS_THAN", r'<')
        self.lexer.add("OR", r'or')
        self.lexer.add("COLON", r':')
        self.lexer.add("USE", r'use')
        self.lexer.add("ATTACK", r'Scratch|Tail Whip|Water Gun')
        self.lexer.add("DOT", r'\.')
        self.lexer.add("EXCLAMATION", r'!')

        # Ignore spaces
        self.lexer.ignore(r'[ \t]+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()   
