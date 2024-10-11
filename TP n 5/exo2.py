import random

def controlebandepassante():
    seuil = 100
    compteur = 0
    for i in range(1,11):
        debit = random.randint(0, 150)
        if debit > seuil :
            compteur = compteur + 1
            print ( " Iteration" ,i ,  ": Debit réseau", debit, "dépasse le seuil de ", seuil)
            if compteur == 3 : 
                print  (" alerte vous avez depasser la limite ")
                break
        else :
            compteur = 0
            print ( " Iteration",i, " Débit réseau ", debit, "est sous controle ")

controlebandepassante()


