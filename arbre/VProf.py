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
        return self._egal(n1.gauche(),n2.gauche()) and self._egal(n1.droite(),n2.droite())
 
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
    
    def _affiche(self,n):
        if n != None:
            return "("+self._affiche(n.gauche())+str(n.val())+self._affiche(n.droite())+")"
        return ""
    
    def _prefixe(self,n):
        if n == None:
            return []
        return [n.val()]+self._prefixe(n.g)+self._prefixe(n.d)
     
    def _infixe(self,n):
        if n == None:
            return []
        return self._infixe(n.g)+[n.val()]+self._infixe(n.d)
     
    def _postfixe(self,n):
        if n == None:
            return []
        return self._postfixe(n.g)+self._postfixe(n.d)+[n.val()]
    
    def _largeur(self,n):
        if n==None:
            return []
        file=[n]
        res=[]
        while file!=[]:
            if file[0].gauche()!=None:
                file.append(file[0].gauche())
            if file[0].droite()!=None:
                file.append(file[0].droite())
            res.append(file.pop(0).val())
        return res
    
    def _ajoute_abr(self,n,val):
        """n est non None"""
        if val<n.val():
            if n.g==None:
                n.g=Noeud(val)
                return None
            self._ajoute_abr(n.g,val)
        if val>n.val():
            if n.d==None:
                n.d=Noeud(val)
                return None
            self._ajoute_abr(n.d,val)
        return None
    
    def _min_abr(self,n):
        if n.gauche() is None:
            return n.val()
        return self._min_abr(n.gauche())
    
    def _max_abr(self,n):
        if n.droite() is None:
            return n.val()
        return self._max_abr(n.droite())
    
    def _recherche_abr(self,n,val,noeud=False):
        """renvoie True si la valeur est dans l'arbre.
        en passant le paramètre noeud à True, renvoie le noeud si la valeur est dans l'arbre"""
        if n==None:
            return False
        if val<n.val():
            return self._recherche_abr(n.gauche(),val,noeud)
        if val>n.val():
            return self._recherche_abr(n.droite(),val,noeud)
        if noeud==False:
            return True
        return n
    
    def _pop_min_abr(self,n):
        """la racine doit avoir au moins un fils gauche non None"""
        if n.gauche().gauche()==None:
            val=n.gauche().val()
            n.g=n.gauche().droite()
            return val
        return self._pop_min_abr(n.gauche())
    
    def _supprime_abr(self,val):
        """val doit être dans un noeud qui a un fils gauche non None"""
        n=self._recherche_abr(self,val,True)
        n.v=self._pop_min_abr(n)
        return None
            
                               
 
class Arbre:
    def __init__(self,tab=None):
        if tab==None:
            self.racine=None
        else:
            noeud=Noeud(None,None,None)
            self.racine=noeud._tab2arbre(tab)
        return None
 
    def taille(self):
        if self.racine==None:
            return 0
        return self.racine._taille(self.racine)
 
    def hauteur(self):
        if self.racine==None:
            return 0
        return self.racine._hauteur(self.racine)
 
    def __eq__(self,arbre):
        if self.racine is None:
            return arbre.racine is None
        return self.racine._egal(self.racine,arbre.racine)
 
    def __str__(self):
        if self.racine==None:
            return '()'
        return self.racine._affiche(self.racine)
        
    def __repr__(self):
        return str(self)
 
    def prefixe(self):
        if self.racine==None:
            return []
        return self.racine._prefixe(self.racine)
 
    def postfixe(self):
        if self.racine==None:
            return []
        return self.racine._postfixe(self.racine)
 
    def infixe(self):
        if self.racine==None:
            return []
        return self.racine._infixe(self.racine)
    
    def largeur(self):
        if self.racine==None:
            return []
        return self.racine._largeur(self.racine)
 
class Abr:
    def __init__(self,tab=None):
        if tab==None:
            self.racine=None
        else:
            noeud=Noeud(None,None,None)
            self.racine=noeud._tab2arbre(tab)
        return None
 
    def taille(self):
        if self.racine==None:
            return 0
        return self.racine._taille(self.racine)
 
    def hauteur(self):
        if self.racine==None:
            return 0
        return self.racine._hauteur(self.racine)
 
    def __eq__(self,arbre):
        if self.racine is None:
            return arbre.racine is None
        return self.racine._egal(self.racine,arbre.racine)
 
    def __str__(self):
        if self.racine==None:
            return '()'
        return self.racine._affiche(self.racine)
        
    def __repr__(self):
        return str(self)
 
    def prefixe(self):
        if self.racine==None:
            return []
        return self.racine._prefixe(self.racine)
 
    def postfixe(self):
        if self.racine==None:
            return []
        return self.racine._postfixe(self.racine)
 
    def infixe(self):
        if self.racine==None:
            return []
        return self.racine._infixe(self.racine)
    
    def largeur(self):
        if self.racine==None:
            return []
        return self.racine._largeur(self.racine)
    
    def ajoute(self,val):
        if self.racine==None:
            self.racine=Noeud(val)
            return None
        self.racine._ajoute_abr(self.racine,val)
        
    def mini(self):
        assert self.racine is not None, 'arbre vide'
        return self.racine._min_abr(self.racine)
    
    def maxi(self):
        assert self.racine is not None, 'arbre vide'
        return self.racine._max_abr(self.racine)
    
    def recherche(self,val):
        if self.racine==None:
            return False
        return self.racine._recherche_abr(self.racine,val)
    
    def supprime(self,val):
        pass
    
def tri_abr(liste):
    a=Abr()
    for val in liste:
        a.ajoute(val)
    return a.infixe()
    
    
            
        
    
test=Arbre([None,4,2,6,1,3,5,7])
test1=Abr()
test1.ajoute(4)
test1.ajoute(2)
test1.ajoute(6)
test1.ajoute(1)
test1.ajoute(7)
test1.ajoute(5)
tab=[5,2,4,6,8,2,35,9,2,8] 