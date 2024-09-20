adresse_ip = input("Entrez une adresse IP : ")
octets = adresse_ip.split(".")

if len(octets) != 4:
    print("Erreur : L'adresse IP doit comporter exactement 4 octets séparés par des points.")
else:
    valide = True 
    for i, octet in enumerate(octets):
        if not octet.isdigit():
            valide = False
            print(f"Erreur : L'octet {octet} n'est pas un nombre valide.")
            break
        valeur = int(octet)
        if valeur < 0 or valeur > 255:
            valide = False
            print(f"Erreur : L'octet {octet} doit être compris entre 0 et 255.")
            break
    if valide:
        print("L'adresse IP est valide.")
