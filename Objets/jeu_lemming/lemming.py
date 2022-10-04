import time    

class Case:
    def __init__(self, contenu):
        self.contenu = contenu
        return None
    
    def est_vide(self):
        return self.contenu == ' '
    
    def entre(self, lem):
        assert self.est_vide()
        self.contenu = lem
        return None
    
    def sors(self):
        self.contenu = ' '
        return None
    
    def est_finale(self):
        return self.contenu == "O"
    
    def __str__(self):
        return str(self.contenu)
    
    def __repr__(self):
        return str(self)
    
    def __call__(self):
        return self.contenu

class Carte:
    def __init__(self, nom_fichier):
        with open(nom_fichier) as carte:
            self.plateau = [[Case(car) for car in ligne] for ligne in carte.readlines()]
        return None
    
    def __str__(self):
        res = ''
        for i in range(len(self.plateau)):
            for car in self.plateau[i] :
                res += str(car)
        return res
    def __repr__(self):
        return str(self)
    
    def __call__(self, ligne, col):
        return self.plateau[ligne][col]


class Leming:
    
    def __init__(self, x_depart, y_depart):
        self.direction = 1
        self.position = (x_depart, y_depart)
        
    def __str__(self):
        if self.direction == 1:
            return '>'
        return '<'
    
    def deplacement(self, carte):
        if carte(self.position[0]+1, self.position[1]).est_vide():
            carte(self.position[0], self.position[1]).sors()
            carte(self.position[0]+1, self.position[1]).entre(self)
            self.position = (self.position[0]+1, self.position[1])
            return False
        
        if carte(self.position[0], self.position[1]+self.direction).est_vide():
            carte(self.position[0], self.position[1]).sors()
            carte(self.position[0], self.position[1]+self.direction).entre(self)
            self.position = (self.position[0], self.position[1]+self.direction)
            return False
        
        if carte(self.position[0], self.position[1]+self.direction).est_finale():
            return True
        
        self.direction *= -1
        
        return False
 

def jeu(x, y, nom_fichier):
    end = True
    nb_pas = 0
    c = Carte(nom_fichier)
    lemming = [Leming(x, y)]
    while end:
        #if nb_pas % entre_deux == 0:
        #    all_lemming.append(Leming(x, y))
        #    c(x, y).entre(all_lemming[len(all_lemming)-1])
        
        for i in range(len(lemming)):
            fin_inter = lemming[i].deplacement(c)
            if fin_inter:
                end = False
        
        print(c)
 
        time.sleep(0.1)
        
        nb_pas += 1

    return nb_pas
 
print(jeu(1,0, 'Objets/jeu_lemming/carte.txt'))
