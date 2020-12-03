class Character:
    speed = 2.5
    strength = 4
    points = 0
    sprite = None
    y = 500
    x = 500

    def __init__(self):
        self.characterSprite = " "

    def walk(self):
        print("Character loopt nu met snelheid", self.speed)

    def throw(self):
        self.throwitem = "item"
        self.character = "character"
        print("character throws", self.throwitem)

class Mario(Character):
    lives = 3
    item = None

    def __init__(self):
        # Super roept de class waarvan wordt overgeërfd, in dit geval Character aan om een functie van die class aan om daar aan toe te voegen.
        # We vullen aan op de constructor van de Character:
        super().__init__()

        # De snlheid van Mario is standaard hoger:
        self.speed = 10

    def walk(self):
        print("Mario loopt heel anders! Maar wel met snelheid", self.speed)

    def Jump(self):
        print("jump!!")

    def throw(self):
        super().throw()
        print("He hits an enemy and gains some health")


# Instanties maken ::
characterA = Character()
marioX = Mario()

characterA.walk()
marioX.walk()

print(marioX.speed)
print(characterA.speed)
print(marioX.lives)
marioX.Jump()
marioX.walk()
characterA.throw()
marioX.throw()


# Print de locaties in het geheugen uit::
#print(marioX.Jump)
#print(marioX)
#print(characterA)