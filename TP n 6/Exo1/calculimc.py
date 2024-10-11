def calculIMC():
    try:
        poids = float(input("Entrez votre poids en kg : "))
        if poids <= 0:
            print("Le poids doit être supérieur à zéro.")
            return   
    except :
        print("Ce n'est pas un nombre valide.")
        return   

    try:
        taille = float(input("Entrez votre taille en cm : ")) / 100
        if taille <= 0:
            print("La taille doit être supérieure à zéro.")
            return   
    except :
        print("Ce n'est pas un nombre valide.")
        return   

    imc = poids / (taille ** 2)
    print("Votre IMC est de", imc)
    return imc  