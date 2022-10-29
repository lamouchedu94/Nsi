class Case:
    def __init__(self, contenu):
        self.contenu = contenu
        return None
    
    def est_vide(self):
        return self.contenu == ' '
    
    def entre(self, voiture):
        assert self.est_vide()
        self.contenu = voiture
        return None

    def sors(self):
        self.contenu = ' '
        return None
    
    def test(self):
        return self.contenu

    def est_finale(self):
        print(self.contenu)
        return self.contenu == "O"
    """
    def depart(self,x,y):
        self.start = (x,y)
        return self.start
    """
    def __str__(self):
        return str(self.contenu)
    
    def __repr__(self):
        return str(self)
    
    def __call__(self):
        return self.contenu

class Carte:
    def __init__(self, nom_fichier):
        with open(nom_fichier) as carte:
            self.circuit = [[Case(car) for car in ligne] for ligne in carte.readlines()]
        return None
    
    def __str__(self):
        res = ''
        for i in range(len(self.circuit)):
            for car in self.circuit[i] :
                res += str(car)
        return res
    
    def __repr__(self):
        return str(self)
    
    def __call__(self, ligne, col):
        return self.circuit[ligne][col]

class Voiture : 
    def __init__(self, x_depart, y_depart):
        self.position = (x_depart, y_depart)
        self.lastpos = []

    def __str__(self):
        return "x"
    
    def historique(self, commande):
        self.lastpos.append(commande)

    def deplacement(self,commande, carte):
        #zqsd
        dicodeplacement = {"z":-1,"s":1,"q":-1,"d":1}
        self.historique(commande)
        a = self.lastpos
        for commande in self.lastpos :
            if commande == "q" or commande == "d":
                if carte(self.position[0],self.position[1]+dicodeplacement[commande]).est_vide():
                    #print("a")
                    carte(self.position[0], self.position[1]).sors()
                    carte(self.position[0],self.position[1]+dicodeplacement[commande]).entre(self)
                    self.position = (self.position[0],self.position[1]+dicodeplacement[commande])
                else :
                    self.lastpos = []

            if commande == "z" or commande == "s":
                if carte(self.position[0]+dicodeplacement[commande],self.position[1]).est_vide():
                    #print("b")
                    carte(self.position[0], self.position[1]).sors()
                    carte(self.position[0]+dicodeplacement[commande],self.position[1]).entre(self)
                    self.position = (self.position[0]+dicodeplacement[commande],self.position[1])
                else :
                    self.lastpos = []
        print(carte(self.position[0]-1, self.position[1]).test())
        if carte(self.position[0]-1, self.position[1]).est_finale():
            return True
        return False
def jeu(x,y,nom_fichier):
    end = True
    c = Carte(nom_fichier)
    v = Voiture(x,y)
    print(c)
    while end :
        command = input()
        fin = v.deplacement(command,c)
        if fin :
            end = False
        print(c)
        
        

jeu(-25,8,"Objets\CourseVoiture\circuit.txt")