from makeup import Makeup
from elf_blush import ElfBlush

if __name__ == "__main__":
    elf_blush = ElfBlush(price=15.0, quality=True, pigments=["rose"], liquid=False, type="powder")
    assert isinstance(elf_blush, Makeup)
    elf_blush.add_pigment(['cerulean'])
    print(elf_blush.pigments)
    # print(f"Elf Blush - Price: {elf_blush.price}, Quality: {elf_blush.quality}, Pigment: {elf_blush.pigment}, Liquid: {elf_blush.liquid}, Type: {elf_blush.type}")