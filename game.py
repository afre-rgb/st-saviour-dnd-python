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
    # name is created as a string and the input is stored as the name
    name = input('Name: ')
    player = Player(name)  

    print_dramatic_text(f'Yeooooo, {player.name}! What is up? Do you want to be bestfriends?') 
    friend_status = input('Type Yes! or I guess.')
    #friend_status is also created as a string and the input is stored 

    # f should be used in front of the text being printed if the variable is being used in said text
    print_dramatic_text(f'Okay. We should build a house together, {player.name}. But first, we need materials. We should go to the cave.')
    print_dramatic_text ('You enter the cave.')
    # using the random.randint function, a dice roll is simulated completely randomly, and the numbers are determined by whatever is in the parenthesis (in this case 1 and 6)    
    input ('Press Enter to roll a d6. ')
    roll = random.randint(1, 6)
    draw_d6(roll)  
    # depending on the number rolled, different outcomes will occur determined by the if statements
    if roll >= 3:
        print_dramatic_text(f'You rolled a {roll}, you receive an emerald!')
        player.add_to_inventory('emerald')   
        #if a certain circumstance is not met, else can be used to have an alternative outcome
    else: 
        print_dramatic_text(f'You rolled a {roll}, you receive rotten flesh!') 
        #item is appended to the inventory list due to the string being passed into the add_to_inventory method
        player.add_to_inventory('rotten flesh')
    #inventory is printed based off of what is added to it 
    print(f'Current inventory: {player.inventory}')  
    #depending on the circumstance, the strengh may be decreased. This is allowed because the strength is being set to a "new" strength using = and subtracting 1   
    if roll == 1 or roll == 2:  
        player.strength = player.strength - 1 
        print_dramatic_text('You fought a zombie and ingested rotton flesh by accident. Your strength decreased by 1 due to the poisoning.')  
        print_dramatic_text(f'Current strength: {player.strength}')
    else: 
        player.strength = 10   
        print_dramatic_text('You found an emerald in a chest! Your strength remains the same.')
        print_dramatic_text(f'Current strength: {player.strength}') 

    print_dramatic_text('You continue deeper into the cave and mine some cobblestone with your iron pickaxe.')
    print_dramatic_text('As you walk out the cave to start building your house, you come across a field of flowers. Hey bestfriend, do you want to pick up some flowers? Pick a couple and we can use them to craft dye for our beds.') 
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
    print_dramatic_text('You head to a grassy field and build a stone house, with great architecture and it feels like the homiest of homes.You dye your bed and place it. You become bored...but you decide to relax in your humble aboade.') 

    print_dramatic_text('You forgot to craft a door and a creeper walks in to blow up your house!')
    
    input ('Press Enter to roll a d4. ')
    roll = random.randint(1, 4)
    draw_d6(roll) 

    if roll  == 3 or roll == 2:
        strength = player.strength - 2 
        print_dramatic_text(f'You rolled a {roll}. Your house withstands the creeper explosion, but you took some damage while defending your home.')
        print_dramatic_text(f'Your strength decreased by 2. Current strength: {strength}')
    else:  
        print_dramatic_text(f'You defeated the creeper before it could blow up and your health remains the same.')
    
    print_dramatic_text('You realize you enjoyed the challenge and understand the importance of defense.It is time for an even greater adventure!') 
    print_dramatic_text('You head back to the cave to gather more resources. You find an ore of some kind.') 

    input ('Press Enter to roll a d3. ')
    roll = random.randint(1, 3)
    draw_d6(roll)

    if roll == 1: 
        player.add_to_inventory('Diamond sword') 
        print_dramatic_text(f'You rolled a {roll}, you found diamond! You may craft a diamond sword.')

    if roll == 2 or roll == 3: 
        player.add_to_inventory('Iron sword') 
        print_dramatic_text(f'You rolled a {roll}, you found iron! You may craft an iron sword.') 

    print_dramatic_text(f'Current inventory: {player.inventory}')
    print_dramatic_text('You continue to explore the cave and you find a chest with a diamond pickaxe! Now we must find obsidian to gain access to the nether!')
    player.add_to_inventory('Diamond pickaxe') 

    cave_choice = input('Do you want to go right of left? Type r for right and l for left')
    if cave_choice  == 'r': 
        print_dramatic_text('A skeleton appears!')  
        skeleton_choice = input ('Do you want to attack or run? Type a for attack and r for run. ') 
        

        if skeleton_choice == 'a': 
            roll = random.randint (1,3) 
            if roll == 1: 
                player.strength = player.strength -1 
                print_dramatic_text('Your strength decreased by 1 after you got hit by an arrow.') 
                print (f'Current strength: {player.strength}') 

            if roll == 2 or roll == 3: 
                print_dramatic_text('You defeated the skeleton without taking any damage and your health stays the same! You received a bow and arrow.') 
                player.add_to_inventory('Bow and Arrow')    

        if skeleton_choice == 'r': 
            print_dramatic_text('You ran away safely without taking any damage! Your strength stays the same.') 
         
    print(f'Current inventory: {player.inventory}') 

    if cave_choice == 'l': 
        print_dramatic_text('You found a chest! You recieved an enchanted golden apple! Your strength increased by 1.') 
        player.add_to_inventory('Enchanted golden apple') 
        player.strength = player.strength + 1  
        print (f'Current strength: {player.strength}')

    print_dramatic_text('You continue through the cave until you find obsidian. Once you find obsidian, you find flint and steel. Now you can build the portal!')
    player.add_to_inventory('Obsidian') 
    player.add_to_inventory('Flint and Steel')  

    nether_choice = input('Do you want to enter the nether? Type y for yes and ofc for Of course!. ') 
    print_dramatic_text('You enter the nether and eventually make eye contact with a ghast! You see a chest nearby.')  
    netherchest_choice = input('Do you want to go for the chest or go back through the portal? Type c for chest and r to return.') 

    if netherchest_choice == 'c': 
        roll = random.randint(1, 3) 
        draw_d6(roll)   

        if roll == 1: 
            player.strength = player.strength -1 
            print_dramatic_text('You rolled a 1. The ghast shoots a fireball at you while you are distracted by the chest. Your strength decreased by 1.') 
            print (f'Current strength: {player.strength}')
        else: 
            print_dramatic_text(f'You rolled a {roll}. You successfully grabbed the loot from the chest without getting hit! You received a healing potion and your strength increased by 2!') 
            player.add_to_inventory('Healing Potion')  
            player.strength = player.strength + 1 
            print (f'Current strength: {player.strength}') 

    if netherchest_choice == 'r':  
        print_dramatic_text('You returned through the portal, but the ghast followed you. Fortunately, it brang its family and its living its best life in the grassy fields! Your strength remains the same.')
# based off a player's inventory or choices, if statements can be used to create different outcomes
print_dramatic_text('It\'s time for one more adventure...') 
player.add_to_inventory('Ender Pearls') 

print_dramatic_text('You are teleported to the end and you are challenged to defeat the ender dragon. The dragon immdediately shoots fire at you! You try to pull out your sword but an enderman steals it from you!')
#item is removed from player inventory 
if player.inventory.count('Diamond sword') > 0:
    remove_item = 'Diamond sword' 
    player.remove_from_inventory(remove_item)  

if player.inventory.count('Iron sword') > 0:
    remove_item = 'Iron sword' 
    player.remove_from_inventory(remove_item)

input ('Press Enter to roll a d2. ')  
roll = random.randint(1, 2) 
draw_d6(roll)   

if roll == 1: 
    player.strength = player.strength -2 
    print_dramatic_text('You rolled a 1. You got hit by the dragon\'s fire breath. Your strength decreased by 2.') 
    print (f'Current strength: {player.strength}') 

if roll == 2: 
    print_dramatic_text('You rolled a 2. You dodged the dragon\'s fire breath and your strength remains the same!')

if player.inventory.count('Bow and Arrow') > 0: 
    print_dramatic_text('You use your bow and arrow to shoot the ender dragon!')   
else:
    print_dramatic_text('You throw a piece of Dubai chocolate at the ender dragon.')

print_dramatic_text('Ouch! Uh...I mean...I\'m totally not the ender dragon. Okay fine, let me explain...It gets lonely out here in the end!')
 
if friend_status == 'Yes!': 
        print_dramatic_text('You were so eager to be my bestfriend in the beginning. Bestfriends forever! You win!') 

if friend_status == 'I guess.': 
        print_dramatic_text('Well...I guess we are not bestfriends after all. The ender dragon defeats you. Game over.')

