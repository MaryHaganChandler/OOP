class Student:

    def __init__(self, studentID, name, DOB, classification):
        self.__studentID = studentID
        self.__name = name
        self.__DOB = DOB
        self.__classification = classification

    
    
    def get_student_ID(self):
        return self.__studentID 

    def withdraw(self, name):
        #Double-check all of this is right