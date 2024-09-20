motdepasse = input("Creez un mot de passe : ")
mdpdmd = ""
essai = 0
while mdpdmd!=motdepasse :
    mdpdmd = input("Entrez le mot de passe :")
    if mdpdmd == motdepasse :
        print ("Connexion reussi")
        break
    else :
        print ("Conexion échoue, ressayé")
        essai = essai+1
    if essai == 3 :
        print ("Accès refusé")
        break
        