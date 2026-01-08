class Makeup: 
    def __init__(self, price: float, quality: bool):
        self.price = price
        self.quality = quality

    def apply(self):  
        pass

    def sell(self): 
        pass
        
        # class SettingPowder(Makeup): 
        #      def __init__(self, finish: str, color: bool):
        #         super().__init__(price, quality)  
        #     def mattify(self): 

        # class elfBlushes(Blush):
        #     def __init__(self, type: str):
        #         super().__init__(pigment, liquid) 

        # class nyxFoundation(Foundation):
        #     def __init__(self, type: str):
        #         super().__init__(shade, coverage) 

        # class hudabeautySettingPowder(SettingPowder):
        #     def __init__(self, type:str):
        #         super().__init__(finish, color)
