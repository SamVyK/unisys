import random
from Models.subject import Subject

EXISTING_STUDENT_IDS = {}

class Student:
    def __init__(self, name, email, password, enrolled_course=None):
        self.student_id = self._generate_id()
        self.name = name 
        self.email = email 
        self.password = password 
        self.enrolled_course = enrolled_course if enrolled_course else []

    def _generate_id(self):
        attempts = 0 
        while attempts < 100:
            new_id = f"{random.randint(1,999999):06d}"
            if new_id not in EXISTING_STUDENT_IDS:
                EXISTING_STUDENT_IDS[new_id] = True
                return new_id
            attempts += 1
        raise Exception
