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
                                        ans == input("You meet a Nun! She invites you for service. Accept? (yes/no) ").lower()
                                        if ans == "yes":
                                            ans == input("You and the Nun exchange information while walking to the church.. When you arrive, she opens the door to the basement. (continue) ").lower() 

                                            if ans == "continue":
                                                print("You follow the Nun down.. Out of nowhere, Multiple Nuns charge towards you and the door closes! What do you do? (fight/run/beg)")

                                                if ans == "fight":
                                                    print("You put your fists up.. The Nuns are too strong! They pin you down and use you as a sacrafice.")
                                                    print("You Died! Game over.")
                                                    break
                                                                                       
                        else:
                            print("You pack up and get ready to leave.")
                    else:
                        print("The old man's smile fades and he closes the door.")
                        print("You now walk back to the area you started from.")
                        visited_locations.add(choose_location)
                        continue
                elif ans == "back":
                    print("You decide to step away from the cabin and look at your map again.")
                    continue
                else:
                    print("Invalid choice. Please choose 'greet', 'punch', or 'run'.")
            
            elif ans == "back":
                print("You decide to leave the cabin and look at your map again.")
                continue
            else:
                print("Invalid choice. Please choose 'knock' or 'back'.")
        
        elif choose_location == "hidden_glade":
            print("You venture into the Hidden Glade and discover a small beautiful clearing filled with flowers.")
            ans = input("You spot a beautiful woman sitting on a rock. Do you wish to approach her? (yes/no) ").lower()
            if ans == "yes":
                print("The woman turns to you and whispers something strange...")
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
