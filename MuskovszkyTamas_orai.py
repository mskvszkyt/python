# 1 feladat

bekert_adat = int(input('Adj meg egy számot 1000 és 10000 között: '))
feltetelek = False
if bekert_adat <= 10000 and bekert_adat >= 1000:
    feltetelek = True
else:
    pass

while feltetelek:
    szamjegyek = []
    for szamjegy in str(bekert_adat):
        szamjegyek.append(szamjegy)
    break

print(szamjegyek)

print(f"a tízes helyiértéken a: {szamjegyek[-2]} szám áll")
print(f"a százas helyiértéken a: {szamjegyek[-3]} szám áll")

# 2 feladat


termek_ara = int(input("\nKérem a termék árát: "))
kedvezmeny = input("Adja meg a termékre vonatkozó kedvezményt(A/B): ")

feltetelek = False
if kedvezmeny.lower() == "a":
    vonatkozo_kedvezmeny = 0.05
    feltetelek = True

elif kedvezmeny.lower() == "b":
    vonatkozo_kedvezmeny = 0.1
    feltetelek = True

else:
    print("hibás adat")

while feltetelek:
    fizetendo_összeg = termek_ara - termek_ara * vonatkozo_kedvezmeny
    print(f"\n\nA fizetendo összeg: {fizetendo_összeg}ft")
    feltetelek = False

# 3 feladat

# a,
helyes_adat_a = False
while helyes_adat_a == False:
    magassag = int(input("Mekkora a magassaga(cm)? "))
    if magassag <= 230 and magassag >= 140:
        helyes_adat_a = True
        print("helyes adat")
    else:
        print("hibás adat")
        pass

# b,

helyes_adat_b = False
while helyes_adat_b == False:
    meret = input("\nMekkora az ing mérete(S/M/L/XL)? ")
    if meret.lower() == "s" or meret.lower() == "m" or meret.lower() == "l" or meret.lower() == "xl":
        helyes_adat_b = True
        print("\nhelyes adat")
    else:
        print("\nhibás adat")
        pass

# szövegkezeles 1,

szöveg = input("írj be egy szöveget ")
szamlalo = 1
szerkesztett = ""
for karakter in szöveg:
    if szamlalo % 2 == 1:
        szerkesztett = szerkesztett + karakter
    szamlalo += 1
print(szerkesztett)

# 2,


szöveg = input("írj be egy szöveget vesszőkkel ")
vesszok = 0
for karakter in szöveg:
    if karakter == ",":
        vesszok += 1
print(f"a vesszők száma a szövegben {vesszok}db")

# 3,

név = input("Írd be a teljes nevedet ")
név_lista = név.split()
vezeteknev = név_lista[0][0:3]
keresztnev = név_lista[1][0:3]
print(vezeteknev)
print(keresztnev)
print(f"Az aktuális felhasználónév: {vezeteknev}_{keresztnev}")
