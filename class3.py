# Define a class named "Person"
class Person:
    # Assign "Person" object using def__init__ function
    def __init__(self, name:str, address:str):
        self.__name = name
        self.__address = address
    
    def Person(self, name:str, address:str):
        pass

    # Fetch the  name
    def getName(self)->str:
        return (self.__name)

    # Fetch the address
    def getAddress(self)->str:
        return (self.__address)
    
    # Change the address
    def setAddress(self,address:str):
        self.__address = address
        return ("Address now: {}".format(address))
    
    # Print "name(address)"
    def __str__(self):
        return (self.getName()+"({})".format(self.getAddress()))

# Define a class named "Student" and it is a subclass from "Person" class
class Student(Person):
    # Assign "Student" object using def__init__ function
    def __init__(self, name:str, address:str, numCourses:int=0, courses:list=[], grades:list=[] ):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = courses
        self.__grades = grades

    def Student(self, name:str, address:str):
        pass

    # Add course(s) / grade(s) / both for student
    def addCourseGrade(self, course:str ,grade:int):
        self.__numCourses += 1
        self.__courses.append(course)
        self.__grades.append(grade)
        return ("Course: {} and Grade: {} is added".format(course,grade))

    # Print all of the grades
    def printGrades(self):
        return (self.__grades)
    
    # Calculate the student's average grade
    def getAverageGrade(self):
        result = 0
        for int in self.__grades:
            result += int
        return (result/len(self.__grades))
    
    # print "name(address)"
    def __str__(self):
        return (self.getName()+"({})".format(self.getAddress()))

# Define a class named "Teacher" and it is a subclass from "Person" class
class Teacher(Person):
    # Assign "Teacher" object using def__init__ function
    def __init__(self, name, address, numCourses:int=0, courses:list=[]):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = courses

    def Teacher(self, name:str, address:str):
        pass

    # Add course(s) for teacher
    def addCourse(self, course:str)->bool:
        if (course in self.__courses):
            return False
        else:
            self.__numCourses += 1
            self.__courses.append(course)
            return ("{} course is added".format(course))
    
    # Remove course(s) for teacher
    def removeCourses(self, course:str)->bool:
        if (course not in self.__courses):
            return False
        else:
            self.__numCourses -= 1
            self.__courses.remove(course)
            return ("{} course is removed".format(course))
    
    #print "name(address)"
    def __str__(self):
        return ("Teacher: "+self.getName()+"({})".format(self.getAddress()))

## UNCOMMENT THE CODE BELOW FOR TESTING THE CODE ##

# person = Person("Harry", "Grove St.")
# student = Student("Harry", "Gading St.",4,["Math", "Chemistry", "Social", "Language"],[100,98,97,60])
# teacher = Teacher("Billy", "Bruh St.",5,["Physics", "Math", "Chemistry", "Social", "Language"])

# print(person.getName())
# print(person.getAddress())
# print(person.setAddress("Wall st."))
# print(person.__str__())
# print(student.addCourseGrade("Physics", 96))
# print(student.printGrades())
# print(student.getAverageGrade())
# print(student.__str__())
# print(teacher.addCourse("Math"))
# print(teacher.addCourse("Biology"))
# print(teacher.removeCourses("Computer"))
# print(teacher.removeCourses("Math"))
# print(teacher.__str__())
