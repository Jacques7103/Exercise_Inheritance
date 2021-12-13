from Person import *
from Student import *
from Teacher import *

if __name__ == "__main__":
    Jacq = Person()
    Jacq.setName("Jacq")
    Jacq.setAddress("ABC Street")
    print(Jacq.__str__())
    
    print("\n================================================")
    
    Fer = Student()
    Fer.setName("Fer")
    Fer.setAddress("DCE Street")
    Fer.addCoursesGrade("Algo", 20)
    print(Fer.__str__())
    Fer.printGrades()
    
    print("\n================================================\n")
    
    Min = Teacher()
    Min.setName("Min")
    Min.setAddress("POL Street")
    Min.addCourses("Algo")
    Min.addCourses("HCI")
    print(Min.__str__())
    
    print("\n================================================\n")
    
    Min.removeCourses("Algo")
    print(Min.__str__())
    