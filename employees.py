
# This module defines an Employee class

class Employee:

    def __init__(self, name="", hours=0, rate=0):
        self.name = name
        self.hours = hours
        self.rate = rate

    def setName(self, name):
        self.name = name
        
    def setHours(self, hours):
        if hours > 0:
            self.hours = hours

    def setRate(self, rate):
        if rate > 0:
            self.rate = rate

    def getName(self):
        return self.name
        
    def getHours(self):
        return self.hours

    def getRate(self):
        return self.rate

  
# This  method prompts for the name, hours worked,
# and hourly rate for an employee, validates the input, and creates an object

    def get_input():
        name = input("Enter a name: ")
        hours = float(input("Enter hours worked: "))
        rate = float(input("Enter hourly rate: "))
        
        e1 = Employee(name)
        e1.setHours(hours)
        e1.setRate(rate)

        return e1


# This method calculates and returns the amount the employee gets paid 

    def calc_pay(self):
        if self.hours <= 40:
            return self.hours * self.rate
        if self.hours > 40:
            return 40*self.rate + (self.hours-40)*1.5*self.rate
        

# This program creates a menu that allows to enter an employee
# or quit the application, print the total and average pay for all employees

if __name__ == "__main__":

    print("*" * 70)
    print("                   Employee Data Entry Application")
    print("*" * 70)

        
    a = input("\n1: Enter an employee \nq: Quit the application\n")

    lst = []
    
    if a == "1":
        e1 = Employee.get_input()
        lst += [e1]

    if a == "q":
        print("No employees were entered")

    
    while a != "q":
        a = input("\n1: Enter an employee \n2: Print employee list \nq: Quit the application\n")

        if a == "1":
            e1 = Employee.get_input()
            lst += [e1]
            
        if a == "2":
            for e1 in lst:
                print()
                print("{:30}".format("Name:"),  e1.name)
                print("{:30}".format("Hours Worked:"), format(e1.hours, ".2f"))
                print("{:31}".format("Hourly Rate:"), "$",
                      format(e1.rate, ".2f"), sep="")
            
        if a == "q":
            total = 0

            for e1 in lst:
                pay = e1.calc_pay()
                total += pay

            print("The total amount to be paid is $",
                  format(total, ",.2f"), sep="")
            print("The average employee is paid $",
                  format(total/len(lst), ",.2f"), sep="") 
