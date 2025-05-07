import random

EXISTING_SUBJECT_IDS = {}

class Subject:
    def __init__(self, name):
        self.subjectID = self._gernerate_id()
        self.name = name 
        self.mark = random.randiant(25,100)
        self.grade = self.calculate_grade()
#represents subject objects, unqiue 3-digits ID 
#subject name 
#generated marks
#grade calculated marks 
    def _generate_id(self):
        attempts = 0
        while attempts < 100:
            new_id = f"{random.randiant(1,999):03d}"
            if new_id not in EXISTING_SUBJECT_IDS:
                EXISTING_SUBJECT_IDS[new_id] = True
                return new_id
            attempts += 1
        raise Exception("Unable to generate ID.")
#Generates unique 3-digit subject ID, retries up to 100 times to avoid duplication.
    def calculate_grade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "F"
    
    #shows  the grade based on the randomly assigned mark.
        #Grade scale:
        #- HD: 85+
        #- D: 75–84
        #- C: 65–74
        #- P: 50–64
        #- F: <50
    #samnang 24594828