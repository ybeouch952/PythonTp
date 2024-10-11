import random

def analyselog() :
    compteur = 0
    tentativesnb = 10
    for i in range (tentativesnb) :
        tentatives = random.randint(0,1)
        if tentatives == 0 : 
            compteur = compteur+1
            print (" Tentatives", i+1 , " Connexion échoué")
            if compteur == 3 :
                print ( " Alerte, compte bloqué")
                break
        else :
            compteur = 0
            print (" Tentatives", i+1 , " Connexion réussi")

analyselog()

# for _ in range(5):
#     print("Hello", end= "-")

# print()