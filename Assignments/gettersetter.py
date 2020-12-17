class MijnClass:

    __points = 0
    @property
    def points (self):
        print("POINTS GETTER WORDT AANGEROEPEN!")
        return self.__points


    @points.setter
    def points (self, value):
        print("POINTS SETTER WORDT AANGEROEPEN! VALUE IS:", value)

        if (value > 100):
            print("De nieuwe waarde is groter dan 100!")
            print("Huidige punten zijn:", self.__points)
            value = 100

        self.__points = value

    name = "Mario"



instance = MijnClass()

print(instance.name)

print(instance.points)

instance.points += 20
print("Points are now:", instance.points)

instance.points = 144
print("Second time. Points are now:", instance.points)