class EmployeeSalary:
    
    def __init__(self, hourlyRate, insuranceRate, taxRate, pfRate, HOURS):
        self.hourlyRate = hourlyRate
        self.insuranceRate = insuranceRate
        self.taxRate = taxRate
        self.pfRate = pfRate
        self.HOURS = HOURS
    
    def get_hourlyRate(self):
        return self.hourlyRate
    def get_insuranceRate(self):
        return self.insuranceRate
    def get_taxRate(self):
        return self.taxRate
    def get_pfRate(self):
        return self.pfRate
    def get_HOURS(self):
        return self.HOURS
    
    def set_hourlyRate(self, hourlyRate):
        self.hourlyRate = hourlyRate
    def set_insuranceRate(self, insuranceRate):
        self.insuranceRate = insuranceRate
    def set_taxRate(self, taxRate):
        self.taxRate = taxRate
    def set_pfRate(self, pfRate):
        self.pfRate = pfRate
    def set_HOURS(self, HOURS):
        self.HOURS = HOURS
    

    def calcMonthlySalary(self):
        return HOURS * hourlyRate * 4
    def calcMonthlyInsurance(self):
        return self.calcMonthlySalary() * (insuranceRate)/100
    def calcMonthlyPfAmount(self):
        return self.calcMonthlySalary() * (pfRate)/100
    def calcAnnualGrossSalary(self, bonus):
        return bonus * (self.calcMonthlySalary()*12)
    def calcAnnualNetPay(self, bonus):
        return self.calcAnnualGrossSalary(bonus) - (self.calcAnnualGrossSalary(bonus) * taxRate) - (self.calcMonthlyInsurance()*12) - (self.calcMonthlyPfAmount() * 12)

hourlyRate = 10   #float(input("Enter hourly rate : "))
insuranceRate = 2.3 # float(input("Enter insurance Rate : "))
taxRate = 1.6 #float(input("Enter tax rate : "))
pfRate = 1.2 #float(input("Enter pf rate : "))
bonus = 10000    # float(input("Enter bonus : "))
HOURS = 20            #int(input("Enter number of hours"))
empSalObj1 = EmployeeSalary(hourlyRate, insuranceRate, taxRate, pfRate, HOURS)

print(empSalObj1.calcMonthlySalary())
print(empSalObj1.calcMonthlyInsurance())
print(empSalObj1.calcMonthlyPfAmount())
print(empSalObj1.calcAnnualGrossSalary(bonus))
print(empSalObj1.calcAnnualNetPay(bonus))

empSalObj2 = EmployeeSalary(hourlyRate, insuranceRate, taxRate, pfRate, HOURS)

empSalObj2.set_hourlyRate(30)
empSalObj2.set_insuranceRate(3.5)
empSalObj2.set_taxRate(6)
empSalObj2.set_pfRate(2.4)
empSalObj2.set_HOURS(20)
print(empSalObj2.get_hourlyRate())
print(empSalObj2.get_insuranceRate())
print(empSalObj2.get_taxRate())
print(empSalObj2.get_pfRate())
print(empSalObj2.get_HOURS())

print(empSalObj2.calcMonthlySalary())
print(empSalObj2.calcMonthlyInsurance())
print(empSalObj2.calcMonthlyPfAmount())
print(empSalObj2.calcAnnualGrossSalary(bonus))
print(empSalObj2.calcAnnualNetPay(bonus))