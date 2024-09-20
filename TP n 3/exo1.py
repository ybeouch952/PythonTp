# Utilisateur correct prédéfini
utilisateur_correct = "admin"

# Nombre maximum de tentatives
max_tentatives = 3

# Compteur de tentatives
tentatives = 0

while tentatives<max_tentatives:
    utilisateur = input("Entrez votre nom d'utiisateur : ")
    if utilisateur == utilisateur_correct :
        print("ok")
        break
    else : 
        tentatives = tentatives+1
        print ( "Inoccrect")
    if tentatives == max_tentatives :
        print ("nombre maximum de tentatives! ")
        break

