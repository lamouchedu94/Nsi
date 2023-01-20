class Noeud:
    
    def __init__(self, v, g = None, d = None):
        self.v = v
        self.g = g
        self.d = d
        return None
    
    def gauche(self):
        return self.g
    
    def droite(self):
        return self.d
    
    def val(self):
        return self.v
    
    def _egal(self,n1,n2):
        if n1 is None :
            return n2 is None
        if n2 is None :
            return False
        return n1.val() == n2.val() and self._egal(n1.gauche(), n2.gauche()) and self._egal(n1.droite(),n2.droite())
    
    def _tab2arbre(self, tab, i=1):
        if i >= len(tab) or tab[i] == None:
            return None
        return Noeud(tab[i], self._tab2arbre(tab, 2*i), self._tab2arbre(tab,2*i+1))
    
    def _hauteur(self,n):
        if n==None:
            return 0 
        return 1+max(self._hauteur(n.gauche()), self._hauteur(n.droite()))

    def _taille(self,n):
        if n==None:
            return 0 
        return 1+self._taille(n.gauche()) + self._taille(n.droite())

    def _arbre2tab(self,tab=None, i=1):
        if tab == None :
            tab = [None for _ in range(2**self._hauteur(self))]
        
        tab[i] = self.val()
        if self.gauche() is not None :
            self.gauche()._arbre2tab(tab, 2*i)
        if self.droite() is not None :
            self.droite()._arbre2tab(tab, 2*i+1)
        return tab


class Arbre :
    def __init__(self, tab=None) :
        if tab == None :
            self.racine=None
        else :
            noeud = Noeud(None, None, None)
            self.racine= noeud._tab2arbre(tab)
        return None

    def taille(self) :
        return self.racine._taille(self.racine)

    def hauteur(self,n):
        if n != None:
            return 1+max(self.hauteur(n.gauche()), self.hauteur(n.droite()))
        return 0
    
    def __eq__(self):
        pass 
    
    def __str__(self) -> str:
        pass

    def __repr__(self) :
        pass

    def prefix(self) :
        pass

    def postfix(self) :
        pass

    def infixe(self) :
        pass
def prefixe(n):
    if n == None:
        return []
    return [n.val()]+prefixe(n.g)+prefixe(n.d)

def infixe(n):
    if n == None:
        return []
    return infixe(n.g)+[n.val()]+infixe(n.d)

def postfixe(n):
    if n == None:
        return []
    return postfixe(n.g)+postfixe(n.d)+[n.val()]

def affiche(n):
    if n != None:
        return "("+affiche(n.gauche())+str(n.val())+affiche(n.droite())+")"
    return ""

def same(n1,n2):
    return affiche(n1) == affiche(n2)

test = Noeud(None,None,None)
tab = [None, 1,2,3,7,4,5,None,None,6]
arbre = test._arbre2tab(tab)
#print(test._egal(arbre, arbre))
arbre = test._tab2arbre(tab)
#print(arbre._arbre2tab())

arbre=Arbre([None, 1,2,3,7,4,5,None,None,6])
print(arbre)

'''
arbre = Noeud(1, Noeud(2, None, Noeud(4)), Noeud(3, Noeud(5), None))
arbre_n = Noeud(1)
'''