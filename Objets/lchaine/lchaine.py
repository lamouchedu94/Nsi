class Maillon:
    def __init__(self, val, suiv):
        self.val=val
        self.suiv=suiv
        return None
 
class Liste:
    def __init__(self,tab = None):
        if tab==None or tab == [] :
            self.tete = None
        else :
 
            self.tete = None
            for i in range(len(tab)):
                self.prepend(tab[len(tab)-i-1])
            return None
        return None         
 
    def est_vide(self):
        return self.tete is None
 
    def prepend(self, val):
        self.tete = Maillon(val, self.tete)
        return None 
 
    def __len__(self):
        curent = self.tete
        i = 0
        while curent != None:
            curent = curent.suiv
            i+=1
        return i
 
    def __getitem__(self,ind):
        assert ind < len(l), "list index out of range"
        curent = self.tete
        for i in range(ind) :
            curent = curent.suiv
        return curent.val
 
    def __str__(self):
        res = "["
        curent = self.tete
        if self.tete == None:
            return "[]"
        for i in range(len(self)-1) :
            res += str(curent.val) +","
            curent = curent.suiv
        curent.suiv
        res += str(curent.val)
        return res+ "]"
 
    def append(self, val):
        current = self.tete
        if self.tete == None :
            self.tete = Maillon(val, None)
            return None
        for i in range(len(self)-1):
            current = current.suiv
        current.suiv = Maillon(val, None)
        return None
 
    def pop(self, key = None):
 
        if key == None :
            key = len(self)
        current = self.tete
        assert key >= len(self), "out of range"
        if key == 0 :
            #temp = self.tete.suiv
            val= self.tete.val
            self.tete = self.tete.suiv
            return val
        if key == 1 :
            res = self.tete.val
            self.tete = None
            return res
 
        for i in range(key-1) :
            current = current.suiv
        temp = current.suiv
        val = temp.val
        current.suiv = temp.suiv
        return val
 
    def __setitem__(self, key, val):
        current = self.tete
        for i in range(key) :
            current = current.suiv
        current.val = val
        return None
 
    def reverse(self):
        res = ""
        for i in range(len(self)-1,-1,-1):
            res += str(self[i])
        print(res)
        for j in range(len(res)):
            self[j] = int(res[j]) 
        return None
 
    def sort(self):
        pass
 
    def slicer(self, ind_depart, ind_fin):
        temp = ""
        res = ""
        assert ind_fin < len(self), "out of range"
        assert ind_depart < len(self), "out of range"
        assert ind_depart < ind_fin, "out of range"
 
        for i in range(len(self)):
            temp += str(self[i])
        for i in range(ind_depart, ind_fin):
            res += temp[i]+ ","
        res += temp[ind_fin]
 
        return "[" + res + "]"
 
 
    def __add__(self, tab):
        res = Liste()
        for j in range(len(tab)-1, -1,-1):
            res.prepend(tab[j])        
        for i in range(len(self)-1, -1, -1):
            res.prepend(self[i]) 
        return res 
 
 
l = Liste([1,2,3])
 
print(l+[18,19])
#print(l.slicer(0,2))
#l.pop()
print(l)
l.reverse()
print(l)