
class Case:
    def __init__(self,contenu):
        self.contenu=contenu
        return None
   
    def est_vide(self):
        return self.contenu==' '
   
    def entre(self):
        self.contenu="X"
        return None
   
    def sort(self):
        self.contenu=' '
        return None
   
    def est_finale(self):
        return self.contenu=='O'
   
    def __str__(self):
        return str(self.contenu)
   
    def __repr__(self):
        return str(self)
   
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


class Voiture:
    def __init__(self,position,carte):
        self.carte=carte
        self.position=position
        self.vecteur=[0,0]
        self.touches={'z':[1,0],'s':[-1,0],'q':[0,-1],'d':[0,1]}
    def deplacement(self,touche='l'):
        self.carte(self.position[0],self.position[1]).sort()
        if touche in self.touches:
            self.vecteur[0]=self.vecteur[0]+self.touches[touche][0]
            self.vecteur[1]=self.vecteur[1]+self.touches[touche][1]
        dest=[self.position[0]+self.vecteur[0],self.position[1]+self.vecteur[1]]
        init=[self.position[0],self.position[1]]
        nb_pas=self.vecteur[0]*10
        ancienne_position = init
        for t in range(nb_pas,-1,-1 ):
            
            point=[int(t/nb_pas*init[0]+(1-t/nb_pas)*dest[0]),int(t/nb_pas*init[1]+(1-t/nb_pas)*dest[1])]
            if not self.carte(point[0],point[1]).est_vide() :
                self.carte(self.position[0],self.position[1]).sort()
                self.vecteur=[0,0]
                self.position = ancienne_position
                #self.position=[int((t-1)*0.1*init[0]+(2-t)*0.1*dest[0]),int((t-1)*0.1*init[1]+(2-t)*0.1*dest[1])]
                self.carte(-dest[0],dest[1]).entre()
                return None
        self.position=dest
        self.carte(-dest[0],dest[1]).entre()
        return None
    def __str__(self):
        return str(self.vecteur)

def prov():
    carte=Carte('Objets\CourseVoiture\petit.txt')

    test = Voiture([-8,3],carte)
    print()
    for i in range(100):
        
        test.deplacement(input())
        print(carte)
        print(test)

    print(test)
prov()
