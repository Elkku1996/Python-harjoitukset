import math

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luoti_grammoina = luodit * 13.3
naula_luoteina = naulat * 32.4
leiviska_nauloina = leiviskat * 20 

kaikki_luodit = luodit + (naulat * naula_luoteina) + (leiviskat * leiviska_nauloina * naula_luoteina)

kokonais_grammat = kaikki_luodit * luoti_grammoina

kilogrammat = int(kokonais_grammat // 1000)
jäljelle_jäävät_grammat = kokonais_grammat % 1000
print("\nKeskiaikainen massa nykymittoina:")
print(f"{kilogrammat} kilogrammaa ja {jäljelle_jäävät_grammat:.2f} grammaa.")
