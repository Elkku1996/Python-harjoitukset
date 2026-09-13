sukupuoli = input ("Anna biologinen sukupuoli ") 
if sukupuoli == "nainen":
    Hemoglobiiniarvo = float(input(" Anna hemoglobiiniarvo g/l: ")) 
    if Hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo alhainen.")
    elif Hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvo normaali.")
    else:
        print("Hemoglobiiniarvo korkea.")

elif sukupuoli == "mies":
    Hemoglobiiniarvo = float(input(" Anna hemoglobiiniarvo g/L: "))
    if Hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo alhainen.")
    elif Hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvo normaali.")
    else: 
        print("Hemoglobiiniarvo korkea.")