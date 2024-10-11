def connexion() :
    compteur = 0
    motdepasse = "admin123"
    motdepasseentree =""
    while motdepasse != motdepasseentree: 
        motdepasseentree = input("Entrez votre mot de passe : ")
        if motdepasseentree == motdepasse :
            print (" Accès autorisé")
        else :
            print (" Mot de passe faux ")
            compteur = compteur+1
            if compteur == 3 :
                print ( "Alerte : Accès bloqué ! ")
                break
connexion()