nimi = input("Kerro nimesi:")

if nimi == "Matti":
    print("Ei käy!")
else:

    print("Montako keittoannosta haluat?")
    keittoannokset = int(input ("Anna keittoannosten määrä: "))
    print("Olet tilnnut", keittoannokset, "keittoannosta.")
    print("Hinta on", keittoannokset * 5.90, "euroa.")
    print("Hyvää päivänjatkoa!")