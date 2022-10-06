class Tabidir :
    def __init__(self, tabg = None, tabd = None ) -> None:
        self.tabg = []
        if tabg != None :
            self.tabg = tabg
        
        self.tabd = []
        if tabd != None :
            self.tabd = tabd
    
    def imin(self):
        return len(self.tabg) * -1 

    def imax(self) :
        return len(self.tabd) - 1 

    def append(self, val) :
        self.tabd.append(val)
        return None

    def prepend(self, val):
        self.tabg.append(val)
        return None 
    
    def __getitem__(self,i):
        if i < 0 :
            return self.tabg[i*-1 -1]
        return self.tabd[i]

    def __setitem__(self, i, val):
        if i < 0 :
            self.tabg[i *-1 - 1 ] = val
            return None
        self.tabd[i] = val
        return None

    def __str__(self) :
        res = ""
        for i in range(self.imin()*-1-1, -1 , -1):
            res += str(self.tabg[i]) + " "
        for val in self.tabd :
            res += str(val) + " "
        return res

    def __len__(self):
        return self.imax() + self.imin() * -1 +1

    def pop(self, i) :
        if i < 0 :
            assert i *-1 -1 > self.imin(), "index error"
            res = self.tabg[i *-1 -1 ]
            del self.tabg[i *-1 -1 ]
            return res
        assert i <= self.imax(), "index error"
        res = self.tabd[i]
        del self.tabd[i]
        return res

test = Tabidir()
print(len(test))
print(test)
test.append(1)
test.append(2)
test.prepend(3)
test.prepend(4)
print(test[1])
print(test[-1])
print(test[-2])
#test[-2] = 10
#test[1] = 11
print(test)
print(len(test))
print(test.pop(1))
print(test)
