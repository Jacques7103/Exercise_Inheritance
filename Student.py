from Person import *

class Student(Person):
    courses_grades = {}
    def __init__(self, numCourses: int = 0, courses: str = "", grades: int = 0):
        super().__init__("Undefine", "Undefine")
        self.__numCourses = numCourses
        self.__courses = courses
        self.__grades = grades
        
    def addCoursesGrade(self, courses, grades: int):
        self.courses_grades.update({courses: grades})
        
    def printGrades(self):
        for key, value in self.courses_grades.items():
            print(f"{key} : {value}")
            
    def getAverageGrade(self):
        grade = 0
        for value in self.courses_grades.values():
            grade = grade + value
        return f"{float(grade / len(self.courses_grades))}"
    
    def __str__(self):
        return f"Student Name              : {self.getName()}\
                \nStudent Address           : {self.getAddress()}\
                \nStudent's Average Grade   : {self.getAverageGrade()}"