class Pile:
   
    def __init__(self, stock=None):
        if stock is None:
            stock = []
        self.stock = stock
        return None

    def empile(self, val):
        self.stock.append(val)
        return None
   
    def depile(self):
        assert not self.est_vide(), 'la pile est vide'
        return self.stock.pop()

    def est_vide(self):
        return self.stock == []
   
class File:
   
    def __init__(self, stock_entree=None):
        if stock_entree is None:
            stock_entree = []
        self.entree = Pile(stock_entree)
        self.sortie = Pile()
        return None
    
    def longeur(self) :
        return len(self.sortie.stock) 

    def enfile(self, val):
        self.entree.empile(val)
        return None
   
    def _entree_dans_sortie(self):
        while not self.entree.est_vide():
            self.sortie.empile(self.entree.depile())
        return None
       
    def defile(self):
        if self.sortie.est_vide():
            self._entree_dans_sortie()
        assert not self.sortie.est_vide(), 'La file est vide'
        return self.sortie.depile()
   
    def est_vide(self):
        return self.entree.est_vide() and self.sortie.est_vide()


class Client():
    """attributs: nb article, date arrivee, duree d'attente à l'arrivee en caisse
    methodes: init, encaisse appelee lorsqu'il arrive en caisse pr calculer sa duree d'attente"""

    def __init__(self,article=0,arrivee=0):
        self.nb_article=article
        self.date_arrivee=arrivee
        self.duree_attente=0
        return None

    def __str__(self) -> str:
        return str(self.nb_article)

    def encaisse(self):
        pass
    
    def plus_article(self) :
        return self.nb_article == 0 


   

class Caisse():
    """attributs: file d'attente, nbr article sur tapis
    methodes: init, nv_client appelé lorsque tapis vide: retire un client de la file et met ses articles sur le tapis
    pas: appelle a chaque pas de la simulation et retire un article du tapis s'il n'est pas vide et appelle un client sinon"""
    def __init__(self,clients=None):
        if clients is None:
            clients = File()
        self.clients = clients
        self.client_encaisse = None
        self.tapis = 0

    def nv_client(self):
        print("Nouveau client encaissé")
        return self.clients.defile() 

    def pas(self, temps):
        if self.client_encaisse == None:
            self.client_encaisse = self.nv_client()
            self.tapis = self.client_encaisse.nb_article
        if self.tapis==0:
            self.client_encaisse = None
            return True
        else :
            self.tapis -= 1
        return False
   

class Simulation():
    "attributs:  "
    "methodes:  "
    def __init__(self):
        self.nb_caisse = 1
        self.pas = 0 
    '''
    def file_attente(self) :
        file = File()
        for i in range(10) :
            file.enfile(i)
        
        print(file.stock)
    '''
    def lancement(self):
        arrive = [0,3,4]
        clients = File([Client(2,arrive[0]),Client(10,arrive[1]),Client(2,arrive[2])]) 
        #clients.longeur()
        caisse = Caisse(clients)
        temps = 0
        caisse.pas(temps)
        nb_client = 0
        while clients.longeur() != 0 :
            if caisse.pas(temps) :
                print(temps)
                nb_client+= 1
            temps += 1  
        
        print("le temps d'attente total est de :",temps)
test = Simulation()
#test.file_attente()
test.lancement()


