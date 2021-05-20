FILE_PATH = "library/"

def main():
    employeeRoster = [] #Place to collect employee objects
    #stuff = SalariedEmployee("fred", 25, 10)
    #print(str(stuff.calculatePay()))

    payrollControl("Y", employeeRoster)

def payrollControl(action, employeeRoster:list): # Y(es) to begin
    if action == "Y": # Yes - continue
        name = str(input("Enter employee's name: ")).strip()
        classification = str(input("Enter employee's classification (Salaried or Hourly): "))
        hours = int(input("Enter the number of hours worked: "))
        if classification == "Salaried":
            rateOfPay = int(input("Enter weekly salary: "))
            employeeRoster.append(SalariedEmployee(name,rateOfPay,hours))
        elif classification == "Hourly":
            rateOfPay = int(input("Enter hourly wage: "))
            employeeRoster.append(HourlyEmployee(name,rateOfPay,hours))
        payrollControl(str(input("Do you want to continue (Y/N)? ")).upper(), employeeRoster)
    elif action == "N": # No - end 
        salaried = 0
        totalPayroll = 0
        totalHoursWorked = 0
        print()
        for employee in employeeRoster:
            totalPayroll += employee.calculatePay()
            totalHoursWorked += employee._hours
            print(employee._name+": ${:,.2f}".format(employee.calculatePay()))
            if isinstance(employee, SalariedEmployee):
                salaried += 1 #Add one if employee is salaried, veryified by Class usage
        print("Number of employees: "+str(len(employeeRoster)))
        print("Number of salaried employees: "+str(salaried))
        print("Total Payroll: ${:,.2f}".format(totalPayroll))
        print("Average number of hours worked per employee: {:,.2f}".format(totalHoursWorked / len(employeeRoster)))

class Employee:
    def __init__(self, name:str, rateOfPay:int, hours:int):
        self._name = str(name)
        self._rateOfPay = int(rateOfPay)
        self._hours = int(hours)

class SalariedEmployee(Employee):
    def __init__(self, name:str, rateOfPay:int, hours:int):
        super().__init__(name, rateOfPay, hours)

    def calculatePay(self):
        return self._rateOfPay

class HourlyEmployee(Employee):
    def __init__(self, name:str, rateOfPay:int, hours:int):
        super().__init__(name, rateOfPay, hours)

    def calculatePay(self):
        return self._rateOfPay * self._hours

main()