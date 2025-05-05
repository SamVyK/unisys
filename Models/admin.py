class Admin:
    def __init__(self, admin_id, name, email):
        self.adminID = admin_id
        self.name = name 
        self.email = email

    def view_student_info(self, students):
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, Email: {student.email}")

    def sort_by_grade(self, students):
        return sorted(students, key=lambda s: s.average_mark(), reverse=True)
    
    def group_pass_fail(self, students):
        passed = [s for s in students if s.has_passed()]
        failed = [s for s in students if not s.has_passed()]

    def delete_student(self, students, student_id):
        return [s for s in students if s.student_id != student_id]
    
    def clear_all_data(self):
        return[]
    
#samnang 24594828