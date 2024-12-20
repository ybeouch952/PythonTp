def est_longueur_valide(mot_de_passe):
    longeur = len(mot_de_passe)
    if longeur > 7 :
        # print("La longeur est correcte")
        return True
    else :
        print("La longueur n'est pas bonne ")
        return False


# est_longueur_valide('Younesssss')