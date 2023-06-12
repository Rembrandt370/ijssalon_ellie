def presenteer(inkomsten, totaal_inkomsten):
    for item, value in inkomsten.items():
        print(f"{item} : {value} euro")
    print("==========================")
    print(f"totaal : {totaal_inkomsten} euro")


