class Ptak:

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print(f"Tutaj {self.gatunek}, startuje i rozpoczynam łowy.")

    def wydaj_odglos(self):
        pass

class Kura(Ptak):

    def lataj(self):
        print(f"Tutaj {self.gatunek}, ja nie latam i nie poluje (jeszcze)...")