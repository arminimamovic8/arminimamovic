import random
class Deck:
    def __init__(self, karte, tipovi, izmjesanaLista):
        self.karte = karte
        self.tipovi = tipovi
        self.izmjesanaLista = izmjesanaLista

class Card(Deck):
    def __init__(self, karte, tipovi, izmjesanaLista):
        super().__init__(karte, tipovi, izmjesanaLista)

    def mjesajKarte(self):
        for x in self.karte:
            for y in self.tipovi:
                self.izmjesanaLista.append(x + " " + y)
        random.shuffle(self.izmjesanaLista)
    
    def ispisKarata(self):
        while len(self.izmjesanaLista) != 0:
            mojaKarta = random.choice(self.izmjesanaLista)
            print(mojaKarta)
            self.izmjesanaLista.remove(mojaKarta)
        
        

c = Card(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"], ["srce", "pik", "tref", "kocka"], [])
c.mjesajKarte()
c.ispisKarata()
