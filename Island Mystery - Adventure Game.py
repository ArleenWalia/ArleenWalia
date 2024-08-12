#import random library
import random
#import time
import time

# Introduction
print("Welcome to Island Mystery!")
player_name = input("Please enter your player name: ")

# Attend the party
print(f"\nYou have received an invitation to a private island party. Do you wish to attend the party, {player_name}?")
answer = input("Enter 'y' to attend or 'n' to decline: ")
if answer == "n":
        print("You chose not to attend the party.")
        time.sleep(1)
        print("During the night of the party, as you look out into the city on your balcony, someone starts shooting at you.")
        answer1 = input("\nDo you: \n(a)Run inside \n(b)Stay outside")
        if answer1 == "a":
            print("Someone knocks on your door and shoots you.\nTHE END.")
            exit()
        else:
            print("You get shot.\n THE END.")
            exit()
else:
    print("\nYou head to the meet up destination and see your friends there.")
    print("Your 3 friends, Pearl, Andrew, and Kelly wait with you.")
    time.sleep(5)
    print("Here is a small description of your friends:")
    print("Pearl always wears pearls (how ironic). She’s a quiet girl who always reads murder mystery books.")
    print("Andrew is very athletic and always gets his shoes dirty.")
    print("Kelly loves playing cards and always wears fur coats.")
    time.sleep(15)


    # Boat ride to the island
    print("\nA boat pulls up and everyone boards. You show your invitation to the boatman.")
    time.sleep(1)
    print(f"“You may sit in the back {player_name}.”")
    time.sleep(1)
    print("When everyone boards the boat speeds off to the island. Dark clouds start rolling in and by the time you reach the island, the water has gotten choppy.")
    time.sleep(1)
    print("As you and your friends get off the boat the boat speeds back to the harbor.")
    time.sleep(15)


    # Arrival at the party
    print("\nA butler greets everyone, “Hello, welcome to Mr. and Mrs. Reed's party! Follow me inside.”")
    time.sleep(1)
    print("Everyone enters the house and is greeted by a maid in the living room.")
    time.sleep(1)
    print("Butler: “I’ll get everyone some water.”")
    time.sleep(1)
    print("You began to chatter with your friends waiting for the hosts.")
    time.sleep(15)


    # Suspicious activity
    print("\nThe Butler calls for the maid and she rushes out of the living room. Everyone looks confused.")
    answer2 = input("Do you say: 'Should we check it out?' (y/n): ")
    if answer2 == "y":
        print("\nYou get up and go into the hall and see the butler coming.")
        time.sleep(1)
        print(f"{player_name}: What’s going on? Why did the maid rush out?”")
        time.sleep(1)
        print("The maid is coming up behind the butler with a tray of water.")
        time.sleep(1)
        print("Butler:I just needed her to get the water for everyone. I had a phone call that I had to attend.")
        time.sleep(1)
        print("You walk back to the living room with the butler and the maid. The maid gives everyone water.")
        time.sleep(1)
        answer3 = input("Do you drink the water (y/n): ")
        if answer3 == "y":
            print("\nYou began choking and die from poison.")
            print("THE END.")
            exit()
        else:
            print("\nYou don’t drink water")
        time.sleep(5)
   
    # The first death.
    print("\nButler:I have some news for everyone. Mr. and Mrs. Reed are unable to make it because a storm has rolled in.")
    time.sleep(1)
    print("Kelly & Pearl: WHAT!")
    time.sleep(1)
    print("Butler: They said to make yourself feel at home.")
    time.sleep(1)
    print("Suddenly Andrew starts choking and falls to the ground. White foam spurted out of his mouth. Kelly, Pearl, & the maid all scream. Kelly faints.")
    answer4 = input("Do you tell everyone 'Don’t drink the water.' (y/n): ")
    if answer4 == "y":
        print("Everyone stays away from the glasses. Pearl and the maid tend to Kelly.")
        time.sleep(1)
        print("Pearl: Who did this!")
        time.sleep(1)
        print("Everyone looks at the maid.")
        time.sleep(1)
        print("Maid: I didn't do anything! I just got the water - 2 glasses were already filled so I used the tap to fill the other 2 glasses! \nI didn't know 1 had poison!")
        time.sleep(1)
        print("The maid and Pearl try to carry Kelly to one of the bedrooms. The butler comes in to help.")
        time.sleep(1)
        print("You wait and help bring Kelly into one of the rooms. When you all return to the living room you begin interrogating the maid again.")
        time.sleep(1)
        print("She repeats the same thing she was saying before and runs out crying.")
        answer5 = input("Do you: \n(a)Start interrogating the butler \n(b)Wait for her to come back")
        if answer5 == "a":
            print("Before you can start interrogating the butler he walks out of the room without a word.")
            time.sleep(10)
        else:
            print("As you stare at Andrew’s lifeless body - the butler gets up without a word and leaves the room.")
    print("30 seconds later there is a loud scream.")
    time.sleep(10)
    print("It is the maid.")
    time.sleep(5)
    print("You and Pearl run towards the sound but doesn’t see the Butler in sight. The maid is dead on the ground in the hallway.")
    time.sleep(1)
    print("Pearl: OMG! SHE'S DEAD! WHERE'S THE BUTLER?")
    time.sleep(1)
    print("Next to the maid’s dead body, you see a slip of paper on the ground.\n Pearl is behind you so you read out the text:")
    time.sleep(1)


    # The Riddle
    riddle = input("Riddle: What gets bigger the more you take away? ")
    if riddle == "a hole":
        print("You grab an umbrella from an umbrella stand and run outside. It’s still raining.")
        time.sleep(1)
        print("You look around for a hole with Pearl who stays by your side.")
        time.sleep(1)
        print("10 minutes later you stumble across a large dug-up hole and you see the Butler's body.")
        time.sleep(1)
        answer6 = input("Do you: \n(a)Check if the Butler is dead \n(b)Assume he is dead and go inside")
        if answer6 == "b":
            print("You open the door and get shot in the head before seeing who killed you. \nTHE END.")
            exit()
        else:
            print("You hand the umbrella over to Pearl and slide down to the Butler’s body.")
            time.sleep(1)
            print("You check if he’s breathing, but he’s not. You climb your way out of the hole and see the umbrella you handed to Pearl on the ground with no sight of Pearl.\n You look around and notice 2 pearls close to the hole. ")
            time.sleep(1)
   
    # Make assumption
    assumption = input("Would you like to make an assumption of who the murderer is? (y/n)")
    if assumption == "y":
        print("Here are the list of options:")
        time.sleep(1)
        options = input("\n(a)Andrew \n(b)Kelly \n(c)Maid \n(d)Pearl \n(e)Butler")
        if options == "a":
            print("Incorrect answer.")
            time.sleep(2)
            print("The killer came up behind you and smashed you in the head with a rock.")
            time.sleep(1)
            print("THE END.")
            exit()
        if options == "b":
            print("Correct answer!")
            time.sleep(2)
            print("You go inside the house and find a gun on the counter. \nYou see a trail of pearl beads leading to the room Kelly was resting in.")
            time.sleep(1)
            print("Kelly has a gun to Pearl’s head as she sobs.")
            time.sleep(1)
            print("Kelly: Drop the gun or I'll shoot her.")
            time.sleep(2)
            answer7 = input("\nDo you: \n(a)Drop the gun \n(b)Shoot Kelly")
            if answer7 == "a":
                print("You drop your gun and kick it to the side.")
                time.sleep(2)
                print(f"{player_name} Don't do this Kelly!")
                time.sleep(2)
                print("She shoots Pearl in the head and quickly shoots you before you can pick up the gun.")
                time.sleep(1)
                print("THE END.")
                exit()
            else:
                print("You pull the trigger of the gun and shoot Kelly.")
                time.sleep(2)
                print("You and Pearl survived!")
                time.sleep(1)
                print("Congradulations, you won the game!")
                exit()
        if options == "c":
            print("Incorrect answer.")
            time.sleep(2)
            print("The killer came up behind you and stabbed you in the head.")
            time.sleep(1)
            print("THE END.")
            exit()
        if options == "d":
            print("Incorrect answer.")
            time.sleep(2)
            print("The killer came up behind you and shot you in the head.")
            time.sleep(1)
            print("THE END.")
            exit()
        if options == "e":
            print("Incorrect answer.")
            time.sleep(2)
            print("The killer knocked you out and buried you alive.")
            time.sleep(1)
            print("THE END.")
            exit()


    # Don't make assumption
    else:
        answer8 = input("Would you like to go inside? (y/n)")
        if answer8 == "y":
            print("You run inside and see a trail of pearl beads leading to Kelly’s bedroom.")
            time.sleep(1)
            answer9 = input("\nDo you: \n(a)Follow the trail \n(b)Look for a weapon")
            if answer9 == "a":
                print("You have no weapon and follow the trail. \nYou open the door and Kelly has a gun to Pearl’s head. \nKelly smirk’s, and shoots both of you.")
                time.sleep(2)
                print("THE END.")
                exit()


            #choose a weapon
            else:
                weapon = input("There are 2 weapons: \n(a)Gun \n(b)Knife")
                if weapon == "a":
                    print(f"{player_name} chose gun.")
                    time.sleep(1)
                    print("\nYou follow the trail and open the door. \n Kelly has a gun to Pearl's head as she sobs in fear.")
                    time.sleep(1)
                    print("Kelly: Drop the gun or I'll shoot her.")
                    time.sleep(1)
                    answer10 = input ("Do you: \n(a)Drop the gun \n(b)Shoot Kelly")
                    if answer10 == "a":
                        print("You drop your gun and kick it to the side.")
                        time.sleep(1)
                        print(f"{player_name}: Don't do this Kelly! ")
                        time.sleep(1)
                        print("She shoots Pearl in the head and quickly shoots you before you can pick up the gun.")
                        time.sleep(2)
                        print("THE END.")
                        exit()
                    else:
                        print("You pull the trigger of the gun and shoot Kelly.")
                        time.sleep(2)
                        print("You and Pearl survive!")
                        time.sleep(2)
                        print("Congradulations, you won the game!")
                        exit()
                else:
                    print(f"{player_name} chose knife.")
                    time.sleep(1)
                    print("\nYou follow the trail and open the door. \n Kelly has a gun to Pearl's head as she sobs in fear.")
                    time.sleep(1)
                    print("Kelly: Drop you knifr or I'll shoot her.")
                    time.sleep(1)
                    answer11 = input("\nDo you: \n(a)Drop the knife \n(b)Throw the knife at Kelly")
                    if answer11 == "a":
                        print("You drop your knife and kick it to the side.")
                        time.sleep(2)
                        print(f"{player_name}: Don't do this Kelly!")
                        time.sleep(3)
                        print("She shoots Pearl in the head and quickly shoots you before you can pick up the knife.")
                        time.sleep(2)
                        print("THE END.")
                        exit()
                    else:
                        print("You throw the knife at Kelly, but your aim sucks.")
                        time.sleep(2)
                        print("She shoots you both")
                        time.sleep(2)
                        print("THE END.")
                        exit()
        else:
            print("You look around the island but find nothing.")
            time.sleep(1)
            answer12 = input("\nDo you: \n(a)Go inside \n(b)Try to swim away from the island")
            if answer12 == "b":
                print("You try to swim away but drown because you don't even know how to swim.")
                time.sleep(1)
                print("THE END.")
                exit()
            else:
                print("You run inside and see a trail of pearl beads leading to Kelly's bedroom.")
                time.sleep(1)
                answer13 = input("\nDo you: \n(a)Follow the trail (no weapon) \n(b)Look for a weapon")
                if answer13 == "a":
                    print("You have no weapon and follow the trail. \nYou open the door and Kelly has a gun to Pearl's head.")
                    time.sleep(1)
                    print("Kelly smirks and shoots you both.")
                    time.sleep(2)
                    print("THE END.")
                    exit()
                else:
                    weapon1 = input("\nThere are two weapons: \n(a)Gun \n(b)Knife")
                    if weapon1 == "a":
                        print(f"{player_name} chose gun.")
                        time.sleep(1)
                        print("You follow the trail and open the door. \n Kelly has a gun to Pearl's head as she sobs.")
                        time.sleep(2)
                        print("Kelly: Drop the gun or I'll shoot her.")
                        time.sleep(2)
                        answer14 = input("\nDo you: \n(a)Drop the gun \n(b)Shoot Kelly")
                        if answer14 == "a":
                            print("You drop your gun and kick it to the side.")
                            time.sleep(2)
                            print(f"{player_name}: Don't do this Kelly!")
                            time.sleep(2)
                            print("She shoots Pearl in the head and quickly shoots you before you can pick up the gun.")
                            time.sleep(2)
                            print("THE END.")
                            exit()
                        else:
                            print("You pull the trigger of the gun and shoot Kelly.")
                            time.sleep(2)
                            print("You and Pearl survived!")
                            time.sleep(2)
                            print("Congradulations, you won the game!")
                            exit()
                    else:
                        print(f"{player_name} chose knife.")
                        time.sleep(2)
                        print("\nYou follow the trail and open the door. \n Kelly has a gun to Pearl's head as she sobs in fear.")
                    time.sleep(1)
                    print("Kelly: Drop you knifr or I'll shoot her.")
                    time.sleep(1)
                    answer11 = input("\nDo you: \n(a)Drop the knife \n(b)Throw the knife at Kelly")
                    if answer11 == "a":
                        print("You drop your knife and kick it to the side.")
                        time.sleep(2)
                        print(f"{player_name}: Don't do this Kelly!")
                        time.sleep(3)
                        print("She shoots Pearl in the head and quickly shoots you before you can pick up the knife.")
                        time.sleep(2)
                        print("THE END.")
                        exit()
                    else:
                        print("You throw the knife at Kelly, but your aim sucks.")
                        time.sleep(2)
                        print("She shoots you both")
                        time.sleep(2)
                        print("THE END.")
                        exit()
