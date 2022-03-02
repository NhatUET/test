class Student(object):
        def __init__(self, name, id, gpa):
                self.name = name
                self.id = id
                self.gpa = gpa
        def show_info(self):
                print ("name:", self.name, "id:", self.id, "gpa:", self.gpa)
        
st1 = Student("Vu Minh Nhat", 20021407, 3.02)
st2 = Student("Nguyen Thi Hang", 20022512, 4.0)

student_list = [st1, st2]
student_list = sorted(student_list, reverse = True)

print(student_list)