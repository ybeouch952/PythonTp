def classification(imc):
    if imc < 16:
        print("Vous êtes en maigreur extrême !")
    elif 16 <= imc < 19:
        print("Vous êtes en maigreur.")
    elif 19 <= imc < 21:
        print("Vous êtes en minceur.")
    elif 21 <= imc < 25:
        print("Vous êtes normal.")
    elif 25 <= imc < 30:
        print("Vous êtes en surcharge.")
    elif 30 <= imc < 35:
        print("Vous êtes en obésité modérée.")
    elif 35 <= imc < 40:
        print("Vous êtes en obésité sévère.")
    else:
        print("Vous êtes en obésité grave.")
