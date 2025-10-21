
class MyTradingStrategy: ##This is our base class
    def __init__(self, name):
        self.__name = name
    
    def generate_signal(self, price_data):
        print("This method is intened to be overridden.")
        return "Hold" 
    
    @property #Now people think its an attribute
    def name(self):
        return self.__name
    

Object = MyTradingStrategy("Awesome Strategy")
Object.generate_signal([11])
Object.name
    
class MySMAStrat(MyTradingStrategy): 
    def __init__(self, s_window, l_window):
        self.__s_window = s_window
        self.__l_window = l_window 
        super().__init__("My SMA Trading Strategy")

    def generate_signal(self, price_data):
        if len(price_data[-self.__l_window:]) < self.__l_window: #This is because the price_data array might be too short
            return "Hold"                                        #That's why the strategy does not work
        short_avg = sum(price_data[-self.s_window:])/self.s_window
        long_avg = sum(price_data[-self.l_window:])/self.l_window

        if short_avg > long_avg:
            return "Buy"
        elif short_avg < long_avg:
            return "Sell"
        else:
            return "Hold"

    @property 
    def s_window(self):
        return self.__s_window
    
    @property 
    def l_window(self):
        return self.__l_window
    
    
price_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
l_window = 5
s_window = 3