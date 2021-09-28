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

def PositionChar(chaine,car):
  position = []
  for i in range(len(chaine)):
    if chaine[i] == car:
       position.append(i)
  return position
print(PositionChar("ozoerzoeroo","o"))
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
      print(f"    " , end="" )
    print(f'| {i*g} ',end="")
    
    if(i == 10):
      print('\n ===============================================')
"""


