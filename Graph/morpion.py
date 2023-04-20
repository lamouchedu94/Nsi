import pygame
import random
import copy

def verif(tab):
    for j in range(3):
        #horizontaux
        if tab[j][0] == tab[j][1] == tab[j][2] != 0:
            return (True, tab[j][0])
        #verticaux
        if tab[0][j] == tab[1][j] == tab[2][j] != 0:
            return (True, tab[0][j])
    #diagonale 1
    if tab[0][0] == tab[1][1] == tab[2][2] != 0:
        return (True, tab[0][0])
    #diagonale 2
    if tab[0][2] == tab[1][1] == tab[2][0] != 0:
        return (True, tab[0][2])
    #Cas nul
    if all(tab[i][j] != 0 for i in range(3) for j in range(3)):
        return (True, 3)
    
    return (False, 0)

class Bouton:
    def __init__(self,position,dimensions,couleurfond,texte,couleurtexte):
        self.position=position
        self.dimensions=dimensions
        self.couleurfond=couleurfond
        self.texte=texte
        self.couleurtexte=couleurtexte
        self.rect=None
        return None
   
    def set_couleur(self,couleurfond,couleurtexte):
        self.couleurfond=couleurfond
        self.couleurtexte=couleurtexte
        return None
       
    def set_texte(self,texte):
        self.texte=texte
        return None
       
    def draw(self,surf):
        self.rect=pygame.Rect(self.position,self.dimensions)
        text_bouton=pygame.font.SysFont('Arial',20).render(self.texte,True,self.couleurtexte)
        text_bouton_rect=text_bouton.get_rect(center=self.rect.center)
        pygame.draw.rect(surf,self.couleurfond,self.rect)
        surf.blit(text_bouton, text_bouton_rect)
        return None
       
    def est_clique(self,pos):
        return self.rect.collidepoint(pos)
   
    def get_rect(self):
        return self.rect
   
class Grille:
    def __init__(self,surf,dim_case):
        pygame.draw.line(surf,(255,255,255),(0,0),(0,dim_case*3),4)
        pygame.draw.line(surf,(255,255,255),(dim_case*3,0),(dim_case*3,dim_case*3),4)
        pygame.draw.line(surf,(255,255,255),(0,0),(3*dim_case,0),4)
        pygame.draw.line(surf,(255,255,255),(0,3*dim_case),(3*dim_case,3*dim_case),4)
        pygame.draw.line(surf,(255,255,255),(dim_case,0),(dim_case,dim_case*3),4)
        pygame.draw.line(surf,(255,255,255),(2*dim_case,0),(2*dim_case,dim_case*3),4)
        pygame.draw.line(surf,(255,255,255),(0,dim_case),(3*dim_case,dim_case),4)
        pygame.draw.line(surf,(255,255,255),(0,2*dim_case),(3*dim_case,2*dim_case),4)
        self.surf=surf
        self.dim_case=dim_case
        return None
   
    def efface(self):
        self.surf.fill((0,0,0))
        self.__init__(self.surf,self.dim_case)
        pygame.display.flip()
        return None
       
       
    def draw(self,tableau):
        for i in range(3):
            for j in range(3):
                if tableau[i][j]==1:
                    self.croix(i,j)
                elif tableau[i][j]==2:
                    self.rond(i,j)
        pygame.display.flip()
        return None
       
    def croix(self,i,j):
        pygame.draw.line(self.surf,(237,28,28),(int((i+0.05)*self.dim_case),int((j+0.05)*self.dim_case)),(int((i+0.95)*self.dim_case),int((j+0.95)*self.dim_case)),4)
        pygame.draw.line(self.surf,(237,28,28),(int((i+0.05)*self.dim_case),int((j+0.95)*self.dim_case)),(int((i+0.95)*self.dim_case),int((j+0.05)*self.dim_case)),4)
        return None
   
    def rond(self,i,j):
        pygame.draw.circle(self.surf,(39,117,238),(int((i+0.5)*self.dim_case),int((j+0.5)*self.dim_case)),int(0.475*self.dim_case),4)
        return None

def coups_possibles(tab):
    res = []
    for i in range(3):
        for j in range(3):
           if tab[i][j] == 0 :
            res.append((i,j))
    return res 

def au_pif(tab):
    cond = True
    while cond :
        x, y = random.randint(0,2), random.randint(0,2)
        if tab[x][y] == 0 :
            cond = False
    return (x,y)

def minimax(tab, joueur, profondeur, maxi=True):
    val_verif = verif(tab)
    
    if val_verif[0] and val_verif[1] == joueur :
        return (100+profondeur, None)
    if val_verif[0] and val_verif[1] == 3 or profondeur == 0 :
        return (0,None)
    if val_verif[0] and val_verif[1] != joueur :
        return (-100-profondeur, None)
    
    
    if maxi :
        maximum = (-200, ())
        for coup in coups_possibles(tab) :
            tab_c = copy.deepcopy(tab)
            tab_c[coup[0]][coup[1]] = joueur
            score = minimax(tab_c,joueur,profondeur-1,not maxi)
            
            if score[0] > maximum[0] :
                maximum = (score[0], coup)
        return maximum

    else :
        minimum = (200, ())
        for coup in coups_possibles(tab) :
            tab_c = copy.deepcopy(tab)
            tab_c[coup[0]][coup[1]] = joueur*-1+3 
            score = minimax(tab_c,joueur,profondeur-1,not maxi)
            if score[0] < minimum[0] :
                minimum = (score[0], coup)
        return minimum


def main(dim) :
    pygame.init()
    surf = pygame.display.set_mode((4*dim+dim,3*dim))
    g = Grille(surf,dim)
    run = True
    en_cours = False
    joueur = 1
    tab = [[0 for j in range(3)] for i in range(3)]
    j1 = Bouton((dim*3+dim//2, dim//5),(dim, dim//2),(255,255,255),"Joueur 1",(0,0,0))
    j1.draw(surf)
    j2 = Bouton((dim*3+dim//2, dim//5*2 + dim//2),(dim, dim//2),(255,255,255),"Joueur 2",(0,0,0))
    j2.draw(surf)
    b3 = Bouton((dim*3+dim//2, dim//5*3 + dim//2*2),(dim, dim//2),(255,255,255),"Commencer",(0,0,0))
    b3.draw(surf)
    zone_aff = Bouton((dim*3+dim//5, dim//5*4 + dim//2*3),(dim+dim//5*3, dim//2),(0,0,0),"",(0,0,0))
    zone_aff.draw(surf)

    texte_j1 = ["Joueur 1","Facile","Medium","Impossible"]
    texte_j2 = ["Joueur 2","Facile","Medium","Impossible"]
    texte_b3 = ["Recommencer","Commencer"]
    indice = [1,1,0]
    orloge = 0
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #partie IA 
            """
            Joueur = 1
            Facile = 2
            Medium = 3
            Impossible = 0 
            """        
            if orloge % 2 == 0 and en_cours and indice[0] != 1 :
                if indice[0] == 0 :
                    score, coup = minimax(tab,1, 8, True)
                elif indice[0] == 2 :
                    score, coup = minimax(tab,1,2, True)
                else : 
                    indice[0] == 3 
                    score, coup = minimax(tab,1,4,True)
                if coup == None :
                    coup = au_pif(tab)
                tab[coup[0]][coup[1]] = 1
                g.draw(tab)
                joueur = 2
                orloge += 1

            if orloge % 2 == 1 and en_cours and indice[1] != 1 :
                if indice[1] == 0 :
                    score, coup = minimax(tab,2, 8, True)
                elif indice[1] == 2 :
                    score, coup = minimax(tab,2,2, True)
                else : 
                    indice[1] == 3 
                    score, coup = minimax(tab,2,4,True)
                if coup == None :
                    coup = au_pif(tab)
                tab[coup[0]][coup[1]] = 2
                g.draw(tab)
                joueur = 1
                orloge += 1

            #Partie Jeu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    pos = pygame.mouse.get_pos()
                    case = (pos[0]//dim,pos[1]//dim)
                    
                    if case[0] < 3 and en_cours : # Si est dans la grille de jeu
                        if tab[case[0]][case[1]]==0:
                            if joueur == 2 :
                                tab[case[0]][case[1]]=2
                                g.draw(tab)
                                joueur = 1
                            elif joueur == 1:
                                tab[case[0]][case[1]]=1
                                g.draw(tab)
                                joueur = 2
                            orloge += 1
                    else :
                        if j1.est_clique(pos) and en_cours == False:
                            j1.set_texte(texte_j1[indice[0]])
                            j1.draw(surf)
                            indice[0]+=1
                            if indice[0] == 4 :
                                indice[0] = 0
                        elif j2.est_clique(pos) and en_cours == False:
                            j2.set_texte(texte_j2[indice[1]])
                            j2.draw(surf)
                            indice[1]+=1
                            if indice[1] == 4 :
                                indice[1] = 0
                        elif b3.est_clique(pos) :
                            b3.set_texte(texte_b3[indice[2]])
                            b3.draw(surf)
                            indice[2] += 1
                            en_cours = True
                            if indice[2] == 2 :
                                en_cours = False
                                indice[2] = 0
                                tab = [[0 for j in range(3)] for i in range(3)]
                                g.efface()
                                g.draw(tab)
                                j1.draw(surf)
                                j2.draw(surf)
                                b3.draw(surf)
            
            #Partie Verification
            val_verif = verif(tab)
            if val_verif[0] :
                couleurs = [(237,28,28),(39,117,238), (255,255,255)]
                en_cours = False
                orloge = 0
                joueur = 1
                if val_verif[1] != 3 :
                    zone_aff.set_couleur((0,0,0), couleurs[val_verif[1]-1])
                    zone_aff.set_texte(f"Le joueur {val_verif[1]} a gagné")
                else : 
                    zone_aff.set_couleur((0,0,0), couleurs[2])
                    zone_aff.set_texte("Partie Nulle")
                zone_aff.draw(surf)
            if en_cours == True :
                j1.set_couleur((168, 177, 186),(0,0,0))
                j2.set_couleur((168, 177, 186),(0,0,0))
                j1.draw(surf)
                j2.draw(surf)
            else :
                j1.set_couleur((255, 255, 255),(0,0,0))
                j2.set_couleur((255, 255, 255),(0,0,0))
                j1.draw(surf)
                j2.draw(surf)            
            

            pygame.display.flip()
pygame.quit()
main(150)