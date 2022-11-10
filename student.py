
class Student():

    def __init__(self, ime_studenta):
        self.ime = ime_studenta
        self.broj_izostanaka = 0
        self.broj_dolazaka = 0

    def ponasanje(self):
        if self.broj_dolazaka < 3:
            return "BAD"
        else:
            return "GOOD"

   # def broji_izostanak(self,broj_izostanaka):
       # self.broj_izostanaka = broj_izostanaka

    #def broji_dolazak(selfs,broj_dolazaka):
       # self.broj_dolazaka = broj_dolazaka