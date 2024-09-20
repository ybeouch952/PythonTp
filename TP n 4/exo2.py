adresse_mac = input("Entrez une adresse MAC (format XX:XX:XX:XX:XX:XX) : ")
parties = adresse_mac.split(":")

if len(parties) != 6:
    print("Erreur : L'adresse MAC doit comporter exactement 6 parties séparées par des deux-points.")
else:
    valide = True 
    for i, partie in enumerate(parties):
        if len(partie) != 2:
            valide = False
            print(f"Erreur : La partie {partie} doit contenir exactement 2 caractères.")
            break
        
        if not all(c in "0123456789ABCDEF" for c in partie):
            valide = False
            print(f"Erreur : La partie {partie} contient des caractères non valides.")
            break
    if valide:
        print("L'adresse MAC est valide.")