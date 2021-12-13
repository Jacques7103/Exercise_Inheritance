class Person:
    def __init__(self, name: str = "Undefine", address: str = "Undefine"):
        self.__name = name
        self.__address = address
    
    def setName(self, name):
        self.__name = name
        
    def setAddress(self, address):
        self.__address = address
            
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
        
    def __str__(self):
        return f"Name      : {self.getName()}\
                \nAddress   : {self.getAddress()}"        