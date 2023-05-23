def mijn_functie_1(argument):
        retourwaarden = {
             2: 4,
             4: 16,
             10: 100,
             12: 144
        }

        if argument in retourwaarden:
             return retourwaarden[argument]
        
waarden1 = mijn_functie_1(2)
print(waarden1)
waarden2 = mijn_functie_1(4)
print(waarden2)
waarden3 = mijn_functie_1(10)
print(waarden3)
waarden4 = mijn_functie_1(12)
print(waarden4)


def mijn_functie_2(argument):
        retourwaarden = {
             12.3: [15, 9, 36, 4],
             12.2: [14, 10, 24, 6],
             10.5: [15, 5, 50, 2],
             100.20: [120, 80, 2000, 5]
        }

        if argument in retourwaarden:
             return retourwaarden[argument]
waarden1 = mijn_functie_2(12.3)
print(waarden2)
waarden2 = mijn_functie_2(12.2)
print(waarden2)
waarden3 = mijn_functie_2(10.5)
print(waarden3)
waarden4 = mijn_functie_2(100.20)
print(waarden4)        


        