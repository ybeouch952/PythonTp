
while True:

    while True:
        ip_source = input("Saisir l'adresse IP source : ")
        parties_source = ip_source.split('.')
        if (len(parties_source) == 4 and 
                all(partie.isdigit() and 0 <= int(partie) <= 255 for partie in parties_source)):
            break
        else:
            print("Adresse IP source invalide, veuillez réessayer.")

    while True:
        ip_destination = input("Saisir l'adresse IP destination : ")
        parties_destination = ip_destination.split('.')
        if (len(parties_destination) == 4 and 
                all(partie.isdigit() and 0 <= int(partie) <= 255 for partie in parties_destination)):
            break
        else:
            print("Adresse IP destination invalide, veuillez réessayer.")

    protocole = input("Saisir le protocole (TCP, UDP, ICMP, etc.) : ")

    source_interne = (parties_source[0] == '192' and parties_source[1] == '168')
    destination_interne = (parties_destination[0] == '192' and parties_destination[1] == '168')

    if source_interne and destination_interne:
        statut_securite = "Sûr (les deux adresses sont internes)"
    else:
        statut_securite = "Potentiellement dangereux (adresse externe détectée)"
    print("\nAnalyse du paquet :")
    print(f"Adresse source : {ip_source}")
    print(f"Adresse destination : {ip_destination}")
    print(f"Protocole : {protocole}")
    print(f"Statut de sécurité : {statut_securite}\n")

    continuer = input("Voulez-vous analyser un autre paquet ? (oui/non) : ")
    if continuer.lower() != "oui":
        break
