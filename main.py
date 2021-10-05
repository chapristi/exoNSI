from datetime import datetime
"""
def moyenne (serie):
  if(len(serie) == 0):
    return "aucune valeur n'a etait entrée"
  else:
    for i in serie:
      somme = 0
      somme += i 
      return somme / len(serie)

print(moyenne([]))
"""
"""
def NombreOccurence(chaine,car):
  compteur = 0
  for i in chaine:
    if i == car:
      compteur += 1
  return compteur
print(NombreOccurence("aazdughayizdg","a"))
"""
"""

def PositionChar(chaine,car,pos=0):
  for i in range(len(chaine)):
    if chaine[i] == car:
        pos= i
        print(pos)
  
PositionChar("Bonjour tout le monde","o")
"""

"""
def repondre (nom,annee,mois):
  print(f" vous vous nommez {nom} et vous avez {(2021 - annee )} ans ")

nom = input("votre nom")
annee = int(input("année de naissance"))
moi =input("votre moi de naissance ")
repondre(nom,annee,moi)
"""
"""
tableau pythagore 
for g in range(1,11):
  
  for i in range(1,11):
    if (g == 1 and i == 1):
      print("      " , end="" )
    print(f'|  {i*g}  ',end="")
    
    if(i == 10):
      print('\n ====================================================================')
"""

"""
nb = int(input("entrez un nombre < 256 "))
result =  []

while(nb != 0):
  r = int(nb%2)
  nb = int(nb/2)
  result.append(r)
  result.reverse()
for i in result:
  print(i,end="")
"""


nb = int(input("entrez un nombre < 256 "))
result =  []
compteur = 0;
while(nb != 0):
  r = int(nb%2)
  nb = int(nb/2)
  result.append(r)

result.reverse()

for i in result:
  if compteur % 4 == 0 and compteur != 0:
    print(" ", end="")
  print(i,end="")
  compteur += 1

