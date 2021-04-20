class Laptop:
    def __init__(self, laptopBrand, processor, operatingSystem, hardDrive, display, touch):
        self.laptopBrand = laptopBrand
        self.processor = processor
        self.operatingSystem = operatingSystem
        self.hardDrive = hardDrive
        self.display = display
        self.touch = touch

    def __init(self):                       #no arg constructor
        pass

    def getLaptopBrand(self):
        return self.laptopBrand
    def getProcessor(self):
        return self.processor
    def getOperatingSystem(self):
        return self.operatingSystem
    def getHardDrive(self):
        return self.hardDrive
    def getDisplay(self):
        return self.display
    def getTouch(self):
        return self.touch
    
    def setLaptopBrand(self, laptopBrand):
        self.laptopBrand = laptopBrand
    def setProcessor(self, processor):
        self.processor = processor
    def setOperatingSystem(self, operatingSystem):
        self.operatingSystem = operatingSystem
    def setHardDrive(self, hardDrive):
        self.hardDrive = hardDrive
    def setDisplay(self, display):
        self.display = display
    def setTouch(self, touch):
        self.touch = touch

    def __str__(self):
        return  "Laptop Brand is : " , self.getLaptopBrand() , "\nName of the processor is : ", self.getProcessor(),"\nOperating System name : ", self.getOperatingSystem(), "\nHard Drive capacity in GB's : ", self.getHardDrive(), "\nScreen Size : " ,self.getDisplay(),"\nis Touch : " ,self.getTouch()

object1 = Laptop("HP", "Intel i5","Debian",512,12.4, True)
print("*Testing getter method on object1*")
print("Laptop Brand is: ",object1.getLaptopBrand() , "\nName of the processor is: "+object1.getProcessor() ,
                        "\nOperating System name: "+object1.getOperatingSystem() , "\nHard Drive capacity in GB's: ",object1.getHardDrive() ,
                        "\nScreen Size: ",object1.getDisplay() , "\nis Touch: ",object1.getTouch())


print("*Testing toString method on object1*")
print(object1.__str__())