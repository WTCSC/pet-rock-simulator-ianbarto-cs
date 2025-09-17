from variables import *
from time import sleep
import os
from ui import *

display_status(happiness, hunger, thirst, boredom)
sleep(1)
print(f"Hey, Im your pet rock! I woke up feeling amazing! My happiness is at {happiness}.")
sleep(1)


while True:
    action1 = input("What do you want to do? ([1] feed,[2] give water,[3] play,or [4] do nothing) ").strip().lower()
    if action1 == "1":
        hunger -= 6
        thirst -= 3
        boredom -= 3
        sleep(1)
        print("The food was 67 good!10/10")
        sleep(1)
        print("Thank you for feeding me!")
        sleep(1)
        print("I feel so much better now, and ready to get my day started!")
        sleep(1)

    elif action1 == "2":
        thirst -= 6
        hunger -= 3
        boredom += 3
        print("Ahh, that hits the spot!")
        sleep(1)
        print("Thank you for giving me a bevy!")
        sleep(1)

    elif action1 == "3":
        boredom -= 2
        hunger += 2
        thirst += 2
        print("Yay! I love playing!")
        sleep(1)
        print("Thank you for playing with me!")
        sleep(1)
        print("I feel so much less bored now!")
        sleep(1)
    elif action1 == "4":
        hunger += 2
        thirst += 2
        boredom += 4
        happiness -= 4
        print("Life is starting to get depressing...")
        sleep(1)
        print("I need you to do something with me!")
        sleep(1)
        print("If you don't do something with me soon, I will die...")
        sleep(1)
    else:
        print("Invalid action. Please choose feed, give water, play, or do nothing.")

    if hunger <= 0:
        hunger = 0
    if thirst <= 0:
        thirst = 0
    if boredom <= 0:
        boredom = 0
    if happiness >= 10:
        happiness = 10

    display_status(happiness, hunger, thirst, boredom)

    if hunger > 10:
        print("I have died of starvation...")
        break

    if thirst > 10:
        print("I have died of dehydration...")
        break

    if boredom > 10:
        print("I have died of boredom...")
        break  

    if happiness <= 0:
        print("I have died of sadness...")
        break

    end = input("Do you want to continue playing? (yes or no) ").strip().lower()
    if end == "no":
        print("Goodbye! Thanks for playing!")
        break



