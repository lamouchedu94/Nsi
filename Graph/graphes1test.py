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
    
    def largeur(self,s):
        """s estun sommetdu graphe"""
        file=[s]
        parcours=[]
        while file!=[]:
            encours=file.pop(0)
            parcours.append(encours)
            for sommet in self.voisins(encours):
                if sommet not in parcours and sommet not in file:
                    file.append(sommet)
        return parcours

g = Graphe_mat(4)

g.ajouter_arc(0,2)
g.ajouter_arc(0,3)
g.ajouter_arc(1,0)
g.ajouter_arc(2,0)
g.ajouter_arc(2,3)
g.ajouter_arc(1,2)
#print(g)
#print(g.voisins(0))
#print("ici")

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
#print(g)

class Graphe_adj:
    def __init__(self, n):
        self.n = n
        self.graphe = {}
        for i in range(n):
            self.graphe[i] = []
        return None
    
    def ajouter_arc(self, s1, s2) :
        """ajoute une arête de s1 à s2, si s1 ou s2 ne sont pas dans le graphe, on les ajoute"""
        if s1 not in self.graphe:
            self.graphe[s1]=[]
            self.n+=1
        if s2 not in self.graphe :
            self.graphe[s2]=[]
            self.n+=1
        if s2 in self.voisins(s1):
            return None
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
        if s not in self.graphe:
            raise KeyError("le sommet ne fait pas partie du graphe")
        return self.graphe[s]
    
    def largeur(self,s):
        """s est un sommet du graphe"""
        file=[s]
        parcours=[]
        distances = {}  
        while file!=[]:
            encours=file.pop(0)
            parcours.append(encours)
            distances[s] = 0  
            for sommet in self.voisins(encours):
                if sommet not in parcours and sommet not in file:
                    file.append(sommet)
                    distances[sommet] = distances[encours] + 1
            
            
        return parcours, distances
    
    def profondeur(self,s):
        """s est sommet du graphe"""
        pile=[s]
        parcours=[]
        while pile!=[]:
            encours=pile.pop(-1)
            parcours.append(encours)
            for sommet in self.voisins(encours):
                if sommet not in parcours and sommet not in pile:
                    pile.append(sommet)
        return parcours                
                
            

    

    def __str__(self):
        return str(self.graphe)

test=Graphe_adj(8)
test.ajouter_arc(0,1)
test.ajouter_arc(0,3)
test.ajouter_arc(1,0)
test.ajouter_arc(1,2)
test.ajouter_arc(1,4)
test.ajouter_arc(1,2)
test.ajouter_arc(2,1)
test.ajouter_arc(3,0)
test.ajouter_arc(3,6)
test.ajouter_arc(4,1)
test.ajouter_arc(4,5)
test.ajouter_arc(5,4)
test.ajouter_arc(5,6)
test.ajouter_arc(5,7)
test.ajouter_arc(6,3)
test.ajouter_arc(6,5)
test.ajouter_arc(7,5)
#print(test)
#print(test.voisins(1))
print(test.largeur(1))
#print(test.profondeur(1))
