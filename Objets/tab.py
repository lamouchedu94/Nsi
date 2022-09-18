from re import S


class Tab_pyth : 
    def __init__(self, tab = None, long = 5) :
        self.tab = [None for i in range(long)]
        self.debut = 0 
        self.fin = 0
    def est_vide(self) :
        if self.debut == self.fin :
            return True
        return False
    def longueur(self):
        return len(self.tab)
    def append(self,val) : 
        if self.fin == self.longueur():
            self.temp = [None for i in range(2*self.longueur())]
            i = 0
            for carc in self.tab :
                if carc != None :
                    self.temp[i] = carc
                    i += 1
                else : 
                    self.fin -= 1 
            self.tab = self.temp
            self.debut = 0 
            
        
        self.tab[self.fin] = val
        self.fin += 1
        
    def pop_debut(self):
        assert not self.est_vide() , "Tableau vide"
        self.tab[self.debut] = None
        self.debut += 1 
        
        
        

test = Tab_pyth(None, 3)

print(test.longueur())
print(test.est_vide())
test.append(1)
test.append(2)
test.append(3)
print(test.tab)
print(test.tab)
test.pop_debut()
test.pop_debut()
test.pop_debut()
test.pop_debut()
print(test.tab)