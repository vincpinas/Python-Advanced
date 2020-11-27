# Class Indeling

### ***Hoe verander je een variable in een class?***
#
Een class heeft meerdere variabelen, om deze variabelen te veranderen moet je een pad maken naar het variabelen.
Om dit bij een instantie van een class te doen zou je als voorbeeld zo een pad kunnen gebruiken.

```player.rect.y = 100```

Dit is misschien een beetje verwarrend, dus is het handig om het in stukjes op te snijden.

```player``` is de instantie van de class, daarna heb je ```rect``` dit is een variable van de class.
Dus dat zou er als volgt uit zien ```player.rect```

In dit geval gebruik je een instantie van de rect class van de pygame module, dus als je een hoogte of breedte mee zou willen geven aan je rect dan zou je

```player.rect.y``` ***of*** ```player.rect.x``` kunnen meegeven.


<br/>
---
### ***Wanneer zet je een variable in je  __init __?***
# 
Je gebruikt een je ```__init__``` wanneer je iets 1 keer wilt uitvoeren aan het begin van je instantie of wanneer je de klas aan roept.

Dus bijvoorbeeld wanneer je een surface/foto inlaad of muziek in laad etc.