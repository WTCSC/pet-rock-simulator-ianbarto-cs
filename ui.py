#Created by AI with human assistance
#File: ui.py
#Description: This file contains functions to display the pet rock's status in a user-friendly way
import os

RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"

def bar(value, color):
    """Return a 10-block bar for a stat that goes from 0–10."""
    filled = value
    empty = 10 - filled
    return color + "█" * filled + RESET + "·" * empty

def display_status(happiness, hunger, thirst, boredom):
    """Draw the pet’s status dashboard using passed values."""
    os.system("cls" if os.name == "nt" else "clear")

    print("\n" + "═" * 40)
    print("      🪨 Pet Rock Vital Stats 🪨")
    print("═" * 40)

    print(f"😊 Happiness : {bar(happiness, GREEN)} {happiness}/10")
    print(f"🍖 Hunger    : {bar(hunger, YELLOW)} {hunger}/10")
    print(f"💧 Thirst    : {bar(thirst, BLUE)} {thirst}/10")
    print(f"😑 Boredom   : {bar(boredom, RED)} {boredom}/10")

    print("═" * 40 + "\n")

if __name__ == "__main__":
    # Example usage
    happiness = 7
    hunger = 3
    thirst = 5
    boredom = 1

    display_status(happiness, hunger, thirst, boredom)