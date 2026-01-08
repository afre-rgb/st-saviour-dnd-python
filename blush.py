from makeup import Makeup

class Blush(Makeup):  
    def __init__(self, price: float, quality: bool, pigments: list, liquid: bool,):
        super().__init__(price, quality)
        self.pigments = pigments
        self.liquid = liquid

    # TODO make variadic function with *args!
    def add_pigment(self, pigments: list):
        for pigment in pigments:
            self.pigments.append(pigment)