from PythonAssignment import Student

class Student_Management:
    list_student = []
    def generate_id(self):
        maxID = 1
        if (self.num_Of_Student() > 0) :
            maxID = self.list_student[0].id
            for sv in self.list_student:
                if maxID < sv.id:
                    maxID = sv.id
            maxID = maxID + 1
        return maxID
    def num_Of_Student(self):
                return self.list_student.__len__()
    def input(self):
        svID = self.generate_id()
        name = input("input the student's name: ")
        sex = input("input the sex of student: ")
        age = input("input the age of student: ")
        gpa = input("input the gpa: ")
        sv = Student(name,svID, sex, age, gpa)
        self.list_student.append(sv)
    def sort_by_gpa(self):
        self.list_student.sort(key = lambda x : x.gpa, reverse = False)
        
    def sort_by_name(self):
        self.list_student.sort(key = lambda x : x.name, reverse = False)


