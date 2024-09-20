
nom_domaine = input("Entrez un nom de domaine : ")
if '.' not in nom_domaine:
    print("Erreur : Le nom de domaine doit comporter au moins un point.")
else:
    parties = nom_domaine.split('.')
    valide = True
    for partie in parties:
        if not partie.isalnum():
            valide = False
            print(f"Erreur : La partie {partie} contient des caractères non valides.")
            break
    if valide:
        extension = parties[-1]  
        if 2 <= len(extension) <= 6:
            print("Le nom de domaine est valide.")
        else:
            print("Erreur : L'extension doit contenir entre 2 et 6 caractères.")
