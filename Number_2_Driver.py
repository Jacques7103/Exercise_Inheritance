from Number_2 import *

if __name__ == "__main__":
    circle = Circle()
    circle.setRadius(3.0)
    circle.setColor("Green")
    print(circle.toString())
    
    print("====================")
    
    cylinder = Cylinder()
    cylinder.setRadius(5.0)
    cylinder.setColor("Blue")
    cylinder.setHeight(2.0)
    print(cylinder.toString())