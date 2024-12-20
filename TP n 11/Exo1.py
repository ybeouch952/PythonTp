class EquipementReseau :
    def __init__ (self, nom:str, adresse_ip:str):
        self.nom = nom
        self.adresse_ip = adresse_ip
    
    def afficher_info(self):
        print(f"Nom : {self.nom}, Adresse Ip : {self.adresse_ip}")
    
class ConnexionReseau :
    def __init__ (self, equipement1:EquipementReseau, equipement2:EquipementReseau, type_connexion:str) :
        self.equipement1 = equipement1
        self.equipement2 = equipement2
        self.type_connexion = type_connexion

    def afficher_details(self) :
        print("Détails de la connexion :")
        print("Equipement 1")    
        print (f"Nom : {self.equipement1.nom}, Adresse Ip : {self.equipement1.adresse_ip}")
        print("Equipement 2") 
        print (f"Nom : {self.equipement2.nom}, Adresse Ip : {self.equipement2.adresse_ip}")
        print (f"Type de connexion : {self.type_connexion}")


# Création des équipements réseau
equipement1 = EquipementReseau("Switch01", "192.168.1.1")
equipement2 = EquipementReseau("Router01", "192.168.1.254")
# Création d'une connexion réseau
connexion = ConnexionReseau(equipement1, equipement2, "Ethernet")
# Affichage des détails de la connexion
connexion.afficher_details()