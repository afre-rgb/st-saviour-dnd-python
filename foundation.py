from makeup import Makeup

class Foundation(Makeup):  
    def __init__(self, price: float, quality: bool, shade: int, coverage: str):
        super().__init__(price, quality)
        self.shade = shade
        self.coverage = coverage

    def oxidize(self): 
        pass