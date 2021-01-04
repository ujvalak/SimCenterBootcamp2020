# manage the transactions (this is called the Driver()) 
from momandpopstore import *
from customer import *
from warehouse import * 
def main():
    
    # * 3 Customers: customerA, customerB, and customerC
    customerA = Customer("customer A", 1000)
    customerB = Customer("customer B", 1000)
    customerC = Customer("customer C", 1000)
    
    # * 2 MomAndPopStores: cornerStore and villageGrocery
    cornerStore = MomAndPopStore("The Corner Store",5000)
    villageGrocery = MomAndPopStore("Village Grocery",5000)
    
    # * 2 WareHouses: veggieSupplier and countyButcher
    veggieSupplier = WareHouse("Veggie Plus", 10000)
    countyButcher  = WareHouse("Big Fat Butcher", 10000)

    print(customerA)
    print(customerB)
    print(customerC)
    print(cornerStore)
    print(villageGrocery)
    print(veggieSupplier)
    print(countyButcher)
#main execution   
if __name__ == '__main__':
    main()
