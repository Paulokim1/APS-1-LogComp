# APS-1-LogComp

```python
<program> ::= {player}, {stats}, <battle>, <outcome>

<player> ::= <name> "chose" <pokemon> "as" <variable>

<name> ::= "Red" | "Blue" | "Green"

<pokemon> ::= "Charmander" | "Squirtle" | "Bulbasaur"

<variable> ::= "pokemon1" | "pokemon2"

<attribute> ::= "Level" | "HP" | "Moves"

<value> ::= [0-9]+ | <move_list>

<move> ::= "Tackle" | "Scratch" | "Ember" | "Water Gun" | "Razor Leaf" | "Leer" | "Tail Whip"

<battle> ::= "while" "(" <condition> ")" ":" {action}

<action> ::= <attack> | <debuf> | <damage> 

<condition> ::= <pokemon1>.alive "or" <pokemon2>.alive

<attack> ::= <pokemon1> | <pokemon2> "uses" <move>

<damage> ::= <pokemon2> "lost" <value> "HP" 

<debuf> ::= <pokemon1> <atk_def_stat> "fell"

<atk_def_stats> ::= "attack" | "defense"

<outcome> ::= <pokemon> "The winner is" <pokemon>
```

## Exemplo

```python
Red chose Charmander as pokemon1

Blue chose Squirtle as pokemon2

Charmander.stats: 

    Level = 1

    HP = 22

    Moves = [Scratch, Ember, Leer]

Squirtle.stats: 

    Level = 1

    HP = 28

    Moves = [Tackle, Water Gun, Tail Whip]

while (pokemon1.alive or pokemon2.alive): 

    Charmander uses Scratch

    Squirtle lost 7 HP

    Squirtle uses Tail Whip

    Charmander defense fell

    Charmander uses Scratch

    Squirtle lost 7 HP

    Squirtle uses Water Gun

    Charmander lost 24 HP

    Charmander fainted

The winner is Squirtle.
```
