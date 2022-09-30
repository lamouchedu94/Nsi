from distutils.log import error


class Maillon:
    def __init__(self, val, suiv):
        self.val=val
        self.suiv=suiv
        return None

class Liste:
    def __init__(self,tab=None):
        self.tete=None
        if tab==None:
            tab=[]
        for i in range(len(tab)):
            self.prepend(tab[len(tab)-i-1])
        return None
        
    def est_vide(self):
        return self.tete is None
    
    def prepend(self,val):
        self.tete=Maillon(val,self.tete)
        return None
    
    def __len__(self):
        if self.tete==None:
            return 0
        maillon_crt=self.tete
        cpt=1
        while maillon_crt.suiv is not None:
            maillon_crt=maillon_crt.suiv
            cpt+=1
        return cpt
    
    def __getitem__(self,ind):
        assert ind<len(self) and ind>=0,"index out of range"
        maillon_crt=self.tete
        for _ in range(ind):
            maillon_crt=maillon_crt.suiv
        return maillon_crt.val
    
    def __str__(self):
        if self.est_vide():
            return '[]'
        res='['
        curs=self.tete
        while curs.suiv is not None:
            res+=str(curs.val)+','
            curs=curs.suiv
        return res+str(curs.val)+']'
    
    def append(self,val):
        if self.est_vide():
            self.tete=Maillon(val,None)
            return None
        curs=self.tete
        while curs.suiv is not None:
            curs=curs.suiv
        curs.suiv=Maillon(val,None)
        return None
    
    def pop(self,ind=None):
        if ind==None:
            ind=len(self)-1
        assert ind<len(self),"out of range"
        if ind==0:
            res=self.tete.val
            self.tete=self.tete.suiv
            return res
        curs=self.tete
        for i in range(ind-1):
            curs=curs.suiv
        res=curs.suiv.val
        curs.suiv=curs.suiv.suiv
        return res
               
    def __setitem__(self,ind,val):
        assert ind<len(self),"out of range"
        curs=self.tete
        for i in range(ind):
            curs=curs.suiv
        curs.val=val
        return None
    
    def reverse(self):
        for i in range(len(self)//2):
            self[i],self[len(self)-1-i]=self[len(self)-1-i],self[i]
        return None
                                                 
    def sort(self):
        pass
    
    def slicer(self,ind_depart,ind_fin):
        assert ind_fin<len(self), "out of range"
        res=Liste()
        curs=self.tete
        for i in range(ind_depart):
            curs=curs.suiv
        for i in range(ind_fin-ind_depart):
            res.prepend(curs.val)
            curs=curs.suiv
        res.reverse()
        return res
    
    def __iter__(self):
        self.curs=self.tete
        return self
    
    def __next__(self):
        if self.curs is None:
            raise StopIteration
        res=self.curs.val
        self.curs=self.curs.suiv
        return res
    
    def __repr__(self):
        return str(self)
    
    def __add__(self,l):
        pass

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

class Dictionnaire :
    def __init__(self, long) :
        self.stock = [Liste() for i in range(long)]
        self.long_tab = long
    def est_vide(self):
        for i in range(self.long_tab) :
            if not self.stock[i].est_vide():
                return False
        return True

    def hash(self, clef) :
        total = 0
        for carac in clef :
            total += ord(carac)
        return total % len(self.stock)
    
    def __setitem__(self, clef, valeur) : 
        position = self.hash(clef)
        if not self.est_vide() :
            for i in range((len(self.stock[position]))):
                if self.stock[position][i][0] == clef :
                    self.stock[position][i] = (clef,valeur)
                    return None    
        self.stock[position].prepend((clef,valeur))
        
        return None

    def __getitem__(self, clef):
        assert not self.est_vide(), "dico vide"
        res = False
        for car in self.stock[self.hash(clef)]:
            if car[0] == clef :
                res = True
                return car[1]
        assert res, "key error"

    def liste_celf(self):
        res = Liste()
        for i in range(self.long_tab):
            for val in self.stock[i] :
                res.prepend(val[0])
        return res

    def liste_val():
        pass

def testEnssemble() :
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
#testEnssemble()

dico1 = Dictionnaire(5)


print("vide Doit afficher True :",dico1.est_vide())
dico1["a"] = "valeur"
dico1["a"] = "valeur1"
dico1["b"] = "val"
print(dico1["a"])
print(dico1["b"])
#print(dico1["c"])
print(dico1.liste_celf())