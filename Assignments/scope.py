class MijnClass:

    varOpenbaar = "Dit is openbaar toegankelijk"
    __varPrive = "Deze is prive"
    # Als deze class geinstantieerd wordt, bestaat "nieweVariabele" nog niet

    def getVarPrive(self):
        return self.__varPrive

    def setVarPrive(self, value):
        if isinstance(value, str):
            self.__varPrive = value

    def Voorbeeld(self):
        print(self.__varPrive)

        waardeA = "Tijdelijk"
        print("Waarde A is", waardeA)
        # WaardeA bestaat alleen in deze functie omdat hij hier gemaakt is.

    def AndereFunctie(self):
        # WaardeA bestaat alleen binnen functie "Voorbeeld"
        # print(waardeA)

        # Vanaf dit punt voeg ik een nieuwe variabele toe aan de instantie van deze class
        self.nieuweVariabele = "Deze variabele is nieuw"

instClass = MijnClass()

print(instClass.varOpenbaar)

instClass.Voorbeeld()

instClass.setVarPrive("wat coool")

instClass.Voorbeeld()

instClass.AndereFunctie()