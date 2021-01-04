class Common(object):
    
    def __init__(self, name='unknown',cash=0):
        self.name = name
        self.cash = cash
        self.items = {}
        self.prices = {}
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "{}(name=\"{}\",cash={})".format(self.__class__.__name__, self.name, self.cash)
    
    def makePayment(self,X):
        if X<=self.cash:
            self.cash -= X
            return X
        else:
            return 0
    
    def checkPrice(self,item):
        if item in self.prices:
            return self.prices[item]
        else:
            return -1 # we don't carry that item
    
    def takePayment(self,X):
        if X>0:
            self.cash += X