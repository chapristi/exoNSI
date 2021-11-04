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
print("",end="   |  ")
for f in range(1,11):
    print(f , end="   |  ")
print()  
print(" ======================================================================")
for g in range(1,11):
  print(g,end=" ")
  if(g < 10):
      print(end=" ")
  for i in range(1,11):
    if(i*g > 9):
      print(f'|  {i*g}  ',end="")
    else:
       print(f'|  {i*g}   ',end="")
  
    if(i == 10):
      print('\n =====================================================================')
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

 


ok=False
while(ok==False):
  enters = ["1->8bits","|2->16bits" , "|3->32bits"]
  print("\n-----------------------------------")
  print("Entrezleformatdelabase:")
  for i in enters : 
    print(i, end="")
  choix = int(input("\nVotrechoix:"))
  if choix==1 or choix==2 or choix==3:
    print(f"votre choix a étéb de {enters[choix -1] }")
    nb = int(input("choisisez un nombre binaire a convetir"))
    for s in str(nb):
      if s[0] == "-": 
        print("le nombre est negatif")
        print(bin(nb))
        break
      else:
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



#retourner une liste a l'envaire deja fait a la maison

#effecer dans un eliste les element en double






moyenne = 0
totalcoef = 0
while True:
  note = int(input("votre note"))
  if note < 0 :
    break
  coef = int(input("son coeff"))
  totalcoef  += coef
  moyenne += note * coef
  


print(moyenne/totalcoef)
  

  
def inverser(mot):
  nv_mot= ""
  for i in range(1 , len(mot) + 1):
     nv_mot +=  mot[len(mot) -i ]
  return nv_mot

print(inverser("python"))
    

  
  
  
  
  def palyndrome(mot):
  nv_mot= ""
  for i in range(1 , len(mot) + 1):
     nv_mot +=  mot[len(mot) -i ]
  
  if nv_mot == mot:
    return True
  else:
    return False

print(palyndrome('kayak'))






def PlusPetit(list):
  hight = 0
  for i in list:
    if hight > i or hight == 0 :
      hight = i
    
  return hight


print(PlusGrand([3,4,5,5,6,56,5,67,5,486,786,7456,46,5798,74,54,98]))





def PlusGrand(list):
  hight = 0
  for i in list:
    hight = i
    if hight < i:
      hight = i
  return hight


print(PlusGrand([1,2,2,5,45,3,15,43,354,4,555,555555]))

    
https://mathete.net/nsi/
