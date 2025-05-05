import random

EXISTING_SUBJECT_IDS = {}

class Subject:
    def __init__(self, name):
        self.subjectID = self._gernerate_id()
        self.name = name 
        self.mark = random.randiant(25,100)
        self.grade = self.calculate_grade()

    def _generate_id(self):
        attempts = 0
        while attempts < 100:
            new_id = f"{random.randiant(1,999):03d}"
            if new_id not in EXISTING_SUBJECT_IDS:
                EXISTING_SUBJECT_IDS[new_id] = True
                return new_id
            attempts += 1
        raise Exception("Unable to generate ID.")

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

        
            
    
