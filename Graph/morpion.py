# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:26:17 2023

@author: lmartin
"""

import pygame
import random
import copy

def verif(tab) :
    #cas vertical
    count = 0
    for i in range(3):
        for ligne in tab :
            if ligne[i] == 1 :
                count += 1
        if count == 3 :
            return (True,1)
        count = 0
    for i in range(3):
        for ligne in tab :
            if ligne[i] == 2 :
                count += 1
        if count == 3 :
            return (True,2)
        count = 0

    #cas horizontal
    count = 0 
    for i in range(3):
        for j in range(3) :
            if tab[i][j] == 1 :
                count += 1
        if count == 3 :
            return (True, 1)
        count = 0 
    
    count = 0
    for i in range(3):
        for j in range(3) :
            if tab[i][j] == 2 :
                count += 1 
        if count == 3 :
            return (True, 2)
        count = 0
    
    #cas diagonales 
    #polo est un petit caca    

    count = 0
    for i in range(3) :
        if tab[i][i] == 1 :
            count += 1 
    if count == 3 :
        return (True, 1)
    
    count = 0
    for i in range(3) :
        if tab[i][i] == 2 :
            count += 1 
    if count == 3 :
        return (True, 2)

    count = 0
    ind = 0 
    for i in range(2,-1,-1) :
        if tab[i][ind] == 1 :
            count += 1
        ind += 1 
    if count == 3 :
        return (True, 1)

    count = 0
    ind = 0 
    for i in range(2,-1,-1) :
        if tab[i][ind] == 2 :
            count += 1
        ind += 1 
    if count == 3 :
        return (True, 2)
    
    #Cas nul 
    count = 0
    for i in range(3):
        for j in range(3) :
            if tab[i][j] != 0 :
                count += 1
    if count == 9 :
        return (True, 3)


    return (False,0) 

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

def ia_facile(tab):
    cond = True
    while cond :
        x, y = random.randint(0,2), random.randint(0,2)
        if tab[x][y] == 0 :
            cond = False
    return (x,y)

def ia_difficile(tab, joueur,profondeur, bool, nb):
    if verif(tab)[1] == 3 :
        return 0
    elif joueur == 1 and verif(tab)[1] == 1 :
        return 100
    elif joueur == 1 and verif(tab)[1] == 2:
        return -100
    
    pos = coups_possibles(tab)
    
    if bool :
        tab[pos[nb][0]][pos[nb][1]] = 2
        return 0 + ia_difficile(tab, 2, 0, False, nb - 1)
    else :
        tab[pos[nb][0]][pos[nb][1]] = 1
        return 0 + ia_difficile(tab, 1, 0, True, nb - 1)
tab = [[1,0,0],[0,2,0],[1,0,0]]
print(ia_difficile(tab,2,0,True,len(coups_possibles(tab))-1))    
print(tab)


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
            if orloge % 2 != 0 and en_cours and indice[0]-1 == 1: 
                val_verif = verif(tab)
                if val_verif[1] != 3 and not val_verif[0] :
                    x,y = ia_facile(tab)
                    tab[x][y] = 2
                    g.draw(tab)
                    joueur = 1
                    orloge += 1
            
            if orloge % 2 == 0 and en_cours and indice[1]-1 == 1:
                val_verif = verif(tab)
                if val_verif[1] != 3 and not val_verif[0]:
                    x,y = ia_facile(tab)
                    tab[x][y] = 1
                    g.draw(tab)
                    joueur = 2
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
#main(150)