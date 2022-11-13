# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 20:56:25 2022

@author: Laurent
"""

class Case:
    def __init__(self,contenu):
        self.cont=contenu
        self.last = ""
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

    def entre(self):
        self.last = self.cont
        self.cont = 'X'
        return None
    
    def sort(self):
        self.cont = self.last
        
        return None

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
    
    def deplacement(self,position,vecteur,check=['0'],nb_checkpoints=0):
        """effectue le plus grand déplacement possible en partant de position,
        dans la direction indiquée par vecteur, d'une longueur maximale indiquée
        par vecteur.
        arguments: position: couple, vecteur: couple
        retourne: nouvelle position, vecteur si la voiture n'a pas rencontré de mur, [0,0] sinon"""
        self.position = position
        self.vecteur = vecteur
        dest=[self.position[0]+self.vecteur[0],self.position[1]+self.vecteur[1]]
        init=[self.position[0],self.position[1]]
        nb_pas=max(abs(self.vecteur[0]*10),abs(self.vecteur[1]*10))
        if nb_pas != 0 :
            for t in range(nb_pas+1):
                point=[int(t/nb_pas*dest[0]+(1-t/nb_pas)*init[0]),int(t/nb_pas*dest[1]+(1-t/nb_pas)*init[1])]
                case = self.plan[point[0]][point[1]].contenu()
                if len(case) != 0:
                    if 48<ord(case)<57 :
                        check[0]=case
                if case =='#':
                    self.vecteur=[0,0]
                    self.position=[int((t-1)/nb_pas*dest[0]+(1-(t-1)/nb_pas)*init[0]),int((t-1)/nb_pas*dest[1]+(1-(t-1)/nb_pas)*init[1])]
                    return self.position,self.vecteur,check
        
        return dest, self.vecteur, check


'''
c = Carte("Objets\CourseVoiture2\carte.txt")
print(c.deplacement([1,1], [1,0]))
print(c.deplacement([2,1], [1,0]))
'''

class Voiture:
    def __init__(self,position,carte):
        self.carte=carte
        self.position=position
        self.vecteur=[0,0]
        self.touches={'z':[-1,0],'s':[1,0],'q':[0,-1],'d':[0,1]}
        self.check=['0']
        
    def demande_deplacement(self,touche='l',nb_checkpoints=0):
        """en fonction de la touche donnée, et du vecteur, calcule un nouveau
        vecteur déplacement, puis appelle la méthode deplacement de Carte,
        pour mettre à jour position et vecteur"""
        self.carte.plan[int(self.position[0])][int(self.position[1])].sort()
        if touche in self.touches:
            self.vecteur[0]=self.vecteur[0]+self.touches[touche][0]
            self.vecteur[1]=self.vecteur[1]+self.touches[touche][1]
        self.position,self.vecteur, self.check = self.carte.deplacement(self.position,self.vecteur)
        print(self.position, self.vecteur, self.check)
        self.carte.plan[int(self.position[0])][int(self.position[1])].entre()
        
        pass
    
    def fini(self,nb_checkpoints=0):
        """retourne True si la voiture a franchi la ligne d'arrivée"""
        if nb_checkpoints == int(self.check[0]) :
            return self.carte.plan[int(self.position[0]+1)][int(self.position[1])].est_finale()
        
    
    def __str__(self):
        """renvoie une chaîne de caractère représentant le circuit et la voiture"""
        pass

def jeu(fichier,depart,nb_checkpoints=0):
    """
    paramètres: fichier est une chaine de caractères qui indique le chemin d'accès 
    au fichier de la carte, départ est un couple qui indique la position de départ
    de la voiture
    """
    carte=Carte(fichier)
    voit=Voiture(depart,carte)
    print(carte)
    cpt=0
    while not voit.fini(nb_checkpoints):
        t=input('touche ? ')
        voit.demande_deplacement(t,nb_checkpoints)
        cpt+=1
        print('vecteur:',voit.vecteur,'compteur',cpt, 'check:',voit.check)
        print(carte)
    print('gagné en ',cpt,' coups !')
    return None

jeu("Objets\CourseVoiture2\carte.txt",[-11,3],3)