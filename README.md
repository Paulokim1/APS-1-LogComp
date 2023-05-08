# APS-1-LogComp

```python
<program> ::= {player}, {stats}, <battle>, <outcome>

<player> ::= <name> "chose" <pokemon> 

<name> ::= "Red" | "Blue" | "Green"

<pokemon> ::= "Charmander" | "Squirtle" | "Bulbasaur"

<stats> ::= <pokemon> "'s stats :" <attribute> "=" <value>, <attribute> "=" <value>, <attribute> "=" <value>

<attribute> ::= "Level" | "HP" | "AS" | "DS"

<value> ::= [0-9]+

<move> ::= "Tackle" | "Scratch" | "Ember" | "Water Gun" | "Razor Leaf" | "Leer" | "Tail Whip"

<battle> ::= "while" "(" <condition> ")" ":" {action}

<action> ::= <attack> | <debuf> | <damage> 

<condition> ::= <pokemon1>.alive "or" <pokemon2>.alive

<attack> ::= <pokemon>  "uses" <move>

<damage> ::= <pokemon> "lost" <value> "HP" 

<debuf> ::= <pokemon> <attribute> "fell"

<outcome> ::= <pokemon> "The winner is" <pokemon>
```

## Exemplo

```python
Red chose Charmander as pokemon1

Blue chose Squirtle as pokemon2

Charmander's stats : 

    Level = 1

    HP = 22

    AS = 10

    DS = 7

Squirtle's stats : 

    Level = 1

    HP = 28

    AS = 8

    DS = 11

while (pokemon1.alive or pokemon2.alive): 

    Charmander uses Scratch

    Squirtle lost 7 HP

    Squirtle uses Tail Whip

    Charmander DS fell

    Charmander uses Scratch

    Squirtle lost 7 HP

    Squirtle uses Water Gun

    Charmander lost 24 HP

    Charmander fainted

The winner is Squirtle.
```
