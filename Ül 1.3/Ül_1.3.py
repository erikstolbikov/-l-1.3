#Ülesanne 1
from datetime import date

nimi = input("Sisesta oma nimi: ")
print("Tere,", nimi)

tana = date.today()

print("Tänane kuupäev:", tana)
print("Päev:", tana.day)
print("Kuu:", tana.month)
print("Aasta:", tana.year)

print("Kuupäev:", tana.strftime("%d/%m/%Y"))

#Ülesanne 2
# Arvutused

a = 3 + 8 / (4 - 2) * 4
b = 3 + 8 / 4 - 2 * 4
c = (3 + 8) / (4 - 2) * 4

print("Esimene vastus:", a)
print("Teine vastus:", b)
print("Kolmas vastus:", c)

print("Järeldus: Sulud muudavad arvutuse tulemust.")

#Ülesanne 3
import math

R = float(input("Sisesta raadius: "))

a = 2 * R

print("Ruudu pindala:", a * a)
print("Ruudu ümbermõõt:", 4 * a)
print("Ringi pindala:", math.pi * R * R)
print("Ringi ümbermõõt:", 2 * math.pi * R)

#Ülesanne 4
import math

raadius = 6378
mundi_laius = 2.575

umbermoot = 2 * math.pi * raadius
umbermoot = umbermoot * 1000000

muntide_arv = umbermoot / mundi_laius

print("Maa ümbermõõt:", round(umbermoot, 2), "mm")
print("Münte on vaja:", math.ceil(muntide_arv))

#Ülesanne 5
tekst = "kill-koll kill-koll killadi-koll kill-koll killadi-koll kill-koll kill-koll kill-koll"

print(tekst.upper())
print("KILL-KOLL.")

#Ülesanne 6
print("ПОЕЗД ГУДЕЛ ТУК-ТУК-ТУК,")
print("ЧИРИКАЮЩАЯ УТКА БЫЛА КОНДУКТОРОМ.")
print("КОЛЕСА ГУДЕЛИ ТУК-ТУК,")
print("ТУК-ТУК И ТУК-ТУК.")
print("НО В ПОЕЗДЕ,")
print("ЗНАЕТЕ ЛИ ВЫ, КТО ТАМ БЫЛ?")
print()

print("ПОЕЗД ГУДЕЛ ТУК-ТУК-ТУК,")
print("ЧИРИКАЮЩАЯ УТКА БЫЛА КОНДУКТОРОМ.")
print("КОЛЕСА ГУДЕЛИ ТУК-ТУК,")
print("ТУК-ТУК И ТУК-ТУК.")

#Ülesanne 7
a = float(input("Esimene kylg: "))
b = float(input("Teine kylg: "))

p = 2 * (a + b)
s = a * b

print("Ymbermoot:", p)
print("Pindala:", s)

#Ülesanne 8
try:
    liitrid = float(input("Sisesta tangitud kütuse liitrid: "))
    kilomeetrid = float(input("Sisesta läbitud kilomeetrid: "))

    kulu = (liitrid / kilomeetrid) * 100

    print("Keskmine kütusekulu 100 km kohta on:", round(kulu, 2), "liitrit")

except ValueError:
    print("Liitrid ja kilomeetrid peavad olema arvud!")

except ZeroDivisionError:
    print("Kilomeetrite arv ei tohi olla 0!")

#Ülesanne 9
kiirus = 29.9

M = float(input("Sisesta sõiduaeg minutites: "))

# Jagame 60-ga, et saada tunnid
aeg_tundides = M / 60

vahemaa = kiirus * aeg_tundides

print("Rulluisutaja jõuab", M, "minutiga", round(vahemaa, 2), "km kaugusele.")

#Ülesanne 10 
kogu_minutid = int(input("Sisesta aeg minutites: "))

tunnid = kogu_minutid // 60
minutid = kogu_minutid % 60

print("Aeg on", tunnid, "tundi ja", minutid, "minutit.")