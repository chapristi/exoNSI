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



#extend va nous eviter d'avoir un tableau dans un tableau
list = ["chien","chat","petit"]
list.extend(["chine","df"])

print(list)
    
https://mathete.net/nsi/
  
  
  
  
  
  
  
  
  
  #for i in range(0,101):
  #print(i)

'''
nbr = int(input("entrez un nombre entre 10 et 100"))
if nbr < 10:
  print("le nombre enbtré est trop petit")
elif nbr>100:
  print("le nombre entré est trop grand ")
else:
  print("le nombre entré est correct")
  '''

'''
def saisir():
  number_return = []
  while True:
    nbr = int(input("entrez un nombre entre 10 et 100"))
    if nbr < 0:
      break
    else:
      number_return.append(nbr)
  return number_return 



saisir = saisir()
print(saisir)

multiple_trois = []
for i in saisir:
  if i%3==0:
    multiple_trois.append(i)

print(multiple_trois)
'''

'''
def methode(valeur):n
  x =1 
  for i in range(10):
    x = (x+valeur/x)/2
  return x
for i in range(0,20):
  print(methode(i))
  print("----")
'''
'''

a = int(input("entrez la vealeur de a "))
b = int(input("entrez la valeure de b "))
c = int(input("entrez la valeure de c"))

x = a
for i in range(b):
  x = (x+c/x)/2
print(x)


'''

'''

phrase = input("entrez une phrase")
replace = phrase.replace(" ","")
split = phrase.split(" ")

compteurMots = 0 
compteurLettres = 0
for i in replace:
 compteurLettres+=1

print(f"le nombre de charactere est de {compteurLettres}")



for i in split:
  compteurMots += 1

print(f"le nombre de mot est de {compteurMots}")

'''




message  = input("entrez un message")


print(type(message))

l_message = []


for i in range(0, len(message)):
  l_message.append(ord(message[i]))

print(message)
print(l_message)


cle  = input("entrez une clé")
l_cle = []

for f in range(0, len(cle)):
  l_cle.append(ord(cle[f]))

print(l_cle)

# ' ' => 32 
# z => 122
# ~ => 126


l_secret = []
try:
  for s in range(0,len(l_message)):

  
    #print(l_cle[s])
    #print( l_message[s])
    #print(l_cle[s] +  l_message[s])

  

    
   
      print(l_cle[s])
      print( l_message[s])
      print(l_cle[s] +  l_message[s])

      l_secret.append(l_cle[s] +  l_message[s])
      print(chr(l_cle[s] +  l_message[s]))

except IndexError:
  for z in range(0,len(l_cle)):
      l_secret.append(l_cle[z] +  l_message[s])
      print(chr(l_cle[z] +  l_message[z]))


print(l_secret)

secret = ""
for i in l_secret:

  secret += chr(i)


print(secret)






phrase=input("entrezlaphraseàcoder:\n")
l_phrase=[]

for c in phrase:
  l_phrase.append(ord(c))


print(l_phrase)
cle=input("entrezlaclé:\n")
cle=cle.upper()
l_cle=[]
for c in cle:
  l_cle.append(ord(c))
print(l_cle)
l_secret=[]
secret=""
for index in range(len(l_phrase)):
  l_secret.append(l_phrase[index]+l_cle[index%len(l_cle)])

  print("listesecret:")
  print(l_secret)
for index in range(len(l_phrase)):
  if(l_secret[index] <=126):
    secret+=chr(l_secret[index])
  else:
    secret+=chr(l_secret[index]+32-126)
print("secret:")
print(secret)






















'''
compteur = 0 
for i in range(0,10000):
  if compteur == 101:
    break
  if i % 3 == 0:
    print(i)
    compteur+=1
'''

'''
compteur = 0 
for i in range(0,10000):
  if compteur == 100:
    break
  if i % 3 == 0:
    print(i)
    compteur+=1
'''

'''
compteur = 0 
for i in range(0,10000):
  if compteur == 100:
    break
  if i % 3 == 0:
    print(i)
    compteur+=1
  elif i % 5 == 0:
     print(i)
     compteur+=1


'''
'''

from random import randint

a = randint(1,999)
print(a)
'''



from random import randint
a = randint(1,1000)
essaies = 0 
while True:
 
 userEnter =  int(input('entrez un nombre'))
 essaies += 1 
 if userEnter < a :
   print("Trop petit")
 elif userEnter > a : 
   print("Trop grand")
 else:
   print(f"Bravo vous avez trouvé en {essaies} essaies")
   break





  
  
from random import randint

userChoice  = int(input('choissisez un nombre en 1 et 1000'))




print("l'ordinateur va commencer a chercher votre nombre")
print("....")
d = 1000
c = 1


while True :
  
  a = randint(c,d)
  print(f"{a}nombre choisi par l'ordi " )
  #entrez 1 si le nombre proposé est trop petit , 2 si il est trop grand et #3 si c'est gagné pas de triche svp ;) 
  
  userHelp = int(input("hop"))

  if userHelp == 1:
    if userChoice < a:
      print("interdit a la triche le jeu s'arrete ;)")
      break
    c = a
    
    
  elif userHelp==2:
    if userChoice > a:
      print("interdit a la triche le jeu s'arrete ;)")
      break
    d = a

  
  elif userHelp ==3:
    if userChoice != a:
      print("interdit a la triche le jeu s'arrete ;)")
      break
    print("Bon je crois que j'ai gagné")
    break

    
    
    
    
    
    
    '''
premiers = [1]
def est_premier(test):
  premier  = True
  for i in range(1,10):
    print(9%2)

    
    if  test != 2 and test % 2== 0 or test == 9 :
      
      premier = False
    return premier





for i in range(2,10):
  if(est_premier(i)):
    premiers.append(i)
print(premiers)
> 2 > 2 > 2 
'''



  from time import sleep,localtime




def afficher_horloge():
  t = localtime()
  print(t)
  print(t.tm_sec)



while True:
  afficher_horloge()
  sleep(1)

  #cela affiche les informations sur le temps actuelle tm_year correspond aux années ...  toute les secondes 

  #sleep sert a mettre un arret dans le code il prend en parametre un int c'est en seconde  

  #voila ici la preuve on voit bien que les seconde change de 1 en 1 car on a mis un sleep de 1 
  print(localtime().tm_sec)
  sleep(1)
  print(localtime().tm_sec)



  print(localtime().tm_hour)
  print(localtime().tm_hour)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
 """
a = 2
b = 5
b,a = a,b
print(a,b)



a = 2
b = 5
c = a
a = b
b = c
print(a,b)





def AskInfos():
    prenom = input("votre prenom")
    nom = input("votre nom")
    age = int(input("votre age"))
    return  prenom,nom,age

infos = AskInfos()
print(infos[0])
print(infos[1])
print(infos[2])


"""
"""
import math
def CalculDelta():
    a = int(input("entrez la valeure de a"))
    b = int(input("entrez la valeure de b"))
    c = int(input("entrez la valeure de c "))
    return (b**2)-4*a*c,a,b,c





def CalculRacine():
    delta = CalculDelta()
    if delta[0] > 0:
        print("deux solutions possible")
        x1 = (-delta[2] + math.sqrt(delta[0]))/2*delta[1]
        print(f"x1 = {x1}")
        x2 = (-delta[2] - math.sqrt(delta[0])) / 2 * delta[1]
        print(f"x2 = {x2}")

    elif delta[0] == 0:
        print("une solution")
        x0 = (-[delta[2]]) / 2* delta[1]

    else:
        print("pas de solution reelle ")
CalculRacine()

"""


"""


t1 = 2,5
t2  = 10 , -1
t3  = t1 + t2
print(t3)
t4  = 3* t1
print(t4)
print(len(t1))
print(len(t3))
print(5 in  t1)
"""



def AskList() :
    values = []
    while True:
        a = input("entrez les valeurs que vous souhaitez")
        if str(a) == "stop":
            break
        values.append(int(a))


    return values
def TrieBulleList(tab):
    compteur = 0
    for i in range(len(tab),1, -1):
        for j in range(0, i-1):
            if tab[j+1] < tab[j]:
                compteur += 1
                tab[j] ,tab[j + 1] = tab[j + 1],tab[j]
    return tab,compteur


list = AskList()
trieBulles = TrieBulleList(list)
print(trieBulles[0])
print(f"{trieBulles[1]} de tests ont été effectués")
print("il ets possible d'ameliorer sont algorithme ")                                                          

























from random import randint
def rempliListe(nbr_entier,valeur_base,valeur_haute):
 
  liste = {}
  for i in range(0,50):
    liste[i] = randint(0,10)
  return liste

def listUniqueValues():
  new_liste = {}
  compteur = 0 
  liste = rempliListe(1,2,5)
  print(liste)
  
  for i in liste.values():
    new_liste[compteur] = i
    compteur+=1
    for g in new_liste.values():
      if i == g :
        new_liste.pop(g)
    




listUniqueValues()
























import csv;
"""
la fonction WriteNewTab nous permet de recuperer les donnees du fichier csv entré
et creer un tableau de celui ci.
"""
def WriteNewTab(file):
    tab = []
    #on ouvre le fichier
    with open(file) as file:
        array = []
        for files in file:
            #on enleve le retour a la ligne mis par default dans le tableau
            files = files[:-1]
            #on ajoute la valeure au tableau
            array.append([files])
        #retourne le tableau    
        return array
"""
la fonction PostNewFormat nous permet d'afficher les données recuperes de la fonction precedente 
et de l'affciher sous forme de tableau dans la console.
"""
def PostNewFormat():
    #appel de la fonction presedente pour recuperer les données
    tableau = WriteNewTab("samere.csv")
    #definir la ligne du tableau
    ligne = "+-----+-----+-----+-----+-----+"

    ligne1 = tableau[0][0].replace(",", "")
    ligne2 = tableau[1][0].replace(",", "")
    ligne3 = tableau[2][0].replace(",", "")
    ligne4 = tableau[3][0].replace(",", "")
    ligne5 = tableau[4][0].replace(",", "")
    print(ligne)
    #affiche la ligne du tableau grace a la boucle
    for i in ligne1:
        #condition qui verifie que nous sommes a la premiere ligne pour y ajouter |
        if i == "A":
            print("| ", end="")
        #afficher la ligne en question
        print(f"{i}",end="")
        #condition qui verifie que nous sommes apres la premiere ligne pour y ajouter |
        if i == "1":
            print("  | ", end="")
    print("\n" + ligne)
    for i in ligne2:
        if i == "A":
            print("| ", end="")
        print(f"{i}",end="")
        if i == "2":
            print("  | ", end="")
    print("\n" + ligne)
    for i in ligne3:
        if i == "A":
            print("| ", end="")
        print(f"{i}",end="")
        if i == "3":
            print("  | ", end="")
    print("\n" + ligne)
    for i in ligne4:
        if i == "A":
            print("| ", end="")
        print(f"{i}",end="")
        if i == "4":
            print("  | ", end="")
    print("\n" + ligne)
    for i in ligne5:
        if i == "A":
            print("| ", end="")
        print(f"{i}",end="")
        if i == "5":
            print("  | ", end="")
    print("\n" + ligne)
    
#apelle la fonction    
PostNewFormat()

