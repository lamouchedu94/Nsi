class File:

    def __init__(self, stock_depart=None):
        if stock_depart == None:
            stock_depart = []
        self.stock = stock_depart
    
    def ajouter(self, val):
        self.stock.append(val)
        return None
    
    def retirer(self):
        assert not self.est_vide(), "file vide"
        return self.stock.pop(0)
    
    def est_vide(self):
        return self.stock == []

test = File()
test.ajouter(1)
test.ajouter(10)
test.ajouter(11)
print(test.stock)
test.retirer()
print(test.stock)