import math

class Circle:
    def __init__(self, radius: float = 1.0, color: str = "Red"):
        self.__radius = radius
        self.__color = color
    
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius: float):
        if radius > 0 :
            self.__radius = radius
        else:
            self.__radius = 1.0
        
    def getColor(self):
        return self.__color
    
    def setColor(self, color: str):
        self.__color = color
        
    def __str__(self):
        return f"Radius: {self.getRadius()}\
                \nColor: {self.getColor()}\
                \nArea: {self.getArea()}"
        
    def getArea(self):
        return f"{float(math.pi * self.__radius * self.__radius):.2f}"
    
class Cylinder(Circle):
    def __init__(self, height: float = 1.0):
        super().__init__(radius = 1.0, color = "Red")
        self.__height = height
        
    def getHeight(self):
        return float(self.__height)
    
    def setHeight(self, height: float):
        self.__height = height
        
    def __str__(self):
        return f"Radius: {self.getRadius()}\
                \nColor: {self.getColor()}\
                \nHeight {self.getHeight()}\
                \nVolume: {self.getVolume()}"
        
    def getVolume(self):
        return f"{float(math.pi * self._Circle__radius * self._Circle__radius * self.__height):.2f}"