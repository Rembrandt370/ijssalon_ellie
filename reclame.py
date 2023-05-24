from algemene_functies import mijn_functie_2

def aanbiedingen(smaak, prijs, korting):
    aanbieding = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de {smaak}, van {prijs} euro voor {prijs - (prijs * korting)} euro."
    return aanbieding

resultaat = aanbiedingen("aardbei", 4, 0.1)
print(resultaat)


def inkomsten_totaal(btw_percentage):
    inkomsten = [220, 430, 125, 160, 260, 205, 90, 345]
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * btw_percentage
    totaal_inclusief_btw = totaal_inkomsten + btw_bedrag
    return totaal_inclusief_btw, btw_bedrag

btw_percentage = 0.09
resultaat, btw_bedrag = inkomsten_totaal(btw_percentage)

resultaat_string = f"Het totaal van alle inkomsten van deze week is {resultaat} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
print(resultaat_string)

def laag_en_hoog():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    hoogste_waarde = max(mijn_lijst)
    laagste_waarde = min(mijn_lijst)
    print("Mijn hoogste waarden is:", hoogste_waarde)
    print("Mijn laagste waarden is:", laagste_waarde)
laag_en_hoog()

def gemiddelde():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    totaal = sum(mijn_lijst)
    aantal_elementen = len(mijn_lijst)
    gemiddelde = totaal / aantal_elementen
    return gemiddelde
resultaat = gemiddelde()
print("Het gemiddelde is:", resultaat)

def gemiddelde():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    totaal = sum(mijn_lijst)
    return totaal

resultaat = gemiddelde()
resultaat_string = f"De gemiddelde inkomsten deze week zijn {resultaat} euro."
print(resultaat_string)

def meervoudig():
    invoer_lijst = [10,5,3,2,1,2,9]
    laagste_waarden = max(invoer_lijst)
    laagste_waarden = min(invoer_lijst)
    laag_en_hoog()
meervoudig()


def combinatie(invoer_lijst_2):
    return meervoudig()
resultaat = meervoudig()
combinatie_resultaat = combinatie(resultaat)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer   
    










