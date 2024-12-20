from contientcaracterespecial import contient_caractere_special
from contientchiffre import contient_chiffre
from contientmajusculeetminuscule import contient_majuscules_et_minuscules
from estlongeurvalide import est_longueur_valide

def verifier_mot_de_passe(mot_de_passe):
    if contient_majuscules_et_minuscules(mot_de_passe) and contient_caractere_special(mot_de_passe) and contient_chiffre(mot_de_passe) and est_longueur_valide(mot_de_passe):
        print("Mot de passe sécurisé")
        return True
    else:
        print("Mot de passe non sécurisé")
        return False



verifier_mot_de_passe('Younes95@')