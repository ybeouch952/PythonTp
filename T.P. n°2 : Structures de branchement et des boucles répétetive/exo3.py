from random import randint
def exo3():
    compteur=0
    continuer = True
    while continuer :
        nombre1 = randint(1,20)
        nombre2 = randint(1,20)
        compteur+=1
        print (f"nombre1 : {nombre1} et nombre2 : {nombre2}")
        if nombre1 == nombre2 :
            print(f"Félicitation vous avez gagné au bout de {compteur} essai")
            continuer = False
        else :
            choix = input("Voulez vous rejouer ? oui / non ")
            if choix == "non" :
                    print (f"Vous avez quité après {compteur} essai")
                    continuer = False
exo3()