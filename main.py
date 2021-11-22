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
  for i in range(2,9):
    print(test*i%2)
   
    if test%i ==0 :
      
      premier = False
    return premier





for i in range(2,10):
  if(est_premier(i)):
    premiers.append(i)
print(premiers)

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


