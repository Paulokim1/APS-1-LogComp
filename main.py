from pokemon_lexer import Lexer

text_input = '''Red chose Charmander 
Blue chose Squirtle 

Charmander stats:

    Level = 1

    HP = 22

    AS = 10

    DS = 7

Squirtle stats:

    Level = 1

    HP = 28

    AS = 8

    DS = 11

while (Charmander.HP > 0 or Squirtle.HP > 0):

    Charmander use Scratch!

    Squirtle use Tail Whip!

    Charmander use Scratch!

    Squirtle use Water Gun!
'''


lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)

# Output:
# Token('TRAINER', 'Red')
# Token('CHOSE', 'chose')
