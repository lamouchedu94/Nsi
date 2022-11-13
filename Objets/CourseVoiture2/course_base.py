
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
   
    def __call__(self,ligne,colonne):
        return self.contenu
    
    def __transp(self,tab):
        res=[[None for i in range(len(tab))] for j in range(len(tab[0]))]
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                res[j][i]=tab[i][j]
        return res
    
    def deplacement(self,touche='l'):
        self.touche = touche
        if touche in self.touche:
            self.vecteur[0]=self.vecteur[0]+self.touches[touche][0]
            self.vecteur[1]=self.vecteur[1]+self.touches[touche][1]
        dest=[self.position[0]+self.vecteur[0],self.position[1]+self.vecteur[1]]
        init=[self.position[0],self.position[1]]
        nb_pas=max(abs(self.vecteur[0]*10),abs(self.vecteur[1]*10))
        for t in range(nb_pas):
            point=[int(t/nb_pas*dest[0]+(1-t/nb_pas)*init[0]),int(t/nb_pas*dest[1]+(1-t/nb_pas)*init[1])]
            if self.carte.plan[point[0]][point[1]].contenu=='#':
                self.vecteur=[0,0]
                self.position=[int((t-1)/nb_pas*dest[0]+(1-(t-1)/nb_pas)*init[0])+0.5,int((t-1)/nb_pas*dest[1]+(1-(t-1)/nb_pas)*init[1])+0.5]
                return None
        self.position=dest
        return None
   
class Voiture:
    def __init__(self,position,carte):
        self.carte=carte
        self.position=position
        self.vecteur=[0,0]
        self.touches={'z':[-1,0],'s':[1,0],'q':[0,-1],'d':[0,1]}


carte=Carte('Objets\CourseVoiture2\carte.txt')   
test1=Voiture([1.5,2.5],carte)  
carte.deplacement('z')
print(carte) 






