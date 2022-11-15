class Case:
    def __init__(self,contenu):
        self.cont=contenu
        return None
   
    def est_vide(self):
        return self.cont==' '
   
    def est_finale(self):
        return self.cont=='A'
    
    def est_mur(self):
        return self.cont=='#'
   
    def __str__(self):
        return str(self.cont)
   
    def __repr__(self):
        return str(self)
   
    def contenu(self):
        return self.cont
           
   
class Carte:
    def __init__(self,nomfichier):
        with open (nomfichier) as carte:
            self.plan=[[Case(carac)for carac in ligne] for ligne in carte.readlines()]
        return None
           
    def __str__(self):
        res=''
        for i in range (len(self.plan)):
            for j in range (len(self.plan[i])):
                res+=str(self.plan[i][j])
        return res      
   
    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return len(self.plan)-1
    
    def nb_colonnes(self):
        return len(self.plan[0])
    
    def __getitem__(self,coord):
        return self.plan[coord[0]][coord[1]]
    
    def deplacement(self,position,vecteur,check,nb_checkpoints=0):
        dest=[position[0]+vecteur[0],position[1]+vecteur[1]]
        nb_pas=(max(abs(vecteur[0]*10),abs(vecteur[1]*10)))
        lastpoint=position
        for t in range(nb_pas):
            point=[int(t/nb_pas*dest[0]+(1-t/nb_pas)*position[0]),int(t/nb_pas*dest[1]+(1-t/nb_pas)*position[1])]
            if [point[0]+0.5,point[1]+0.5]!=lastpoint:
                if not self.plan[point[0]][point[1]].est_vide():
                        if not self.plan[point[0]][point[1]].est_mur():
                            if self.plan[point[0]][point[1]].contenu()=='A':
                                if check==[str(i) for i in range(nb_checkpoints+1)]:
                                    check.append('A')
                            elif int(self.plan[point[0]][point[1]].contenu())==int(check[-1])+1:
                                check.append(self.plan[point[0]][point[1]].contenu()) 
                        else:
                            #vecteur=[0,0]
                            #break
                            return lastpoint,[0,0],check
                lastpoint=[point[0]+0.5,point[1]+0.5]
        return lastpoint,vecteur,check      
 

class Voiture:
    def __init__(self,position,carte):
        self.carte=carte
        self.position=position
        self.vecteur=[0,0]
        self.touches={'z':[-1,0],'s':[1,0],'q':[0,-1],'d':[0,1]}
        self.check=['0']
        
    def demande_deplacement(self,touche='l',nb_checkpoints=0):
        if touche in self.touches:
            self.vecteur[0]=self.vecteur[0]+self.touches[touche][0]
            self.vecteur[1]=self.vecteur[1]+self.touches[touche][1]
        self.position,self.vecteur,self.check=self.carte.deplacement(self.position,self.vecteur,self.check,nb_checkpoints)
        return None
    
    def fini(self,nb_checkpoints=0):
        if self.check==[]:
            return False
        return self.check==[str(i) for i in range(nb_checkpoints+1)]+['A']
    
    def __str__(self):
        res=''
        for i in range (len(self.carte)): 
            for j in range (self.carte.nb_colonnes()): 
                if [i+0.5,j+0.5]==self.position:
                    res+='¤'
                else:
                    res+=str(self.carte[i,j]) 
        return res          
    
def jeu(fichier,depart,nb_checkpoints=0):
    carte=Carte(fichier)
    voit=Voiture(depart,carte)
    print(voit)
    cpt=0
    while not voit.fini(nb_checkpoints):
        t=input('touche ? ')
        voit.demande_deplacement(t,nb_checkpoints)
        cpt+=1
        print('vecteur:',voit.vecteur,'compteur',cpt)
        print(voit)
    print('gagné en ',cpt,' coups !')
    return None

jeu('carte.txt',[3.5,5.5],3)
    

  






