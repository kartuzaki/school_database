class Uczen:
    def __init__(self, imie_i_nazwisko, klasa):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"Uczeń: {self.imie_i_nazwisko}, klasa: {self.klasa}"


class Nauczyciel:
    def __init__(self, imie_i_nazwisko, przedmioty=[], klasy=[]):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.przedmioty = przedmioty
        self.klasy = klasy

    def __repr__(self):
        return f"Nauczyciel: {self.imie_i_nazwisko}, przedmioty: {', '.join(self.przedmioty)}, klasy: {', '.join(self.klasy)}"


class Wychowawca:
    def __init__(self, imie_i_nazwisko, klasa):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"Wychowawca: {self.imie_i_nazwisko}, klasa: {self.klasa}"


uczniowie = []
nauczyciele = []
wychowawcy = []


def utworz_ucznia():
    imie_i_nazwisko = input("Podaj imię i nazwisko ucznia: ")
    klasa = input("Podaj nazwę klasy ucznia: ")
    uczniowie.append(Uczen(imie_i_nazwisko, klasa))


def utworz_nauczyciela():
    imie_i_nazwisko = input("Podaj imię i nazwisko nauczyciela: ")
    przedmioty = input("Podaj przedmioty prowadzone przez nauczyciela (oddzielone przecinkami): ").split(',')
    klasy = []
    print("Podaj klasy, które prowadzi nauczyciel (po jednej nazwie klasy w jednej linii, zakończ pustą linią):")
    while True:
        klasa = input()
        if not klasa:
            break
        klasy.append(klasa)
    nauczyciele.append(Nauczyciel(imie_i_nazwisko, przedmioty, klasy))


def utworz_wychowawce():
    imie_i_nazwisko = input("Podaj imię i nazwisko wychowawcy: ")
    klasa = input("Podaj nazwę klasy, którą prowadzi wychowawca: ")
    wychowawcy.append(Wychowawca(imie_i_nazwisko, klasa))


def zarzadzaj_klasa():
    klasa = input("Podaj nazwę klasy, którą chcesz wyświetlić: ")
    print(f"Uczniowie klasy {klasa}:")
    for uczen in uczniowie:
        if uczen.klasa == klasa:
            print(uczen)
    print(f"Wychowawca klasy {klasa}:")
    for wychowawca in wychowawcy:
        if wychowawca.klasa == klasa:
            print(wychowawca)


def zarzadzaj_uczen():
    imie_i_nazwisko = input("Podaj imię i nazwisko ucznia: ")
    for uczen in uczniowie:
        if uczen.imie_i_nazwisko == imie_i_nazwisko:
            print(f"Przedmioty ucznia {uczen.imie_i_nazwisko}:")
            for nauczyciel in nauczyciele:
                if uczen.klasa in nauczyciel.klasy:
                    print(f"{', '.join(nauczyciel.przedmioty)}")
            break


def zarzadzaj_nauczyciel():
    imie_i_nazwisko = input("Podaj imię i nazwisko nauczyciela: ")
    for nauczyciel in nauczyciele:
        if nauczyciel.imie_i_nazwisko == imie_i_nazwisko:
            print(f"Klasy prowadzone przez nauczyciela {nauczyciel.imie_i_nazwisko}: {', '.join(nauczyciel.klasy)}")
            break


def zarzadzaj_wychowawca():
    imie_i_nazwisko = input("Podaj imię i nazwisko wychowawcy: ")
    for wychowawca in wychowawcy:
        if wychowawca.imie_i_nazwisko == imie_i_nazwisko:
            print(f"Uczniowie prowadzeni przez wychowawcę {wychowawca.imie_i_nazwisko} w klasie {wychowawca.klasa}:")
            for uczen in uczniowie:
                if uczen.klasa == wychowawca.klasa:
                    print(uczen)
            break


koniec_programu = False
while not koniec_programu:
    print("Witaj w programie zarządzania bazą szkolną. Wybierz komendę, którą chcesz wykonać:")
    operacja = input("1. Utwórz\n2. Zarządzaj\n3. Koniec programu\n")

    if operacja == "1":
        opcja_utworzenia = input("Co chcesz utworzyć?\n1. Uczeń\n2. Nauczyciel\n3. Wychowawca\n4. Koniec\n")
        if opcja_utworzenia == "1":
            utworz_ucznia()
        elif opcja_utworzenia == "2":
            utworz_nauczyciela()
        elif opcja_utworzenia == "3":
            utworz_wychowawce()
        elif opcja_utworzenia == "4":
            continue

    elif operacja == "2":
        opcja_zarzadzania = input("Czym chcesz zarządzać?\n1. Klasa\n2. Uczeń\n3. Nauczyciel\n4. Wychowawca\n5. Koniec\n")
        if opcja_zarzadzania == "1":
            zarzadzaj_klasa()
        elif opcja_zarzadzania == "2":
            zarzadzaj_uczen()
        elif opcja_zarzadzania == "3":
            zarzadzaj_nauczyciel()
        elif opcja_zarzadzania == "4":
            zarzadzaj_wychowawca()
        elif opcja_zarzadzania == "5":
            continue

    elif operacja == "3":
        koniec_programu = True

    else:
        print("Nieprawidłowa komenda. Spróbuj ponownie.")
