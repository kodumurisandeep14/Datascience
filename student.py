from person import person
class student (person):
    def __init__(self, name, age,roll_no,marks):
        super().__init__(name, age)
        self.roll_no= roll_no
        self.marks=marks
    def show_student_detail(self):
        self.show_student_detail
        print("Roll no:",self.roll_no)
        print("Marks:",self.marks)    