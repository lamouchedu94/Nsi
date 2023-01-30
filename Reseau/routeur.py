class Reseau : 
    def __init__(self, liste_routeur=None) -> None:
        if liste_routeur == None :
            self.liste_r = []
        else :
            self.liste_r = liste_routeur
        return None
    
    def ajout(self, nom, connection):
        for r in self.liste_r :
            if nom == r.name() :
                return None
        self.liste_r.append(Routeur(nom, connection))
        return 1

    def __str__(self) -> str:
        res = ""
        for r in self.liste_r :
            res += r.name() + " " + str(r.connec()) + "\n"
        return res

class Routeur :
    def __init__(self, nom, connection = None) -> None:
        if connection == None :
            self.connection = []
        else :
            self.connection = connection
        self.nom = nom
        return None
    
    def name(self):
        return self.nom
    
    def connec(self):
        return self.connection

    def table(self):
        
        pass

reseau = Reseau()
reseau.ajout("A", ["B", "C"])
reseau.ajout("B", ["A", "C", "F"])
reseau.ajout("C", ["A","B","D"])
reseau.ajout("D", ["C", "E"])
reseau.ajout("E", ["D", "F"])
reseau.ajout("F", ["E", "G", "B"])
print(reseau)

"""
reseau.ajout("seveur", ["192.168.1.0/24"])
reseau.ajout("R1", ["192.168.1.0/24", "10.1.1.0/30"])
reseau.ajout("R3", ["10.1.2.0/30", "10.1.4.0/30", "10.1.3.0/28", "10.1.1.0/30"])
reseau.ajout("R2", ["10.1.2.0/30", "10.1.6.0/30"])
reseau.ajout("R4", ["10.1.3.0/28", "10.1.5.0/28"])
reseau.ajout("R5", ["10.1.6.0/30", "10.1.5.0/28","10.1.4.0/30", "10.1.7.0/28"])
reseau.ajout("R6", ["10.1.7.0/28", "192.168.6.0/24"])
reseau.ajout("client", ["192.168.6.0/24"])
print(reseau)
"""