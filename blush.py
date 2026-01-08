from makeup import Makeup

class Blush(Makeup):  
    def __init__(self, price: float, quality: bool, pigment: str, liquid: bool,):
        super().__init__(price, quality)
        self.pigment = pigment
        self.liquid = liquid

    def add_pigment(self):
        pass 