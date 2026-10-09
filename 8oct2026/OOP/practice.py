class employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def display(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)

class Engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer", "IT", 100000)

eng1=Engineer("Elon Musk", 50)
eng1.display()