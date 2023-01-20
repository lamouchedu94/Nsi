def nb_arbre(nb_noeuds):
    if nb_noeuds <= 1 :
        return 1
    res = 0
    for g in range(nb_noeuds) :
        res += nb_arbre(g)*nb_arbre(nb_noeuds-g-1)
    return res

print(nb_arbre(14))

"""
12345 pre
24153 in
42531 post
"""

class Noeud:
    
    def __init__(self, valeur, gauche=None, droite=None):
        self.val = valeur 
        self.g = gauche
        self.d = droite 
        return None
    
    def gauche(self):
        return self.g
    
    def droite(self):
        return self.d
 
    def valeur(self):
        return self.val
    
    def __str__(self):
        return str(self.val)
    
arbre = Noeud(1, Noeud(2, None, Noeud(4)), Noeud(3, Noeud(5), None))
 
class Arbre:
    
    def __init__(self,valeur='None', gauche=None, droite=None):
        self.racine = Noeud(valeur, gauche, droite) if valeur != 'None' else None
        return None
    
    def taille(self):
        if self.racine == None:
            return 0
        return 1+self.racine.gauche().taille() + self.racine.droite().taille()
        
    def hauteur(self):
        if self.racine == None:
            return 0
        return 1 + max(self.racine.gauche().hauteur(), self.racine.droite().hauteur())
 
    def _affichage(self):
        if self.racine == None:
            return ')'
        res = '('
        res += self.racine.gauche()._affichage()+','
        res += str(self.racine.valeur())+',' 
        res += self.racine.droite()._affichage()
        return res
    
    def get_racine(self):
        return self.racine
    
    def __eq__(self, arbre):
        if self.racine == None or arbre.get_racine() == None:
            return self.racine == None and arbre.get_racine() == None
        if self.racine.valeur() == arbre.get_racine().valeur():
            return self.racine.gauche() == arbre.get_racine().gauche() and self.racine.droite() == arbre.get_racine().droite()
        return False
    
 
arbre = Arbre(1, Arbre(2,None,Arbre(4)), Arbre(3,Arbre(5), None))
arbre2 = Arbre(3, Arbre(4, Arbre(2)), Arbre(5, None, Arbre(10)))
arbre3 = Arbre(1, Arbre(2,None,Arbre(4)), Arbre(3,Arbre(5), None))
#i enfant en 2i et 2i+1
def tab_to_arbre() :
    pass







