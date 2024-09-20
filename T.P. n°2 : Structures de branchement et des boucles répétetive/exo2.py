from random import randint

nombre1 = randint(1,100)
nombre2 = randint(1,100)

demande = int(input(f"Calcule la somme de {nombre1} et {nombre2} : "))
print(type(demande))

somme = nombre1+nombre2
if (demande==somme) :
    print ("Félicitation")
else :
    print ( "Ressayer ou quitter")