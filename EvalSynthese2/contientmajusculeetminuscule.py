def contient_majuscules_et_minuscules(mot_de_passe):
    for caractere in mot_de_passe:
        if caractere.isupper():  
            return True
        if caractere.islower():  
            return True
    return False

contient_majuscules_et_minuscules('Younes')




