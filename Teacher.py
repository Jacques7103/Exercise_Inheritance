from Person import *

class Teacher(Person):
    def __init__(self, numCourses: int = 0, courses: dict = []):
        super().__init__("Undefine", "Undefine")
        self.__numCourses = numCourses
        self.__courses = courses
        
    def addCourses(self, courses):
        if courses in self.__courses:
            return f"The {courses} course already existed"
        else:
            self.__courses.append(courses)
            
    def removeCourses(self, courses):
        if courses in self.__courses:
            self.__courses.remove(courses)
        else:
            return f"The {courses} course is not exist"
        
    def __str__(self):
        return f"Teacher's Name    : {self.getName()}\
                \nTeacher's Address : {self.getAddress()}\
                \nTeacher's Courses : {self.__courses}"