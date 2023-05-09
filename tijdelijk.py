producten = {"aardbei": 3, "vanille": 4, "chocolade": 5}
print(producten)


aanbieding = producten["vanille"] * 0.8

print(aanbieding)

reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding:.2f}"

#print(reclame_tekst)
reclame_tekst2 = reclame_tekst[:38]
#print(reclame_tekst2)

reclame_tekst3 = reclame_tekst2.upper()

#print(reclame_tekst3)
reclame_tekst4 = str(reclame_tekst3)
#print(reclame_tekst4)
for el in reclame_tekst4:
    #print(el)
    #print(el.lower())
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())








