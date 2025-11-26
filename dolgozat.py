"""
Olvasunk be billentyűzetről egész számokat, és tároljuk őket egy listában! A bevitel végét a 0 jelezze.
  Majd oldjuk meg a következő feladatokat!Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e -10 és -15 közé eső szám a beírtak között?
2. Írjuk ki az utolsó 2-vel és 5-tel osztható szám indexét!
3. Hány darab 20-nál nagyobb számot írtak be?
4. Melyik és hányadik volt a legkisebb beírt pozitív egész szám?
5. Mennyi a negatív számok számok átlaga?
"""


bekert = [int(input("Kérlek adj meg egy egész számot")) for i in range(10)]

#elsofeladat
print("Első feladat")

negativ = any(-15 < x <-10 for x in bekert) 
if negativ:
    print(f"Van a listában -15 és -10 közéeső szám!")
else:
    print(f"Nincs a listában -15 és -10 kőzé eső szám!")


#masodikfeladat
print("Második feladat")





#harmadikfeladat
print("Harmadik feladat")

husz=20
szamlalo= sum(1 for x in bekert if x > husz)
print(f"{szamlalo} db húsznál nagyobb szám van a listában!")


#negyedikfeldat
print("Negyedik feladat")

min_szam = min(x for x in bekert if x>0)
print(f"A legkisebb szám a listában: {min_szam}")

index_min_szam = bekert.index(min(x for x in bekert if x>0))
index_igazi = index_min_szam + 1
print(f"A legkisebb szám a listában a {index_igazi}. szám!")


#otodikfeladat
print("Ötödik feladat")

minuszok = []
for x in bekert:
    if x < 0:
        minuszok.append(x)

atlag = sum(minuszok) / len(minuszok)

print(f"A negatív számok átlaga:{atlag}")