class Graphe_mat :
    def __init__(self,n) :
        self.n = n
        self.mat=[[0 for i in range(n)] for i in range(n)]
    
    def ajouter_arc(self, s1, s2) :
        self.mat[s1][s2] = 1
        return None
    
    def arc_entre(self, s1, s2): 
        return self.mat[s1][s2] == 1
    
    def suppr_arc(self, s1, s2) :
        self.mat[s1][s2] = 0 
        return None

    def voisins(self, s) :
        res = []
        for i in range(self.n) :
            if self.arc_entre(s,i):
                res.append(i)
        return res

    def __str__(self) -> str:
        res = ""
        for n in self.mat :
            res += str(n) + "\n"
        
        return res

g = Graphe_mat(4)

g.ajouter_arc(0,2)
g.ajouter_arc(0,3)
g.ajouter_arc(1,0)
g.ajouter_arc(2,0)
g.ajouter_arc(2,3)
g.ajouter_arc(1,2)
print(g)
print(g.voisins(0))

class Graphe_mat_non_orient :
    def __init__(self,n) :
        self.n = n
        self.mat=[[0 for i in range(n)] for i in range(n)]
    
    def ajouter_arc(self, s1, s2) :
        self.mat[s1][s2] = 1
        self.mat[s2][s1] = 1
        return None
    
    def arc_entre(self, s1, s2): 
        return self.mat[s1][s2] == 1
    
    def suppr_arc(self, s1, s2) :
        self.mat[s1][s2] = 0 
        self.mat[s2][s1] = 0
        return None

    def voisins(self, s) :
        res = []
        for i in range(self.n) :
            if self.arc_entre(s,i):
                res.append(i)
        return res

    def __str__(self) -> str:
        res = ""
        for n in self.mat :
            res += str(n) + "\n"
        
        return res
g = Graphe_mat_non_orient(4)  
g.ajouter_arc(0,2)
g.ajouter_arc(0,3)
g.ajouter_arc(1,0)
g.ajouter_arc(2,0)
g.ajouter_arc(2,3)
g.ajouter_arc(1,2)
print(g)

class Graphe_adj:
    def __init__(self, n):
        self.n = n
        graphe = {}
        for i in range(n):
            graphe[i] = []
        return None
    