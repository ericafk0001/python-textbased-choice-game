import sys

if sys.version_info < (3, 8):
    print("This game requires Python 3.8 or higher. Please update your Python installation.")
    exit(1)
# test

import random

print("Welcome to 'The Forgotten Woods'!")
print("You wake up in a dense forest with no memory of how you got there.")
print("A tattered map beside you shows three key locations: The Old Cabin, The Hidden Glade, and The Ancient Tree.")
print("Your goal: Escape the forest before nightfall.\n")

name = input("What is your name? ")

health = 100
visited_locations = set()
inventory = {}

# add items to inventory
def add_to_inventory(item, quantity=1):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Added {quantity} {item}(s) to your inventory.")

# remove items from inventory
def remove_from_inventory(item, quantity=1):
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        if inventory[item] == 0:
            del inventory[item]  # Remove the item completely if quantity is 0
        print(f"Removed {quantity} {item}(s) from your inventory.")
    else:
        print(f"Not enough {item}(s) in inventory to remove.")

# view inventory
def view_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

wants_to_play = input("Do you want to play? (yes/no) ").lower()
if wants_to_play == "yes":
    print(f"Welcome, {name}. Good luck! You start with 100 HP.")
    
    while True:
        choose_location = input("You look at your map... Would you like to venture into The Old Cabin, The Hidden Glade, or The Ancient Tree? (old_cabin/hidden_glade/ancient_tree) ").lower()
        
        if choose_location in visited_locations:
            print("You have already visited this area. Pick another location.")
            continue

        if choose_location == "old_cabin":
            ans = input("You walk up to the cabin and you smell food... Do you wish to knock on the door or go back? (knock/back) ").lower()
            
            if ans == "knock":
                print("You knock on the door, and an old man greets you.")
                ans = input("What would you like to do? (greet/punch/run) ").lower()
                
                if ans == "greet":
                    ans = input("The old man smiles and invites you inside to eat lunch. Do you accept? (yes/no) ").lower()
                    
                    if ans == "yes":
                        print("You get 1 sandwich!")
                        add_to_inventory("Sandwich")
                        ans = input("You and the old man are sitting at the dining table. You think about asking him about the Forest. Do you ask? (yes/no) ").lower()
                        
                        if ans == "yes":
                            print("Old Man: 'Hah, Well, it ain't just trees and shadows, boy. It's got a memory older than the stones beneath your feet. They say the trees whisper to each other, and if you listen too close, you might just hear somethin' you wish you hadn't.'")
                            ans = input("Ask about how to get out of the Forest? (yes/no) ").lower()
                            
                            if ans == "yes":
                                print("Old Man: Just go North East from here until you reach a giant mushroom. A wise kitten will guide you.")
                                ans = input("Do you listen to the Old Man? (yes/no) ").lower()

                                if ans == "yes":
                                    ans = input("You start going North East just like the Old Man said.. you come across a village! Do you wish to go in the village or go around? (village/around) ").lower()

                                    if ans == "village":
                                        print("You explore the village..")
                                        ans = input("You meet a Nun! She invites you for service. Accept? (yes/no) ").lower()
                                        if ans == "yes":
                                            ans = input("You and the Nun exchange information while walking to the church.. When you arrive, she opens the door to the basement. (continue) ").lower() 

                                            if ans == "continue":
                                                ans = input("You follow the Nun down.. Out of nowhere, Multiple Nuns charge towards you and the door closes! What do you do? (fight/run/beg) ").lower()

                                                if ans == "fight":
                                                    print("You put your fists up.. The Nuns are too strong! They pin you down and use you as a sacrafice.")
                                                    print("-100 HP")
                                                    print("You Died! Game Over.")
                                                    break

                                                elif ans == "run":
                                                    print("You burst through the door behind you and you dash as far away as you can from the Church..")                                        
                                                    print("You lose -5 HP for running so long")
                                                    health -= 5
                                                    print("You have", health, "HP")
                                                    ans = input("You are now outside the village.. Do you want to continue going North East or go back to the village? (continue/back) ")

                                                    if ans == "continue":
                                                        print("After a few hours through the forest.. You see a giant mushroom!")
                                                        print("You find the Cat resting on the Mushroom. You ask the Cat how to get out of the forest.")
                                                        print("Wise Cat: To leave this forest, follow my words carefully:")
                                                        print("Wise Cat: Head north until you reach a wide river. There’s no bridge, but look for the fallen tree—it’s sturdy enough to cross.")
                                                        print("Wise Cat: Once across, beware the thorn bushes to the west. They may look harmless, but they’ll trap anyone who strays too close.")
                                                        print("Wise Cat: Instead, keep going east until you find the old oak tree with twisted roots. Beneath it, you’ll find the path that leads you out.")   
                                                        print("Wise Cat: Be swift, traveler. The forest doesn’t take kindly to those who linger.")
                                                        ans = input("continue? (continue)")  
                                                        if ans == "continue":
                                                            print("You thank the wise cat and go North.. You reach the wide river the Cat mentioned and look for a fallen tree..")                                                
                                                            ans = input("You see the fallen tree and walk towards it until you realized that you are very tired.. Do you want to take a nap or cross the river? (cross/nap) ").lower()                                                
                                                            
                                                            if ans == "nap":
                                                                print("You decide to take a short nap before crossing the river.. Oh no! You got startled awake in the dark")
                                                                ans = input("You hear leaves ruffling all around.. Out of nowhere, a wolf jumps on top of you! Quick! You need to do something. (punch/run) ").lower()
                                                                
                                                                if ans == "punch":
                                                                    print("You channel all your energy into punching the wolf, but it is not affected at all.")
                                                                    print("The wolf's huge mouth open wide displaying his canine teeth.. Your vision goes blank.")
                                                                    print("You died by a wolf. Game Over.")
                                                                    break

                                                                else:
                                                                    print("You try to push yourself off the ground to run away, but the wolf's shear weight pins you down..")
                                                                    print("The wolf's huge mouth open wide displaying his canine teeth.. Your vision goes blank.")
                                                                    print("You died by a wolf. Game Over.")
                                                                    break
                                                            
                                                            else:
                                                                print("You decide to cross the fallen tree because you do not know what will happen at night..")
                                                                print("While crossing the tree, you almost slip.. You manage to stay balanced and cross to the other side!")
                                                                print("The sun is starting to set down, so you can't see that well..")
                                                                ans = input("On your west, you spot some bushes with something sharp that looks like berries. On your east, there are just trees. Do you go west or east? (west/east) ")
                                                                
                                                                if ans == "east":
                                                                    print("You head eastbound and find an huge oak tree.. you see a path!")
                                                                    print("You follow the path, and soon enough you come out the forest!")
                                                                    print("You escaped the forest before nightfall! You win!")
                                                                    break

                                                                else:
                                                                    print("You go west to the bushes.. You decide to pick some of the berries for later.")
                                                                    print("You get poked by something sharp, and turns out the berries were actually thorns the cat was talking about!")
                                                                    print("You start bleeding from your finger.. your vision gets blurry")
                                                                    print("You died by poisonous bushes. Game Over.")
                                                                    break
                                                                    
                                                    else:
                                                        print("You decide to go back to the village.. While exploring the village you cross paths with the Nuns again!")
                                                        print("You try to run again but having been exhausted before, you do not get far before the Nuns catch you!")
                                                        print("A punch knocks you out. You do not wake up again.")
                                                        print("You died from being sacrificed. Game Over.")     
                                                        break 

                                                else:
                                                    print("You get on your knees and beg to not be sacrificed..")  
                                                    print("The Nuns gather in a circle and start whispering to each other..")   
                                                    if random.random() < 0.35:  # 35% chance
                                                        print("The Nuns decide to spare you and let you off with a warning to not tell anyone.")
                                                        print("You run as far as you can away out the village.. finally, you reach a huge oak tree!")
                                                        ans = input("You see a path.. Do you follow the path or continue going North East? (follow/continue) ").lower()

                                                        if ans == "follow":
                                                            print("You follow the path, and soon enough you come out the forest!")
                                                            print("You escaped the forest before nightfall! You win!")  
                                                            break                                                         
                                                        else:
                                                            print("You continue going North East.. after hours you are still in the forest.")
                                                            print("The sun is starting to set and it's getting dark. What do you want to do? (sleep/eat) ")

                                                            if ans == "sleep":
                                                                print("You decide to take a short nap before crossing the river.. Oh no! You got startled awake in the dark")
                                                                ans = input("You hear leaves ruffling all around.. Out of nowhere, a wolf jumps on top of you! Quick! You need to do something. (punch/run) ").lower()
                                                                
                                                                if ans == "punch":
                                                                    print("You channel all your energy into punching the wolf, but it is not affected at all.")
                                                                    print("The wolf's huge mouth open wide displaying his canine teeth.. Your vision goes blank.")
                                                                    print("You died by a wolf. Game Over.")
                                                                    break

                                                                else:
                                                                    print("You try to push yourself off the ground to run away, but the wolf's shear weight pins you down..")
                                                                    print("The wolf's huge mouth open wide displaying his canine teeth.. Your vision goes blank.")
                                                                    print("You died by a wolf. Game Over.")
                                                                    break
                                                            else:
                                                                remove_from_inventory("Sandwich")
                                                                print("You eat 1 sandwich.")
                                                                print("It's night and the sun has set..")
                                                                print("You lost! You didn't escape the forest before nightfall.")
                                                                break
                                                    else:
                                                        print("The Nuns decide that sparing you would anger their deity and proceed with the sacrifice!")     
                                                        print("You died from being sacrificed. Game Over.")                                          
                                                        break  

                                        else:
                                            print("You politely decline the Nun's offer. The Nun shoots a dirty glare at you and leaves.")
                                            ans = input("You see a bar and a weaponsmith. Where do you want to go? (bar/weaponsmith) ").lower()

                                            if ans == "bar":
                                                print("You head to the bar.. as soon as you enter everyone stops talking and stares at you.")
                                                ans = input("What do you want to say? (greet/stare)").lower()

                                                if ans == "greet":
                                                    print("You introduce yourself to the bar.. The people welcome you and everyone goes back to drinking")
                                                    print("A woman walks up to you..")
                                                    ans = input("Woman: Hey! What brings you to this small town of ours?").lower()
                                                    print("You think about asking for a drink or asking how to get out of the forest.. (drink/ask) ")

                                                    if ans == "drink":
                                                        print("You tell the woman that you want to drink.. She buys you a pint on her.")
                                                        print("Before long, you two test each other on who can drink the most..")
                                                        print("You drink too much and pass out. It becomes night time.")
                                                        print("You lose! You drank too much and couldn't escape the forest before nightfall.")
                                                        break

                                                    else:
                                                        print("You ask about directions to leave the forest.")
                                                        print("Woman: You just need to go east of here and you will get out of the forest! Did you not remember where you came from?")
                                                        ans = input("You ignore her and thank her for the directions. (continue) ").lower()
                                                        
                                                        if ans == "continue":
                                                            print("You go East like the woman said and eventually you see some open grass..")
                                                            print("You come out of the forest!")
                                                            print("You win! You escaped the forest before nightfall.")
                                                            break  
                                                
                                                else: 
                                                    print("People: Who do you think you are!")
                                                    print("The people beat you up.")
                                                    print("You died! Game Over.")
                                                    break
                                            
                                            else: 
                                                print("You go to the weaponsmith and get a free sword.")
                                                add_to_inventory("Bronze Sword")
                                                ans = input("You come out of the weaponsmith. The sun is setting now. Where do you want to go? (bar/northeast)").lower()
                                                    
                                                if ans == "northeast":
                                                    print("You go northeast and through the thick forest you see an open plains!")
                                                    print("Suddenly you see from your right eye, a orc charges at you!")
                                                    ans = input("You dodge swiftly. Do you want to run to the grass or fight the orc? (fight/run) ").lower()
                                                    if ans == "fight":
                                                        print("You pull out the sword you got before.")
                                                        print("The orc backs up slowly.. Then runs at you!!")
                                                        ans = input("Step back or slash? (step_back/slash) ")

                                                        if ans == "slash":
                                                            print("You wait for the perfect timing . . .")
                                                            print("You slash the orc in half!")
                                                            print("You walk towards the grass you saw earlier.")
                                                            print("You win! You escaped the forest before nightfall.")
                                                        
                                                        else:
                                                            print("You step back.")
                                                            print("The orc changes direction fast and lands a punch on you! (-50 HP)")
                                                            health -= 50
                                                            print("What do you do now? (attack/run) ")
                                    else:
                                        print("You decide to go around the village and come across a pack of goblins..")
                                        ans = input("What do you do now? (run/fight) ").lower()

                                        if ans == "run":
                                            print("You tried to run away from the gang of goblins but they chase up to you!")
                                            print("You died by a group of goblins. Game Over.")
                                            break

                                        else:
                                            print("You stand your ground and fight the goblins.. A goblin bigger than the rest of the goblins charges towards you!")
                                            ans = input("What do you want to do? (punch/throw_sandwich) ")
                                            
                                            if ans == "punch":
                                                print("You throw a punch but it does nothing. . .")
                                                print("You died by the leader goblin splitting you in half. Game Over.")
                                                break

                                            elif ans == "throw_sandwich":
                                                if "Sandwich" in inventory and inventory["Sandwich"] > 0:
                                                    remove_from_inventory("Sandwich")
                                                    print("You grab the sandwich you got from the old man and throw it at the goblin.")
                                                    print("All the other goblins run for it and they all start fighting each other for your sandwich.")
                                                    print("You sneak away while they are busy and continue heading northeast.")
                                                    print("You come across a clearing and see the sun setting, you quickly run into the clearing..")
                                                    print("You win! You escaped the forest before nightfall.")
                                                    break
                                                else:
                                                    print("You don't have a sandwich! The goblins realize you're bluffing.")
                                                    print("They get angry and eat you instead. Game over.")
                                                    input("Press any key to exit the game.")
                                                    break  

                        else:
                            print("You pack up and get ready to leave.")
                    else:
                        print("The old man's smile fades and he closes the door.")
                        print("You now walk back to the area you started from.")
                        continue
                elif ans == "punch":
                    print("You punch the Old Man in the face . . .")
                    print("He dodges it! He returns a punch that knocks you out... When you wake up you find yourself tied next to a lake.")
                    print("Old Man: You won't see the sun again.")
                    print(". . .")
                    print("You died by drowning in a lake. Game Over.")
                    break

                elif ans == "run":
                    print("You decide to run away and trip over some vines.")
                    print("You fall to your death into a ravine. Game Over.")
                    break

                else:
                    print("Invalid choice. Please choose 'greet', 'punch', or 'run'.")
            
            elif ans == "back":
                print("You decide to step away from the cabin and look at your map again.")
                continue
            else:
                print("Invalid choice. Please choose 'knock' or 'back'.")
                break
        
        elif choose_location == "hidden_glade":
            print("You venture into the Hidden Glade and discover a small beautiful clearing filled with flowers.")
            ans = input("You spot a beautiful woman sitting on a rock. Do you wish to approach her? (yes/no) ").lower()
            if ans == "yes":
                print("The woman turns to you and whispers something strange...")
                print("All of a sudden you stinging pain throughout your entire body")
                print("You died by witch magic. Game Over.")
                break
            else:
                print("You decide not to disturb her and leave the glade.")
            visited_locations.add(choose_location)
            continue
        
        elif choose_location == "ancient_tree":
            print("You approach the Ancient Tree and feel its immense aura.")
            print("The Ancient Tree's aura affects your health! +10 HP.")
            health += 10
            print(f"Your health is now {health}.")
            ans = input("You go back to where you woke up. (type 'continue' to proceed.) ").lower()
            if ans == "continue":
                visited_locations.add(choose_location)
                continue
        
        else:
            print("Invalid choice. Please choose a valid location.")
else:
    print("Maybe next time!")
