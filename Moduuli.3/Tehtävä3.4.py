Vuosiluku = int(input("Anna vuosiluku"))
if Vuosiluku % 4 == 0 and Vuosiluku % 100 == 0 and Vuosiluku % 400 == 0:
    print("Vuosi on karkausvuosi,")
else:
    print("Vuosi ei ole karkausvuosi.")

