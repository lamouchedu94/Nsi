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
    
    def _ajoute_abr(self,n, val):
        """n est non None"""
        if val<n.val():
            if n.g == None :
                n.g = Noeud(val)
                return None
            self._ajoute_abr(n.g,val)
        if val> n.val() :
            if n.d == None :
                n.d=Noeud(val)
                return None
            self._ajoute_abr(n.d,val)
        return None

    def _min(self, n):
        if n.g is None : 
            return n.v
        return self._min(n.g)
    
    def _max(self, n):
        if n.d is None :
            return n.v
        return self._max(n.d)
    
    def _recherche(self, n, val):
        if n.v == val :
            return True
        if n.v > val :
            if n.g is None :
                return False
            return self._recherche(n.g, val)
        else :
            if n.d is None :
                return False
            return self._recherche(n.d, val)

class Arbre:
    def __init__(self,tab=None):
        if tab==None:
            self.racine=None
        else:
            noeud=Noeud(None,None,None)
            self.racine=noeud._tab2arbre(tab)
        return None
    
    def taille(self):
        if self.racine == None :
            return 0
        return self.racine._taille(self.racine)
    
    def hauteur(self):
        if self.racine == None :
            return 0 
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
    
    def __repr__(self,n ):
        return "Arbre (" + self.__str__(n) + ")" 
    
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

    def larg(self,n):
        file = []
        res = []
        file.append(n)
        if n == None :
            return []
        '''
        while current is not None :
            file.append(current)
            current = current.gauche()
        print(file)
        '''
        while len(file) > 0 :
            if file[0].gauche() != None :
                file.append(file[0].gauche())
            if file[0].droite() != None :
                file.append(file[0].droite())
            res.append(file.pop(0).val())
        return res


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
print(a.__repr__(a.racine))
print(a.larg(a.racine))
arbre = Noeud(1, Noeud(2, None, Noeud(4)), Noeud(3, Noeud(5), None))
arbre_n = Noeud(1)

class Abr :
    def __init__(self,tab=None):
        if tab==None:
            self.racine=None
        else:
            noeud=Noeud(None,None,None)
            self.racine=noeud._tab2arbre(tab)
        return None
    
    def taille(self):
        if self.racine == None :
            return 0
        return self.racine._taille(self.racine)
    
    def hauteur(self):
        if self.racine == None :
            return 0 
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
    
    def __repr__(self,n ):
        return "Arbre (" + self.__str__(n) + ")" 
    
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

    def larg(self,n):
        file = []
        res = []
        file.append(n)
        if n == None :
            return []
        '''
        while current is not None :
            file.append(current)
            current = current.gauche()
        print(file)
        '''
        while len(file) > 0 :
            if file[0].gauche() != None :
                file.append(file[0].gauche())
            if file[0].droite() != None :
                file.append(file[0].droite())
            res.append(file.pop(0).val())
        return res

    def recherche(self, val) :
        if self.racine is not None :
            return self.racine._recherche(self.racine, val)
        return False
    def min(self):
        if self.racine is not None :
            return self.racine._min(self.racine)
        return 0
    
    def max(self):
        if self.racine is not None :
            return self.racine._max(self.racine)
        return 0 
    
    def ajouter(self, val):
        if self.racine == None :
            self.racine = Noeud(None, val, None)
            return None
        '''
        if val<self.val():
            if self.gauche() == None :
                self.g= Noeud(val)
                return None
            self.gauche.ajoute(val)
        if val > self.val
        
        '''
        n = self.racine
        while val > n.gauche().val() or  val < n.droite().val() :
            if val < n.gauche().val() :
                n = n.gauche()
            else :
                n = n.droite()
            
            try : 
                n.gauche.val()
            except : 
                break
        print(n.val())
    '''
    def supprimer(self):
        pass

    def equilibre(self):
        pass
    '''
c = Abr([None,4,2,6,1,3,5,7])
#c.racine._ajoute_abr(c.racine, 8)
print(c.__str__(c.racine))
print(c.min())
print(c.max())
print(c.recherche(10))
