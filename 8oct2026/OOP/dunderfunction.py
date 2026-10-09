class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr):
        return self.price>odr.price


odr1 = order("fries",100)
odr2 = order("burger",150)

print(odr1>odr2)