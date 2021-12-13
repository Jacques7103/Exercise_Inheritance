from Number_2 import *

if __name__ == "__main__":
    circle = Circle()
    circle.setRadius(-5.0)
    circle.setColor("Green")
    print(circle.__str__())
    
    print("====================")
    
    cylinder = Cylinder()
    cylinder.setRadius(5.0)
    cylinder.setColor("Blue")
    cylinder.setHeight(2.0)
    print(cylinder.__str__())