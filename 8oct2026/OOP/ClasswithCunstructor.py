class student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi {self.name} your avrage is ",sum/3)

std_name = input("Your Name :")
std_marks = []

for i in range(1,4):
    marks=int(input(f"enter marks {i}:"))
    std_marks.append(marks)

s1=student(std_name,std_marks)
s1.avg_marks()
