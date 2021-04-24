class RouteCalculator:

    def __init__(self, routeNo, numpassengers, isMember, isFirstTimeUser, haveCoupon):
        self.routeNo = routeNo
        self.numpassengers = numpassengers
        self.isMember = isMember
        self.isFirstTimeUser = isFirstTimeUser
        self.haveCoupon = haveCoupon
        
        
    # def __init__(self):
    #     pass
    
    def get_routeNo(self):
        return self.routeNo
    def get_numpassengers(self):
        return self.numpassengers
    def get_isMember(self):
        return self.isMember
    def get_isFirstTimeuser(self):
        return self.isFirstTimeUser
    def get_haveCoupon(self):
        return self.haveCoupon
    # def get_Coupon(self):
    #     return Coupon
    # def get_salesTax(self):  
    #     return salesTax
    
    def set_routeNo(self, routeNo):
        self.routeNo = routeNo
    def set_numpassengers(self, numpassengers):
        self.numpassengers = numpassengers
    def set_isMember(self, isMember):
        self.isMember = isMember
    def set_isFirstUser(self, isFirstTimeUser):
        self.isFirstTimeUser = isFirstTimeUser
    def set_haveCoupon(self, haveCoupon):
        self.haveCoupon = haveCoupon
    # def set_Coupon(self, Coupon):  these are not required as they are not attributes which are to be defined
    #     self.Coupon = Coupon
    # def set_salesTax(self, salesTax):
    #     self.salesTax = salesTax
    
    def calcRoutePrice(self):
        if self.routeNo == 1:
            if self.numpassengers == 1:
                return 35
            elif self.numpassengers == 2:
                return 60
            elif self.numpassengers > 2:
                return self.numpassengers * 26.50
        elif self.routeNo == 2:
            if self.numpassengers == 1:
                return 32.89
            elif self.numpassengers == 2:
                return 53.12
            elif self.numpassengers > 2:
                return self.numpassengers * 24.20
        elif self.routeNo == 3:
            if self.numpassengers == 1:
                return 38
            elif self.numpassengers == 2:
                return 63.78
            elif self.numpassengers > 2:
                return self.numpassengers * 28.78
        else:
            return "Route number should be 1 or 2 or 3"

    def calcMembershipDiscount(self):
        if self.isMember:
            if self.numpassengers == 1:
                if self.routeNo == 1:
                    return 35 * 5.0/100
                elif self.routeNo == 2:
                    return 32.89 * 5.0/100
                elif self.routeNo >3:
                    return 38 * 5.0/100
            elif self.numpassengers == 2:
                if self.routeNo == 1:
                    return 60 * 6.2/100
                elif self.routeNo == 2:
                    return 53.12 * 6.2/100
                elif self.routeNo == 3:
                    return 63.78 * 6.2/100
            elif self.numpassengers>2:
                if self.routeNo == 1:
                    return (self.numpassengers * 26.50) * 8.0/100
                elif self.routeNo == 2:
                    return (self.numpassengers * 24.20) * 8.0/100
                elif self.routeNo == 3:
                    return (self.numpassengers * 28.78) * 8.0/100
        else:
            return 0.0

    def calcFirstTimeUserDiscount(self):
        if self.isFirstTimeUser: 
            if self.numpassengers == 1:
                if self.routeNo == 1:
                    return 35 * 10.0/100
                elif self.routeNo == 2:
                    return 32.89 * 10.0/100
                elif self.routeNo >3:
                    return 38 * 10.0/100
            elif self.numpassengers == 2:
                if self.routeNo == 1:
                    return 60 * 7.0/100
                elif self.routeNo == 2:
                    return 53.12 * 7.0/100
                elif self.routeNo == 3:
                    return 63.78 * 7.0/100
            elif self.numpassengers>2:
                if self.routeNo == 1:
                    return (self.numpassengers * 26.50) * 4.0/100
                elif self.routeNo == 2:
                    return (self.numpassengers * 24.20) * 4.0/100
                elif self.routeNo == 3:
                    return (self.numpassengers * 28.78) * 4.0/100
        else:
            return 0.0

    def calcCouponDiscount(self):
        if self.haveCoupon:
            if self.numpassengers == 1:
                if self.routeNo == 1:
                    return 35 - 5.0
                elif self.routeNo == 2:
                    return 32.89 - 5.0
                elif self.routeNo >3:
                    return 38 - 5.0
            elif self.numpassengers == 2:
                if self.routeNo == 1:
                    return 60 - 5.0
                elif self.routeNo == 2:
                    return 53.12 - 5.0
                elif self.routeNo == 3:
                    return 63.78 - 5.0
            elif self.numpassengers>2:
                if self.routeNo == 1:
                    return (self.numpassengers * 26.50) - 5.0
                elif self.routeNo == 2:
                    return (self.numpassengers * 24.20) - 5.0
                elif self.routeNo == 3:
                    return (self.numpassengers * 28.78) - 5.0
        else:
            return 0.0
    def totalPrice(self):
        if self.isMember and self.isFirstTimeUser and self.haveCoupon:
            return self.calcCouponDiscount() - self.calcMembershipDiscount() - self.calcFirstTimeUserDiscount()
    def totalPriceWithSalesTax(self):
        return self.totalPrice() * salesTax /100 

Coupon = 5.00
salesTax = 7.50

route_obj1 = RouteCalculator(0,20, True, True, True)
print(route_obj1.calcRoutePrice())
print(route_obj1.calcMembershipDiscount())
print(route_obj1.calcFirstTimeUserDiscount())
print(route_obj1.calcCouponDiscount())
print(route_obj1.totalPrice())
print(route_obj1.totalPriceWithSalesTax())
print("Please try again” )