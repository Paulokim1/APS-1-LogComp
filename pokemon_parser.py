from rply import ParserGenerator

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names, accepted by the parser.
            ['START', 'TRAINER', 'CHOSE', 'POKEMON', 'STATS_DECLARATION', 'STAT', 'ASSIGN', 'VALUE', 
            'WHILE', 'GREATER_THAN', 'OR', 'USE', 'ATTACK', 'DOT', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LAST']
        )

    def parse(self):
        @self.pg.production('program : START player stats battle LAST')
        def program(p):
            return p
        
        @self.pg.production('player : TRAINER CHOSE POKEMON player')
        @self.pg.production('player : TRAINER CHOSE POKEMON')
        def player(p):
            return p

        @self.pg.production('stats : POKEMON STATS_DECLARATION STAT ASSIGN VALUE STAT ASSIGN VALUE STAT ASSIGN VALUE STAT ASSIGN VALUE stats')
        @self.pg.production('stats : POKEMON STATS_DECLARATION STAT ASSIGN VALUE STAT ASSIGN VALUE STAT ASSIGN VALUE STAT ASSIGN VALUE')
        def stats(p):
            return p

        @self.pg.production('condition : POKEMON DOT STAT GREATER_THAN VALUE OR POKEMON DOT STAT GREATER_THAN VALUE')
        def condition(p):
            return p

        @self.pg.production('battle : WHILE LEFT_BRACKET condition RIGHT_BRACKET action')
        def battle(p):
            return p

        @self.pg.production('action : POKEMON USE ATTACK action')
        @self.pg.production('action : POKEMON USE ATTACK')
        def action(p):
            return p
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
