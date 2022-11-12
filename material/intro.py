# -*- coding: utf-8 -*-

cat = "miaou"
print(cat)
print("Hello")
print(len(cat))

cat = "toto" + str(4)
print(cat)
print(4 + 1.5)

# interprêté, typage dynamique, implicite, orienté objet, fortement typé
x = 4

if x == 4:
    print("vrai")
elif x == 6:
    print("c'est égal à 6")
else:
    print("faux")

annee = 2008
typeAnnee = "non bissextile" if annee % 4 != 0 else "bissextile"
print(typeAnnee)
# boucle while
count = 0
while count < 9:
    print('The count is:', count)
    count += 1

if x == 5:
    pass
else:
    print("dans le else")

items = [42, 55, 10, 11]
for item in items:
    print(item)

for i in range(len(items)):
    print(i, "->", items[i])

for i in [0, 1, 2, 3, 4, 5, 6]:
    print(i)

for i in range(7):
    print(i)

print("range avec intervalle (borne inf, borne sup, pas)")
for i in range(1, 5, 2):
    print(i)

for i in range(1000, 20, -48):
    print(i)

# dictionnaire (map en java)
lolCharacter = {"name": "ashe", "hp": 80, "role": "adc"}
print(lolCharacter["name"])
lolCharacter["attack"] = 10
print(lolCharacter["attack"])

for k in lolCharacter:
    print(k, "->", lolCharacter[k])

for k, v in lolCharacter.items():
    print(k, "->", v)
