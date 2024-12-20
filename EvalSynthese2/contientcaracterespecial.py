def contient_caractere_special(mot_de_passe):
    caracteres_speciaux = "@#$%&"
    for caractere in mot_de_passe:
        if caractere in caracteres_speciaux:
            # print ( "Le mot de passe contient bien un caractère spècial")  
            return True  
    print("Le mot de passe doit contenir au moins un caractère spécial parmi @, #, $, %, &.")
    return False  


# contient_caractere_special("you@")

