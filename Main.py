# Carrie West
# A Choose-Your-Own-Adventure Game
from typing import List, Any

import time


def gameOver():
    print("You have failed")


def collect(item):
    inventory.append(item)


def collection():
    print(inventory)


def commands():
    print("LOOK (area): Look around an area"
          "\nCOLLECT (item): Add an item to your collection."
          "\nCOLLECTION: Take a look at your collection."
          "\nSEARCH (area): Take a thorough search of a specific place")


# running = True
inventory = []
name = input("Hello! Before we start, what is your name?")
heHim = ["he", "him", "his"]  # Getting the user's pronouns for usage in in-game dialogue/descriptions
sheHer = ["she", "her", "her's"]
theyThem = ["they", "them', their's"]
otherPronouns = []
acceptedPronouns = "N"
pronounSet = input("What pronouns do you use? (He,She,They,Other)")
if pronounSet == "He":
    pronounSet = heHim
elif pronounSet == "She":
    pronounSet = sheHer
elif pronounSet == "They":
    pronounSet = theyThem
elif pronounSet == "Other":
    print("Awesome! You're valid.")
    while acceptedPronouns != "Y":
        otherPronounsOne = input("What should others use to refer to you? (ex: 'he' or 'she') ")
        otherPronouns.append(otherPronounsOne)
        otherPronounsTwo = input("What should others use to refer to you? (ex: 'her' or 'them')")
        otherPronouns.append(otherPronounsTwo)
        otherPronounsThree = input("What should others use to refer to your possessions? (ex: 'their's' or 'his')")
        otherPronouns.append(otherPronounsThree)
        print(otherPronouns)
        acceptedPronouns = input("Are these pronouns correct? (Y/N)")
        pronounSet = otherPronouns
# player is in coach, create NPC in first class that judges them for it
run = "N"
subRun = "N"
while run != "Y":
    run = input("Ready to begin, " + name + "? (Y/N))")
    if run == "Y":
        print("You awake to a deafening silence.\n Your 5 o'clock flight should have landed by now, right?")
        print("(LOOK AROUND CABIN or GO BACK TO SLEEP)")
    else:
        print("Alright, how about now?")
t_end = time.monotonic() + 60 * 2
print(time.monotonic())
print(t_end)
while time.monotonic() < t_end:
    print(time.monotonic())
    command = input("What are you going to do?")
    if command == "look around cabin" or command == "LOOK AROUND CABIN" or command == "Look Around Cabin":
        print(
            "You peek up over the seat in front of you, apparently missing the whimsical sound of your fellow "
            "passenger's hacking cough. "
            "\n'They must be in the bathroom', you think. "
            "\nBut wait. Wasn't there someone in the seat next to them? (GET UP or STAY PUT)")
        command = ""
        subRun = "Y"
        while subRun == "Y":
            command = input("What are you going to do?")
            if command == "stay put" or command == "STAY PUT" or command == "Stay Put":
                print("You're right, you're probably just imagining things.")
                subRun = "N"
            elif command == "get up" or command == "GET UP" or command == "Get Up":
                print("There is no way you are imagining things. Worst case, you can use the bathroom. "
                      "\n'Maybe that's where they are' you think to yourself. "
                      "\n Hm, apparently not. There is no one here, or anywhere in Coach as far as you can see.")
                subRun = "N"
            else:
                command = ""
                print("You cannot do that right now.")
    elif command == "collect book" or command == "COLLECT BOOK" or command == "Collect Book":
        collect("book")
        collection()
    elif command == "go back to sleep" or command == "GO BACK TO SLEEP" or command == "Go Back To Sleep":
        gameOver()
        t_end = time.monotonic()
    elif command == "COLLECTION":
        collection()
    else:
        command = ""
        print("You cannot do that right now.")
gameOver()
