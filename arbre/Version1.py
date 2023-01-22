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
        if n1 is None:
            return n2 is None
        if n2 is None:
            return False
        if n1.val()!=n2.val():
            return False
        a = self._egal(n1.gauche(),n2.gauche()) and self._egal(n1.droite(),n2.droite())
        return a
    
    def _tab2arbre(self,tab,i=1):
        if i>=len(tab):
            return None
        if tab[i]==None:
            return None
        return Noeud(tab[i],self._tab2arbre(tab,2*i),self._tab2arbre(tab,2*i+1))
    
    def _hauteur(self,n):
        if n==None:
            return 0
        return 1+max(self._hauteur(n.gauche()),self._hauteur(n.droite()))
    
    def _taille(self,n):
        if n==None:
            return 0
        return 1+self._taille(n.gauche())+self._taille(n.droite())
    
    def _arbre2tab(self,tab=None,i=1):
        if tab==None:
            tab=[None for _ in range(2**self._hauteur(self))]
        tab[i]=self.val()
        if self.gauche() is not None:
            self.gauche()._arbre2tab(tab,2*i)
        if self.droite() is not None:
            self.droite()._arbre2tab(tab,2*i+1)
        return tab
    
class Arbre:
    def __init__(self,tab=None):
        if tab==None:
            self.racine=None
        else:
            noeud=Noeud(None,None,None)
            self.racine=noeud._tab2arbre(tab)
        return None
    
    def taille(self):
        return self.racine._taille(self.racine)
    
    def hauteur(self):
        return self.racine._hauteur(self.racine)
    
    def __eq__(self,arbre):
        if arbre is None :
            return False
        if arbre.racine is None and self.racine is None :
            return True
        if arbre.racine is None or self.racine is None :
            return False
        return self.racine._egal(self.racine, arbre.racine)
    
    def __str__(self,n):
        if n != None:
            return "("+self.__str__(n.gauche())+str(n.val())+self.__str__(n.droite())+")"
        return ""
    """
    def __repr__(self,n):
        return "Arbre (" + self.__str__() + ")" 
    """
    def prefixe(self,n):
        if n == None:
            return []
        return [n.val()]+self.prefixe(n.g)+self.prefixe(n.d)
    
    def postfixe(self,n):
        if n == None:
            return []
        return self.postfixe(n.g)+self.postfixe(n.d)+[n.val()]
    
    def infixe(self,n):
        if n == None:
            return []
        return self.infixe(n.g)+[n.val()]+self.infixe(n.d)

'''
def same(n1,n2):
    return affiche(n1) == affiche(n2)
'''

a = Arbre([None,1,2,3,4,5])
b = Arbre([None,1,2,3])

print(a == b)
print(a.taille())
print(a.hauteur())
print(a.__str__(a.racine))
print(a.infixe(a.racine))
arbre = Noeud(1, Noeud(2, None, Noeud(4)), Noeud(3, Noeud(5), None))
arbre_n = Noeud(1)