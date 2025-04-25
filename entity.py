import random

EXSIT_STU_ID = dict() # should put in database later
EXSIT_SUBJECT_ID = dict()

class student:
    def __init__(self,name,email,passord,loginAttempts,enrolledCourse):
        self.student_id = self.get_id()
        self.name = name 
        self.email = email
        self.loginAttempts = loginAttempts
        self.password = passord
        self.enrolledCourse = enrolledCourse
        
    def get_id(self, ):
        stu_id = random.randint(1,999999)
        c = 0
        max_step = 100
        while '{0:09d}'.format(stu_id) in EXSIT_STU_ID:
            stu_id = random.randint(1,999999)
            c += 1
            if c > max_step:
                break
        EXSIT_STU_ID['{0:09d}'.format(stu_id)] = True
        return '{0:09d}'.format(stu_id)
    
    def register(self):
        pass
    def login(self):
        pass
    def updatePassword(self):
        pass
    def enroll(self):
        pass
    def unenroll(self):
        pass
    def viewSubject(self):
        pass

class Admin:
    def __init__(self, adminID, name, email):
        self.adminID = adminID
        self.name = name
        self.email= email
    def viewStudentData(self):
        pass
    def sortByGrade(self):
        pass
    def groupPassOrFail(self):
        pass
    def deleteStudent(self):
        pass
    def clearAllData(self):
        pass

class Subject:
    def __init__(self, name, mark):
        self.subjectID = self.gen_sub_id()
        self.name = name 
        self.mark = mark
    def generationMark(self):
        pass
    def gen_sub_id(self):
        subject_id = random.randint(1,999)
        c = 0
        max_step = 100

        while '{0:03d}'.format(subject_id) in EXSIT_SUBJECT_ID:
            
            subject_id = random.randint(1,999)
            c += 1
            if c > max_step:
                break
        EXSIT_SUBJECT_ID['{0:03d}'.format(subject_id)] = True
 
        return '{0:03d}'.format(subject_id)


if __name__ == "__main__":
    pass
