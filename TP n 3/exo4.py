cleewifi = input("Entrez une clé Wi-Fi WPA ou WPA2 : ")
longeur = len(cleewifi)
if 8 <= longeur <= 63: 
    if cleewifi.isalnum():
        print("Clé valide")
    else:
        print("Erreur : la clé Wi-Fi ne doit contenir que des caractères alphanumériques (lettres et chiffres).")
else:
    print("Erreur : la clé Wi-Fi doit contenir entre 8 et 63 caractères.")