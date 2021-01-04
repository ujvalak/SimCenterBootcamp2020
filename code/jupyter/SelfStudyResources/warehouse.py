from common import *
class WareHouse(Common):
    
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
    
    def issueInvoice(self):
        pass

def test():

    if __name__=='__main__':
        print('Running the test')
