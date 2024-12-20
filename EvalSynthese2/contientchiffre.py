def contient_chiffre(mot_de_passe):
    for caractere in mot_de_passe:
        if caractere.isdigit():  
            # print("Le mot de passe contient bien un mot de passe")
            return True  
    print("Le mot de passe doit contenir au moins un chiffre.")
    return False  

# contient_chiffre('Younes95')