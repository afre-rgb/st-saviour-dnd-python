class  Player:
    def __init__(self, name:str):
        self.name = name
        self.inventory = []
        self.strength = 10

    def add_to_inventory(self, item: str):
        self.inventory.append(item)    