class StudentClass:
    def __init__(self,studentID,name,DOB,classification):
        self.__studentID = studentID
        self.__name = name
        self.__DOB = DOB
        self.__classification = classification

    def set_studentID(self,studentID):
        self.__studentID = studentID
    #Should have another 3 for these variables, good practice

    def calculate_age(self,DOB):