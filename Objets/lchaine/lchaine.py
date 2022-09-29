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
        assert ind <= len(self), "list index out of range"
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
        assert key < len(self), "out of range"
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
        current = self.tete
        long = len(self)
        self.tete = None
        for i in range(long):
            self.prepend(current.val)
            current = current.suiv
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
 
 
class Ensemble :
    def __init__(self) :
        self.stock = Liste()
        self.long = 0
 
    def est_vide(self):
        return self.stock.est_vide()
 
    def add(self, val):
        for i in range(len(self.stock)) :
            if self.stock[i] == val :       
                return None
        self.stock.prepend(val)
        self.long+=1
        return None
 
    def discard(self, val):
        '''
        if len(self.stock) == 1 :
            if self.stock[0] == val :
                self.long -=1
                self.stock.pop(0)
        '''
        for i in range(len(self.stock)):
            if self.stock[i] == val :
                self.long -=1
                self.stock.pop(i)
                return None
        return None
 
    def __str__(self):
        res = "{"
        curent = self.stock.tete
        if self.stock.tete == None:
            return "{}"
        for i in range(len(self.stock)-1) :
            res += str(curent.val) +","
            curent = curent.suiv
        curent.suiv
        res += str(curent.val)
        return res+ "}" 
 
    def __len__(self):
        if self.est_vide() :
            return 0
        return self.long
 
    def __contains__(self, val):
       for i in range(len(self.stock)) :
           if self.stock[i] == val :
               return True
       return False
 
    def __eq__(self, ens):
        if self.stock.est_vide() and ens != {}:
            return False
        for i in range(len(self.stock)):
            if self.stock[i] not in ens :
                return False
        return True
    def __and__(self, ens):
        res = Ensemble()
 
        for i in range(len(self.stock)):
            if self.stock[i] in ens :
                res.add(self.stock[i])
        return res
 
    def __or__(self, ens):
        res = Ensemble()
        for i in range(len(self.stock)):
            res.add(self.stock[i])
        for i in range(len(ens.stock)):
            res.add(ens.stock[i])
        return res

class Dico :
    def __init__(self) -> None:
        pass


ensemble1 = Ensemble()
ensemble1.add(2)
ensemble1.add(3)
ensemble1.add(4)
ensemble1.add(5)
#ensemble1 = {2,3,4,5}
 
ens2 = Ensemble()
ens2.add(1)
ens2.add(2)
ens2.add(3)
#ens2 = {1,2,3}
 
ens3 = Ensemble()
ens3.add(2)
ens3.add(3)
ens3.add(4)
 
test = Ensemble()
test.add(1)
test.add(2)
print("1 len doit afficher 2 :",len(test))
test.add(2)
test.add(3)
print("2 in doit afficher True :",3 in test)
print("3 in doit afficher False :",5 in test)
print("4 eq Doit afficher True :",test == ens2)
print("5 & Dois afficher {2,3} :",test & ens3)
print("6 | Dois afficher {1,2,3,4,5}", test | ensemble1)
 
 
print("7 len doit afficher 3 :",len(test))
test.discard(1)
test.discard(42)
test.discard(2)
test.discard(3)
print("8 len doit afficher 0 :",len(test))
print("9 eq Doit afficher False :",test == ensemble1)
ensemble1.discard(3)
print("10 | Dois afficher {2,4,5}", test | ensemble1)
 
print("11 eq Doit afficher False:",test == ens2)
