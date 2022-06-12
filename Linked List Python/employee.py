class Employee:
    idInteger = 1
    def __init__(self, name , rate = 0.0):
        self.name = name
        self.rate = rate
        self.id = Employee.idInteger
        self.hours = 0.0

    def getRate(self):
        return self.rate

    def getEID(self):
        return self.id

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getGrossPay(self):
        return self.hours*self.rate

    def __eq__(self, ID):
        return self.id == ID

    def setRate(self, newRate):
        self.rate = newRate

    def setHours(self, newHours):
        self.hours = newHours

    def __str__(self):
        return "Employee Name:"+self.name+"\nEmployee ID:"+str(self.id)+"\nHourly Rate:"+str(self.rate)+"\nHours Worked:"+str(self.hours)+"\nGross Pay:"+str(self.getGrossPay())
        


    

    