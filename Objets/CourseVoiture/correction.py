
class Case:
    def __init__(self,contenu):
        self.contenu=contenu
        return None
   
    def est_vide(self):
        return self.contenu==' '
   
    def entre(self,lem):
        assert self.est_vide(),"la case n'estpas vide"
        self.contenu=lem
        return None
   
    def sort(self,lem):
        #assertself.contenu==  
        self.contenu=' '
        return None
   
    def est_finale(self):
        return self.contenu=='O'
   
    def __str__(self):
        return str(self.contenu)
   
    def __repr__(self):
        return str(self)
   
   
   
   
class Carte:
    def __init__(self,nomfichier):
        with open (nomfichier) as carte:
            self.plan=[[Case(carac)for carac in ligne] for ligne in carte.readlines()]
        return None
    #attributdépart
           
    def __str__(self):
        res=''
        for i in range (len(self.plan)):
            for j in range (len(self.plan[i])):
                res+=str(self.plan[i][j])
        return res      
   
    def __repr__(self):
        return str(self)
   
class Voiture:
    def __init__(self,position,carte):
        self.carte=carte
        self.position=position
        self.vecteur=[0,0]
        self.touches={'z':[0,1],'s':[0,-1],'q':[-1,0],'d':[1,0]}
    def deplacement(self,touche='l'):
        if touche in self.touches:
            self.vecteur[0]=self.vecteur[0]+self.touches[touche][0]
            self.vecteur[1]=self.vecteur[1]+self.touches[touche][1]
        dest=[self.position[0]+self.vecteur[0]+0.5,self.position[1]+self.vecteur[1]+0.5]
        init=[self.position[0]+0.5,self.position[1]+0.5]
        nb_pas=self.vecteur[0]*10
        for t in range(nb_pas):
            point=[int(t*0.1*init[0]+(1-t*0.1)*dest[0]),int(t*0.1*init[1]+(1-t*0.1)*dest[1])]
            if self.carte[point[0]][point[1]]=='#':
                self.vecteur=[0,0]
                self.position=[int((t-1)*0.1*init[0]+(2-t)*0.1*dest[0]),int((t-1)*0.1*init[1]+(2-t)*0.1*dest[1])]
                return None
        self.position=dest
        return None
    
    

carte='carte.txt'


