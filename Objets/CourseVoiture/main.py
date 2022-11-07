import time

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
        
        if commande == "s" and self.lastpos[len(self.lastpos)-1] == "z" :
            self.lastpos.pop()
        if commande == "z" and self.lastpos[len(self.lastpos)-1] == "s" :
            self.lastpos.pop()
        if commande == "q" and self.lastpos[len(self.lastpos)-1] == "d" :
            self.lastpos.pop()
        if commande == "d" and self.lastpos[len(self.lastpos)-1] == "q" :
            self.lastpos.pop()
        
        for commande in self.lastpos :
            if commande == "q" or commande == "d":
                if carte(self.position[0],self.position[1]+dicodeplacement[commande]).est_vide():
                    #print("a")
                    if not carte(self.position[0], self.position[1]).est_finale():
                        carte(self.position[0], self.position[1]).sors()
                    carte(self.position[0],self.position[1]+dicodeplacement[commande]).entre(self)
                    self.position = (self.position[0],self.position[1]+dicodeplacement[commande])
                else :
                    self.lastpos = []
                    return False

            if commande == "z" or commande == "s":
                if carte(self.position[0]+dicodeplacement[commande],self.position[1]).est_vide():
                    #print("b")
                    if not carte(self.position[0], self.position[1]).est_finale():
                        carte(self.position[0], self.position[1]).sors()
                    carte(self.position[0]+dicodeplacement[commande],self.position[1]).entre(self)
                    self.position = (self.position[0]+dicodeplacement[commande],self.position[1])
                else :
                    self.lastpos = []
                    return False
        #print(carte(self.position[0]-1, self.position[1]).test())
        
        if carte(self.position[0]-1, self.position[1]).est_finale():
            return True
        return False

def jeu(x,y,nom_fichier):
    temps = []
    utilistateur = True
    while utilistateur :
        end = True
        c = Carte(nom_fichier)
        v = Voiture(x,y)
        print(c)
        
        depart = time.time()
        
        while end :
            command = input()
            fin = v.deplacement(command,c)
            if fin :
                end = False
            print(c)
        
        temps.append(round(time.time()-depart, 2))
        for i in range(len(temps)-1):
            print(f"temps {i} : {temps[i]} ")    
        print(f"temps réalisé : {temps[len(temps)-1]}s")
        print("rejouer ? (y or n)")
        if input() != "y" :
            utilistateur = False
        
        
#jeu(-4,2,"Objets/CourseVoiture/test.txt")
#jeu(-25,8,"Objets\CourseVoiture\circuit.txt")
jeu(-19,8,"Objets/CourseVoiture/circuit2.txt")