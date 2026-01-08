from blush import Blush

class ElfBlush(Blush):
    def __init__(self, price: float, quality: bool, pigments: list, liquid: bool, type: str):
        super().__init__(price, quality, pigments, liquid)
        self.type = type

    def shimmer(self):
        pass