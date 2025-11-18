import random
import time

from player import Player
from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    name = input('Name: ')
    player = Player(name) 

    print_dramatic_text(f'Yeooooo, {player.name}! What is up? Do you want to be bestfriends?') 
    friend_status = input('Type Yes! or I guess.')


    print_dramatic_text(f'Okay. We should build a house together, {player.name}. But first, we need materials. We should go to the cave.')
    print_dramatic_text ('You enter the cave.')
        
    input ('Press Enter to roll a d6. ')
    roll = random.randint(1, 6)
    draw_d6(roll)  
    if roll >= 3:
        print_dramatic_text(f'You rolled a {roll}, you receive an emerald!')
        player.add_to_inventory('emerald')  
    else: 
        print_dramatic_text(f'You rolled a {roll}, you receive rotten flesh!') 
        player.add_to_inventory('rotten flesh')

    print(f'Current inventory: {player.inventory}') 
    if roll == 1 or roll == 2: 
        player.strength = player.strength - 1 
        print_dramatic_text('You fought a zombie and ingested rotton flesh by accident. Your strength decreased by 1 due to the poisoning.')  
    
    else: 
        player.strength = 10   
        print_dramatic_text('You found an emerald in a chest! Your strength remains the same.')

    print (f'Current strength: {player.strength}') 
    print_dramatic_text('You continue deeper into the cave and mine some cobblestone with your iron picckaxe.')
    print_dramatic_text('As you walk out the cave to start building your house, you come across a field of flowers.Hey {player.name}, do you want to pick up some flowers? Pick a couple and we can keep some, and use the others to dye our beds') 
    input('Which flowers would you like to pick: Lilies of the Valley, Blue Orchids, or Pink Tulips?') 
    flower_choice = input('Which flowers would you like to pick: Lilies of the Valley, Blue Orchids, or Pink Tulips? ')
   
    if flower_choice == 'Lilies of the Valley':  
        player.add_to_inventory('White Dye')
    if flower_choice == 'Blue Orchids': 
        player.add_to_inventory('Light Blue Dye') 
    if flower_choice == 'Pink Tulips': 
        player.add_to_inventory('Pink Dye')  

    print_dramatic_text(f'Great choice! You picked {flower_choice} and received dye for your bed!')
    print(f'Current inventory: {player.inventory}') 
    print_dramatic_text('We should build our house now!') 
    print_dramatic_text('You head to a grassy field and build a stone house, with great architecture and the homiest of homes.You dye your bed, amd place it. You become bored...but you decide to relax in your humble aboade.') 
    print('