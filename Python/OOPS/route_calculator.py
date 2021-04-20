class RouteCalculator:

    def __init__(self, routeNo, numpassengers, isMember, isFirstTimeUser, haveCoupon):
        self.routeNo = routeNo
        self.numpassengers = numpassengers
        self.isMember = isMember
        self.isFirstTimeUser = isFirstTimeUser
        self.haveCoupon = haveCoupon
        Coupon = 5.00
        salesTax = 7.50
        
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
    def get_Coupon(self):
        return Coupon
    def get_salesTax(self):
        return salesTax
    
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
    def set_Coupon(self, Coupon):
        self.Coupon = Coupon
    def set_salesTax(self, salesTax):
        self.salesTax = salesTax
    
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



route_obj1 = RouteCalculator(1, 30, True, True, False)
print(route_obj1.calcRoutePrice())
print(route_obj1.calcMembershipDiscount())