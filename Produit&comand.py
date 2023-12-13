import copy
# creat class for produit
class Produit :
    _nbpr = 0
    def __init__(self, ref , dis , prix_b, prix_s , stock = 0) :
        self.__ref = ref
        self.__dis = dis
        self.__prix_b = prix_b
        self.__prix_s = prix_s
        self.__stock = stock
        Produit._nbpr += 1
        
    # create classmethod for the number thr produit 
    
    @classmethod
    def getnbpr(cls):
        return cls(Produit._nbpr) 
    
    # setter for  stok
    
    def set_stock(self, new_stock):
        if ((self.__stock) + (new_stock))<0 :
             print("dont have enough  productfor  comand")
        else :
            self.__stock = self.__stock + new_stock
            print("done")
            
    # setter for  prix the buy 
    
    def setprix_b(self , new_prix):
        self.__prix_b = new_prix
        
    # stter for prix the  sales
    
    def setprix_s(self , new_prix):
        self.__prix_s = new_prix
        
    #  fun dunder str 
    
    def __str__(self) :
        return "reference;" + self.__ref   +"---- "+  "name;"  +  self.__dis +"---- "+ "prix buy;" + str(self.__prix_b) +"---- "+ "prix sale;" + str( self.__prix_s) +"---- "+  "stock;" + str(self.__stock)
    
    # fun eq compare betweeen two prd 
    
    def __eq__(self,other):
        return self.__ref == other.__ref
    
    # getter for stock
    
    def getsto(self):
        return self.__stock

# Define a class named "Commandes"
class Commandes:
    # Constructor method
    def __init__(self, date, qa, produit):
        self.__date = date
        self.__qa = qa
        self.__produit = copy.copy(produit)

    # Getter method for the date
    @property
    def Getdate(self):
        return self.__date

    # Getter method for the product associated with the command
    @property
    def Getpro(self):
        return self.__produit

    # Setter method to update the product associated with the command
    def Setpro(self, pro1):
        self.__produit = pro1

    # Setter method to update the date
    def Setdate(self, date):
        self.__date = date

    # String representation of the object
    def __str__(self):
        return "Date :" + self.__date + "; Quantity :" + str(self.__qa) + str(self.__produit)

    # Equality comparison method
    def __eq__(self, c1):
        return self.__date == c1.__date and self.__produit == c1.__produit