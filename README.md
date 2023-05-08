# APS-1-LogComp

```python
<program> ::= {player}, {stats}, <battle>, <outcome>

<player> ::= <trainer> "chose" <pokemon> 

<trainer> ::= "Red" | "Blue" | "Green"

<pokemon> ::= "Charmander" | "Squirtle" | "Bulbasaur"

<stats> ::= <pokemon> "'s stats :" <attribute> "=" <value>, <attribute> "=" <value>, <attribute> "=" <value>

<attribute> ::= "Level" | "HP" | "AS" | "DS"

<value> ::= [0-9]+

<move> ::= "Tackle" | "Scratch" | "Ember" | "Water Gun" | "Razor Leaf" | "Leer" | "Tail Whip"

<battle> ::= "while" "(" <condition> ")" ":" {action}

<action> ::= <attack>

<condition> ::= <pokemon>.<attribute> "or" <pokemon>.<attribute>

<attack> ::= <pokemon>  "use" <move>
```

## Exemplo

```python
The Battle of Pallet Town

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
```
