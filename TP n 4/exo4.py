email = input("Entrez une adresse email : ")
if email.count('@') != 1:
    print("Erreur : L'adresse email doit contenir un seul symbole '@'.")
else:
    nom_utilisateur, domaine = email.split('@')
    if '.' not in domaine:
        print("Erreur : Il doit y avoir au moins un point (.) après le symbole '@'.")
    else:
        parties_domaine = domaine.split('.')
        extension = parties_domaine[-1]
        if len(extension) < 2:
            print("Erreur : Le nom de domaine doit avoir au moins 2 caractères après le dernier point.")
        else:
            print("L'adresse email est valide.")
