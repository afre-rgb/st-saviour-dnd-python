from makeup import Makeup 

class setting_Powder(Makeup): 
    def __init__(self, price: float, quality: bool, finish: str, color: str):
        super().__init__(price, quality)
        self.finish = finish
        self.color = color  
        
        def mattify(self) 