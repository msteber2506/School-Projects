from employee import Employee
from linkedList import LinkedList

if __name__ == "__main__":
    employeeList = LinkedList()
    print("*** CS 172 Payroll Simulator ***") 
    while(True):
        print("a. Add New Employee")
        print("b. Enter Employee Hours")
        print("c. Update Employee Hourly Rate")
        print("d. Display Payroll")
        print("e. Remove Employee from Payroll")
        print("f. Exit the program")
        choice = input("Enter your choice:")
        if choice == "a":
            newEmployeeName = input("Enter the new employee name:")
            newEmployeeRate = float(input("Enter their hourly rate:"))
            newEmployee = Employee(newEmployeeName,newEmployeeRate)
            Employee.idInteger += 1
            employeeList.append(newEmployee)
            print("Employee {} added to payroll".format(newEmployee.getEID()))
            print()
        elif choice == "b":
            for employee in employeeList:
                hours = float(input("Enter hours worked for employee {}: ".format(employee.getEID())))
                employee.setHours(hours)
        elif choice == "c":
            employeeID = int(input("Enter employee ID:"))
            if employeeList.isEmpty():
                print("Employee doesn't exist.")               
            for employee in employeeList:
                if employee.getEID() == employeeID:
                    rate = float(input("Enter new wage for employee {}:".format(employee.getEID())))
                    employee.setRate(rate)
                    continue
                print("Employee doesn't exist.")
        elif choice == "d":
            print("*** Payroll***")
            for employee in employeeList:
                print(employee)
        elif choice == "e":
            employeeID = int(input("Enter employee ID:"))
            if employeeList.isEmpty():
                print("Employee doesn't exist.")   
            for employee in employeeList:
                if employee.getEID() == employeeID:
                    employeeList.remove(employee)
                    continue
                print("Employee doesn't exist.")
        elif choice == "f":
            print("Goodbye.")
            break
