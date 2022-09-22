from pydoc import cli
import random
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
        if self.sortie.est_vide() :
            return None
        #assert not self.sortie.est_vide(), 'La file est vide'
        return self.sortie.depile()
   
    def est_vide(self):
        return self.entree.est_vide() and self.sortie.est_vide()


class Client:
    """attributs: nb article, date arrivee, duree d'attente à l'arrivee en caisse
    methodes: init, encaisse appelee lorsqu'il arrive en caisse pr calculer sa duree d'attente"""
    def __init__(self, article) :
        self.articles = article
        self.duree_attente=0
    
    def nombre_article(self):
        return self.articles

    def encaisse(self, ):
        pass

class Caisse :
    """attributs: file d'attente, nbr article sur tapis
    methodes: init, nv_client appelé lorsque tapis vide: retire un client de la file et met ses articles sur le tapis
    pas: appelle a chaque pas de la simulation et retire un article du tapis s'il n'est pas vide et appelle un client sinon"""
    def __init__(self):
        self.tapis = 0 
        #self.client = client 
    def tapis_vide(self) :
        if self.tapis == 0 :
            return True
        return False 
    def noveau_client(self, client):
        self.client = client
        if self.tapis_vide() :
            self.tapis = self.client.nombre_article()
            self.client.encaisse()
    def avancement(self):
        print(self.tapis)
        self.tapis -= 1 


class Simulation :
    def __init__(self, nb_caisse = 1, nb_client = 1, max_article = 1) :
        self.nb_caisse = nb_caisse
        self.nb_client = nb_client
        self.max_article = max_article
        self.caisse_libre = [False for i in range(self.nb_caisse)]
    
    def initialisation_caisse(self):
        #self.caisse = Caisse
        self.caisse = [Caisse() for i in range(self.nb_caisse)]
        return None

    def initialisation_client(self):
        self.file = File([Client(random.randint(0, self.max_article)) for i in range(self.nb_client)])
        return None


    def lancement(self) :
        pas = 0
        i = 0
        self.initialisation_client()
        self.initialisation_caisse()

        while not self.file.est_vide() :
            for i in range(self.nb_caisse):
                if self.caisse[i].tapis_vide() :
                    self.caisse[i].noveau_client(self.file.defile())
                    print(f"nouveau client en caisse {i}")
            for i in range(self.nb_caisse) :
                self.caisse[i].avancement()
                   
            

            pas += 1         


tests = Simulation(1,2,10)
tests.lancement()