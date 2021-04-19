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

hourlyRate = 10                     # float(input("Enter hourly rate : "))
insuranceRate = 2.1                 #float(input("Enter insurance Rate : "))
taxRate = 6                       #float(input("Enter tax rate : "))
pfRate = 1.2                         #float(input("Enter pf rate : "))
bonus = 1000                        #float(input("Enter bonus : "))
HOURS = 40                         #int(input("Enter number of hours"))
empSalObj1 = EmployeeSalary(hourlyRate, insuranceRate, taxRate, pfRate, HOURS)

print(empSalObj1.calcMonthlySalary())
print(empSalObj1.calcMonthlyInsurance())
print(empSalObj1.calcMonthlyPfAmount())
print(empSalObj1.calcAnnualGrossSalary(bonus))
print(empSalObj1.calcAnnualNetPay(bonus))