print("Lets do OOPS now!")

class Employee:
    def __init__(self, first, last, pay ):
        self.Fname = first
        self.Lname = last
        self.paisal = pay
        self.emailID = first +"."+ last + "@gmmail.com"

    def fullname(self):
        return '{}{}'.format(self.Fname,self.Lname)
    


emp1 = Employee('Ram','babu','120000')
emp2 = Employee('Veer','babu','160000')

print(Employee.fullname(emp2))
print(emp1.emailID)