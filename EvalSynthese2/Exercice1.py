
def saisir_mac():
    continuer = True
    while continuer:  
        mac = input("Saisir l'adresse MAC: ")
        if est_mac_valide(mac):
            print(f"Adresse MAC {mac} est valide.")
            continuer = False
        else:
            print(f"Adresse MAC {mac} est invalide.")

def est_mac_valide(mac):
    if mac.count(":") == 5:
        groupe = mac.split(":")
    elif mac.count("-") == 5:
        groupe = mac.split("-")
    else:
        print("L'adresse MAC doit contenir 5 séparateurs")
        return False
    if est_groupe_hex_valide(groupe):
        return True
    else:
        return False

def est_groupe_hex_valide(groupe):
    for partie in groupe:
        if len(partie) != 2:
            print(f"Erreur : La partie {partie} doit contenir exactement 2 caractères.")
            return False
        for caractere in partie:
            if caractere not in "0123456789ABCDEFabcdef": 
                print(f"Erreur : La partie {partie} contient des caractères non valides.")
                return False
    return True

saisir_mac()
