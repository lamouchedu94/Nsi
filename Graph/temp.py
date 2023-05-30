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
print("ici")

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
        self.graphe = {}
        for i in range(n):
            self.graphe[i] = []
        return None
    
    def ajouter_arc(self, s1, s2) :
        if s1 in self.graphe :
            self.graphe[s1].append(s2)
        else :
            self.graphe[s1] = []
            self.graphe[s1].append(s2)
        return None 
    
    def arc_entre(self, s1,s2):
        return s2 in self.graphe[s1]    
    
    def suppr_arc(self,s1,s2):
        if s2 in self.graphe[s1] :
            pos = 0
            for i in range(len(self.graphe[s1])):
                if self.graphe[s1][i] == s2 :
                    pos=i
                    break
            self.graphe[s1].pop(pos)
        return None
    
    def voisins(self, s) :
        res = []
        for i in range(self.n) :
            if self.arc_entre(s,i):
                res.append(i)
        return res
    
    def profondeur(self,s,tab=None):
        if tab == None : 
            tab = []
        if s not in tab :
            tab.append(s)
        pas_vu = [i for i in self.graphe[s] if i not in tab]
        for v in pas_vu : 
            self.profondeur(v, tab)
        return tab



    def __str__(self):
        return str(self.graphe)

test=Graphe_adj(4)
test.ajouter_arc(0,2)
test.ajouter_arc(0,3)
test.ajouter_arc(1,0)
test.ajouter_arc(2,0)
test.ajouter_arc(2,3)
test.ajouter_arc(1,2)

print(test)
print(test.voisins(1))
print(test.profondeur(1))
test.suppr_arc(2,3)
print(test)