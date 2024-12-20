# class Ordinateur():
#     def __init__(self,marque,prix):
#         self.marque = marque
#         self.prix = prix

#     def afficher(self):
#         print(self.marque)
#         print(f"{self.prix} euros")

#     def afficher_avec_retour(self):
#         return self.marque, self.prix
    
# monOrdinateur = Ordinateur("Apple", 1800)
# # monOrdinateur.afficher()
# marque, prix = monOrdinateur.afficher_avec_retour()
# print (f"L'ordintaur de marque {marque} qui coute {prix}")



class CapteurMeteo():
    def __init__(self, nom, emplcaement,dateinstallation):
        self.nom = nom
        self.emplacement = emplcaement
        self.dateinstallation = dateinstallation
    
    def afficher_infos(self):
        print (f" Le capteur s'appel {self.nom} se trouvant à {self.emplacement} et a été installé le {self.dateinstallation}")
        return 
    
monCapteurMeteo = CapteurMeteo("Younes", "Herblay", "22 Janvier")
monCapteurMeteo.afficher_infos()