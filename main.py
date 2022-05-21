class Pracownik:
    
    
    def __init__(self, imie=None, pensja_netto=0, skladki_pracodawcy=0, koszt_pracodawcy=0):
        self._imie = imie
        self._pensja_netto = pensja_netto
        self._skladki_pracodawcy = skladki_pracodawcy
        self._koszt_pracodawcy = koszt_pracodawcy
    
    def __str__(self):
        return f"{self._imie} {self._pensja_netto} {self._skladki_pracodawcy} {self._koszt_pracodawcy}"
        
    
        
liczba_pracownikow = input()
imiona=[]
pensje = []
wyplaty = []
skladki = []
koszt_calk = []
for index in range(int(liczba_pracownikow)):
    wejscie=input().split(" ")
    imie = wejscie[0]
    pensja_brutto = float(wejscie[1])
    skladka_emerytalna = round(pensja_brutto* 0.0976,2)
    skladka_rentowa = round(pensja_brutto* 0.015,2)
    skladka_chorobowa = round(pensja_brutto* 0.0245,2)
    suma_skladek = round(skladka_emerytalna + skladka_rentowa + skladka_chorobowa,2)
    podstawa_na_ubezp = round(pensja_brutto-suma_skladek,2)
    skladka_na_ubezp_zdr = round(podstawa_na_ubezp*0.09,2)
    skladka_na_ubezp_zdr_do_odl = round(podstawa_na_ubezp*0.0775,2)
    koszty_uzysk_przychodu = 111.25
    podstawa_oblicz_zaliczki_na_podatek =round(pensja_brutto-koszty_uzysk_przychodu-suma_skladek,0)
    zaliczka_na_podatek = round((podstawa_oblicz_zaliczki_na_podatek *0.18)-46.33,2)
    zaliczka_do_pobrania = round(zaliczka_na_podatek-skladka_na_ubezp_zdr_do_odl,0)
    kwota_do_wyplaty = round(pensja_brutto-suma_skladek-skladka_na_ubezp_zdr-zaliczka_do_pobrania,2)
    skladki_pracodawcy = round((pensja_brutto*0.0976)+(pensja_brutto*0.065)+(pensja_brutto*0.0193)+(pensja_brutto*0.0245)+(pensja_brutto*0.001),2)
    koszt_pracodawcy = round(pensja_brutto+skladki_pracodawcy,2)
                 
    imiona.append(imie)
    pensje.append(pensja_brutto)
    wyplaty.append(kwota_do_wyplaty)
    skladki.append(skladki_pracodawcy)
    koszt_calk.append(koszt_pracodawcy)



for i in range(len(imiona)):

    pracownik = Pracownik(imiona[i], str('%.2f' % wyplaty[i]),str('%.2f' % skladki[i]),str('%.2f' % koszt_calk[i]))

    print(pracownik)
print(sum(koszt_calk))
