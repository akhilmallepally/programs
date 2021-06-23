class Starbucks:
    '''This class provides methods for calculating the bill for the entered items and balance
    to be returned for customer upon paying the final bill amount.'''
    def __init__(self, customerName, address, contactNumber, customerType):
        self.customerName = customerName
        self.address = address
        self.contactNumber = contactNumber
        self.customerType = customerType        
        billReciept = ""
        billAmount = 0
        order = ""
    
    def get_customerName(self):
        return customerName
    def get_address(self):
        return address
    def get_contactNumber(self):
        return contactNumber
    def get_customerType(self):
        return customerType
    def get_billReceipt():
        return billReciept
    def get_billAmount():
        return billAmount
    def get_order():
        return order

    
    
    def set_customerName(self, customerName):
        self.customerName = customerName
    def set_address(self, address):
        self.address = address
    def set_contactNumber(self, contactNumber):
        self.contactNumber = contactNumber
    def set_customerType(self, customerType):
        self.customerType  = customerType

    def get_nameInitials(self):
        out = ""
        if len(customerName)>0:
            for

        else:
            return "no customer name given"


    def get_itemName(self, itemNumber):
        if itemNumber ==1:
            return 'Ham & Swiss Panini'
        elif itemNumber ==2:
            return 'Cheese & Fruit Bistro Box'
        elif itemNumber ==3:
            return 'Turkey Pesto Panini'
        elif itemNumber ==4:
            return 'Salted Caramel or Birthday Cake Pop'
        elif itemNumber ==5:
            return 'Roasted Tomato & Mozzarella Panini'
        return ""

    def get_itemCost(self, getItemName):
        itemCost = 0.0
        if self.get_itemName() == "Ham & Swiss Panini":
            return itemCost = 5.25;
        elif self.get_itemName() == "Cheese & Fruit Bistro Box":
            return itemCost = 4.95;
        elif self.get_itemName() ==  "Turkey Pesto Panini":
            return itemCost = 5.96;
        elif self.get_itemName == "Salted Caramel or Birthday Cake Pop":
            return itemCost = 3.50;
        elif self.get_itemName == "Roasted Tomato & Mozzarella Panini":
            return itemCost = 3.46;
        else:
            return itemCost = 0.0;
        
    def updateReceipt(self, quantity, itemNumber):
        count = count +1
        self.billAmount = self.get_itemCost(self.get_itemName(itemNumber)) *quantity
        if(count ==1):
            this.billReciept = "The Following is the bill for purchased products"
            self.get_itemName(itemNumber) + '(' + self.get_itemCost(self.get_itemName(itemNumber)) +')' + quantity+ ''='' +self.billAmount  
        else:
            this.billReciept += self.get_itemName(itemNumber)+self.getItemCost(self.get_itemName(itemNumber)) + quantity '='+self.billAmount


    def get_discount(self):
        if self.get_customerType() == Regular and self.billAmount>10.00:
            return self.billAmount * 10/100
        else:
            return self.billAmount
    
    def get_salesTax(self):
        return self.billAmount*8/100

    def get_finalBillAmount(self):
        return self.billAmount + get_salesTax() - get_discount()

    def get_finalBillReceipt(self):
        print('The Following is the bill for purchased products\n'
         + get_itemName()+'('+get_itemCost()+') * '+quantity + '='+ self.billAmount +'\n'+
         + get_itemName()+ '('+get_itemCost()+') * '+quantity + '='+self.billAmount+
         '\n           Sales Tax = ' get_salesTax()+ '\n         discount = '+get_discount()
         +'\n-------------------------------------------\n'+'Total Bill = '+get_finalBillAmount()
         +'\n ---------------------------------------------')

    def get_orderWithName():
        




