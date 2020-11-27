# Deze Test blauwdruk wordt vanaf dit moment in het geheugen gezet. Van hier...
class Test():
    STATIC_VAR = 123
    voorbeeld = "Hallo"

    def __init__(self):
        print("INIT:", self.voorbeeld)

    def Verander(self, nieuw):
        self.voorbeeld = nieuw
        print("Veranderd naar:", self.voorbeeld)

    def DoeIets(self):
        self.x += Test.STATIC_VAR
# ... Tot hier
# Test is nu een object in het geheugen. Het class object dus.

# Vanaf hier maken wij een INSTANTIE van de Test class. Er wordt een kopie gemaakt van de Test class object. (Zoals deze op dat moment in het geheugen staat.)
leuk = Test()
leuk.Verander("Raar")

print("-----------------------------------")
print(leuk.voorbeeld)
print(Test.voorbeeld)

# Vanaf dit moment verander ik de waarde van het Test CLASS OBJECT. Als ik nu een nieuwe instantie van de Test class ga maken, dan heeft de nieuwe instantie
# nu "Gekkigheid" als standaard waarde voor de "voorbeeld" variabele.
Test.voorbeeld = "Gekkigheid"

print("-----------------------------------")
print(leuk.voorbeeld)
print(Test.voorbeeld)


print("-----------------------------------")
# Vanaf hier maken we dus weer een nieuwe instantie van de Test class. MAAR, het CLASS OBJECT hebben we veranderd. De huidige staat van het class object wordt
# gebruikt om er een kopie van te maken en die in "ding" op te slaan.
ding = Test()
print(leuk.voorbeeld)
print(ding.voorbeeld)
print(Test.voorbeeld)