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
    
    def set_customerName(self, customerName):
        self.customerName = customerName
    def set_address(self, address):
        self.address = address
    def set_contactNumber(self, contactNumber):
        self.contactNumber = contactNumber
    def set_customerType(self, customerType):
        self.customerType  = customerType
    