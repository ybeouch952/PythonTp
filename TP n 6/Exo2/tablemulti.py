def tablemulti():
    try :
        nombre = int(input("Entrez un nombre entier positif : "))
        if nombre < 0 :
            print ("Veillez entrez un nombre positif ! ")
            return
    except :
        print("Ce n'est pas un nombre valide.")
        return
    print ("Table de multiplication de ", nombre )
    for i in range (11) :
        print( nombre, "x", i , "= ", nombre*i)

