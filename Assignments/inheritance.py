class Character:
    speed = 2.5
    strength = 2
    points = 0
    sprite = None
    y = 500
    x = 500

    def __init__(self):
        self.characterSprite = " "

    def walk(self):
        print("Character loopt nu met snelheid", self.speed)

    def throw(self,character, throwitem):
        self.throwitem = throwitem
        self.character = character
        print(self.character, "throws", self.throwitem)

class Mario(Character):
    lives = 3
    item = None

    def __init__(self):
        # De snlheid en strength van Mario is standaard hoger:
        # het wordt hier overgeschreven.
        self.speed = 10
        self.strength = 5

    def walk(self):
        print("Mario loopt heel anders! Maar wel met snelheid", self.speed)

    def Jump(self):
        print("jump!!")

        # de throw function wordt hier uitgebreid.
    def throw(self):
        super().throw("Mario", "fireball")
        print("He hits an enemy and gains some health")


# Instanties maken ::
characterA = Character()
marioX = Mario()

characterA.walk()

print(marioX.speed)
print(characterA.speed)
print(marioX.lives)
marioX.Jump()
marioX.walk()
characterA.throw("character", "item")
marioX.throw()