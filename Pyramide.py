class Noeud:
    
    def __init__(self, val=None, gauche=None, droite=None):
        self.g = gauche
        self.d = droite
        self.v = val
        return None
        
    def val(self):
        return self.v
    
    def gauche(self):
        return self.g

    def droite(self):
        return self.d
        
    
def Route_plus_chere(noeud):
    if noeud.gauche() is not None and noeud.droite() is not None: 
        g = Route_plus_chere(noeud.gauche())
        d = Route_plus_chere(noeud.droite())
        if d[0] > g[0]:
            return (d[0]+noeud.val(), [noeud.val()]+d[1])
        return (g[0]+noeud.val(), [noeud.val()]+g[1])
    return (noeud.val(),[noeud.val()])

arbre = Noeud(3,Noeud(6,Noeud(8,Noeud(15),Noeud(3)),Noeud(1,Noeud(7),Noeud(12))),Noeud(4,Noeud(2,Noeud(9),Noeud(13)),Noeud(13,Noeud(14),Noeud(4))))
print(Route_plus_chere(arbre))

n6 = Noeud(8)   
n5 = Noeud(6)
n4 = Noeud(3)
n3 = Noeud(2,n5, n6)
n2 = Noeud(4, n4, n5)
pyramide = Noeud(5, n2, n3)
print(Route_plus_chere(pyramide))
