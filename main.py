class Uczen:
    def __init__(self, imie_nazwisko_ucznia, klasa_ucznia):
        self.imie_nazwisko_ucznia = imie_nazwisko_ucznia
        self.klasa_ucznia = klasa_ucznia

class Wychowawca:
    def __init__(self, imie_nazwisko_wychowawcy, prowadzona_klasa):
        self.imie_nazwisko_wychowacy = imie_nazwisko_wychowawcy
        self.prowadzona_klasa = prowadzona_klasa

class Nauczyciel:
    def __init__(self):


zakoncz_program = False
while not zakoncz_program:
    print("Szkolna lista personelu i uczniów\nWybierz co chcesz zrobić:\n")
    opcje = input("1.Utwórz\n2.Zarządzaj\n3.Koniec\n")
    if opcje = "1":
        pass
    if opcje = "2":
        pass
    if opcje = "3":
        zakoncz_program = True
    else:
        print("Błąd. Wybierz jedną z sugerowanych komend")
