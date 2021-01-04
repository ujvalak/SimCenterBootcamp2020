from common import *
class MomAndPopStore(Common):
    
    def takeOrder(self, item):
        if item in self.items:
            stock = self.items[item]
            if stock > 0:
                # sell one item, so reduce stock
                self.items[item] -= 1
                # request payment
                return self.prices[item]
            else:
                # we usually carry this item but we are currently out of stock.
                return 0
        else:
            # we don't stock that item
            return -1
    
    def placeOrder(self):
        pass
    
    def issueInvoice(self):
        pass