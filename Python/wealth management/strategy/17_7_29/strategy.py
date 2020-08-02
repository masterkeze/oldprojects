#strategy_base class
from broken_line import *
class strategy():
    def __init__(self):
        self.reserve = 10000
        self.longonly = True
        self.holding = 0
        self.current_price = 0.00
        self.property = 10000
        self.profit_line = broken_line()
        self.market_line = broken_line()
        self.holding_line = broken_line()
        self.short_period = 5
        self.long_period = 15
        self.date = None

    def get_property(self):
        self.property = int(self.reserve + self.holding*self.current_price)
        return self.property

    def set_reserve(self,value):
        if value>=0:
            self.reserve = value
            
    def get_line(self):
        return self.profit_line

    def update(self,point):
        self.market_line.add_point(point.title,point.date,point.value)
        self.date = point.date

        self.current_price = point.value
        self.marketing()

        self.get_property()

        self.profit_line.add_point(point.title,point.date,self.property)
        self.holding_line.add_point(point.title,point.date,self.holding)
        
        

    def get_average(self,duration):
        length = self.market_line.length
        if type(duration)==int and duration>0 and length >= duration:
            s = 0
            for t in range(length-1,length-duration-1,-1):
                s = s + self.market_line.points[t].value
            average = s/duration
            return average
        return None

    def marketing(self):
        if self.get_average(self.long_period) != None:
            short_average = self.get_average(self.short_period)
            long_average = self.get_average(self.long_period)

            if (short_average >= long_average):
                if self.reserve >= self.current_price*100:
                    temp_buy = int(self.reserve//(self.current_price*100))*100
                    self.holding = self.holding + temp_buy
                    self.reserve = self.reserve - temp_buy * self.current_price
                    
                    #print('+',self.holding,'at',round(self.current_price,2),'at',self.date,':',self.get_property())
            else:
                if self.holding > 0:
                    #print('-',self.holding,'at',round(self.current_price,2),'at',self.date,':',self.get_property())
                    self.reserve = self.reserve + self.holding * self.current_price
                    self.holding = 0
                    
            

















            
