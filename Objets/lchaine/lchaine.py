class Maillon:
    def __init__(self, val, suiv):
        self.val=val
        self.suiv=suiv
        return None
 
class Liste:
    def __init__(self):
        self.tete = None
 
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
        for i in range(len(self)-1) :
            res += str(curent.val) +","
            curent = curent.suiv
        curent.suiv
        res += str(curent.val)
        return res+ "]"

    def append(self, val):
        current = self.tete
        for i in range(len(self)-1):
            current = current.suiv
        current.suiv = Maillon(val, None)
        
    def pop(self, key ):
        current = self.tete
        for i in range(key-1) :
            current = current.suiv
        print(current.val)
        temp = current.suiv
        current = temp.suiv


    def __setitem__(self, key, val):
        current = self.tete
        for i in range(key) :
            current = current.suiv
        current.val = val

l = Liste()
'''
l.prepend(1)
l.prepend(2)
l.prepend(3)
print(len(l))
print(l[2])
'''
l.prepend(2)
l.prepend(3)
print(l)
l.append(1)
l[1] = 10
l.pop(1)
print(l)
