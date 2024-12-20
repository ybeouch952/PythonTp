reseau = {
    1 : {"source" : "192.168.0.1", "destination": "192.168.0.2", "type" : "IPV4", "etat": "transmise"},
    2 : {"source" : "192.168.0.3", "destination": "192.168.0.4", "type" : "ARP", "etat": "perdue"},
    3 : {"source" : "192.168.0.5", "destination": "192.168.0.6", "type" : "IPV4", "etat": "transmise"},
}

def ajouter_trame(id,source,destination,type,etat,reseau) :
    if id in reseau:
        print("Erreur l'ID existe deja")
    else :
        reseau[source] = source
        reseau[destination] = destination
        reseau[type]=type
        reseau[etat]=etat
    print (reseau)


def modifier_etat_trame(id,nouvel_etat,reseau) :
    if id in reseau :
        reseau[id]["etat"]=nouvel_etat
    else :
        print ("L'id n'est pas compris")
    print(reseau)

def supprimer_trame(id,reseau):
    if id in reseau :
        del reseau[id]
    else :
        print ("L'id n'est pas compris")
    print(reseau)


def afficher_trames_par_type(type, reseau):
    trames = [f" {id} {trame}" for id, trame in reseau.items() if trame["type"] == type]
    if trames:
        print(f"Trames du type '{type}' :")
        for trame in trames:
            print(trame)

def calculer_statistique(reseau):
    total_trames = len(reseau)
    for trame in reseau :
        if reseau[trame]["etat"] == "perdue" :
            trames_perdues =+1
    print(f"Il y a en tout {total_trames} trames et {trames_perdues} trames perdues")

# ajouter_trame(4,'192.158.23.44','147.152.123.125','IPV4','perdue', reseau)
# modifier_etat_trame(2,"transmise",reseau)
# supprimer_trame(2,reseau)
# calculer_statistique(reseau)
# afficher_trames_par_type("IPV4", reseau)



