from pokemon_lexer import Lexer
from pokemon_parser import Parser

text_input = ''' The Battle of Pallet Town
Red chose Charmander 
Blue chose Squirtle 
Charmander stats
    Level = 1
    HP = 22
    AS = 10
    DS = 7
Squirtle stats
    Level = 1
    HP = 28
    AS = 8
    DS = 11
while (Charmander.HP > 0 or Squirtle.HP > 0)
    Charmander use Scratch
    Squirtle use Tail Whip
    Charmander use Scratch
    Squirtle use Water Gun
Gotta catch 'em all
'''


lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

# for token in tokens:
#     print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()

try: 
    parser.parse(tokens)
except Exception as e:
    print(e)
