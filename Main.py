""" Carrie West
 A Choose-Your-Own-Adventure Game"""
import random
import time

import NPCs



def gameOver():
    print("You have failed")


def collect(item):
    inventory.append(item)


def collection():
    print(inventory)


def location():
    print(area)

def group():
    if "Holly" in party:
        print(holly.name)
        print("Mood:",holly.mood)
        print("Opinion", holly.opinion)

def commands():
    print("HELP: Display the commands list"
          "\nGO (area): Move to the inputted area"
          "\nLOOK AROUND: Look around your current area"
          "\nCOLLECT (item): Add an item to your collection."
          "\nCOLLECTION: Take a look at your collection."
          "\nSEARCH (area): Take a thorough search of a specific place"
          "\nLOCATION: Gives you the name of your current location."
          "\nPARTY: Gives you a look at your current party and their status")


name = input("Hello! Before we start, what is your name?")
inventory = []
party= []
area = ""
knockCount = 0
pilotPath = "N"
heHim = ["he", "him", "his", "is"]  # Getting the user's pronouns for usage in in-game dialogue/descriptions
sheHer = ["she", "her", "her's", "is"]
theyThem = ["they", "them', their's", "are"]
otherPronouns = []
acceptedPronouns = "N"
pronounSet = input("What pronouns do you use? (He,She,They,Other, Just Use My Name)")
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
        isOrAre = input("Do these pronouns work with is, or are? (ex. 'They are' or 'She is')")
        print(otherPronouns)
        acceptedPronouns = input("Are these pronouns correct? (Y/N)")
        otherPronouns.append(isOrAre)
        pronounSet = otherPronouns
elif pronounSet == "Just Use My Name":
    otherPronounsOne = name
    otherPronouns.append(otherPronounsOne)
    otherPronounsTwo = name + "'s"
    otherPronouns.append(otherPronounsTwo)
    pronounSet = otherPronouns
# player is in coach, create NPC in first class that judges them for it
run = "N"
subRun = "N"
dialogue = "N"
while run != "Y":
    run = input("Ready to begin, " + name + "? (Y/N))")
    if run == "Y":
        print("You awake to a deafening silence.\n Your 5 o'clock flight should have landed by now, right?")
        print("(LOOK AROUND CABIN or SLEEP)")
    else:
        print("Alright, how about now?")
t_end = time.monotonic() + 60 * 2
print(time.monotonic())
print(t_end)
while time.monotonic() < t_end:
    print(time.monotonic())
    command = input("What are you going to do?")
    if command == "LOOK AROUND CABIN":
        print(
            "You peek up over the seat in front of you, apparently missing the whimsical sound of your fellow "
            "passenger's hacking cough. "
            "\n'They must be in the bathroom', you think. "
            "\nBut wait. Wasn't there someone in the seat next to them? (GET UP or STAY PUT)")
        command = ""
        subRun = "Y"
        while subRun == "Y":
            command = input("What are you going to do?")
            if command == "STAY PUT":
                area = "seat"
                print("You're right, you're probably just imagining things.")
                subRun = "N"
                # separating the branches from one another.
            elif command == "GET UP":
                print("There is no way you are imagining things. Worst case, you can use the bathroom. "
                      "\n'Maybe that's where they are' you think to yourself. "
                      "\n Hm, apparently not. There is no one here, or anywhere in Coach as far as you can see.")
                subRun = "N"
            else:
                command = ""
                print("You cannot do that right now.")
    elif command == "GO BATHROOM":
        area = "bathroom"
        print("You've had too many drinks to think about anything but sweet release."
              "\nYou move to the back of Coach, still unnerved by the absence of your fellow passengers "
              "(at least I hope you are)."
              "\n Hm. Occupied. Figures that would happen the exact time you need to go."
              "\n You hear crying from the other side of the door. Should you KNOCK or SPEAK?")
        command = ""
        subRun = "Y"
        while subRun == "Y":
            command = input("What are you going to do?")
            if command == "KNOCK" and knockCount <= 5:
                print("'Please go away', you hear in between sobs from behind the thin plastic door.")
                knockCount += 1
            elif command == "SPEAK":
                dialogue = "Y"
                while dialogue == "Y":
                    speech = input("It's usually rude to speak to strangers while they are in the bathroom, but go on "
                                   "ahead \n 'Who are you?', you hear in a meek and muffled voice.(ANSWER HONESTLY OR "
                                   "LIE)")
                    if speech == "ANSWER HONESTLY":
                        print("'A passenger? But you all...', the voice trails off."
                              "\nThe door unlocks and out comes a stewardess. The marks of dried tears run down her"
                              "cheeks. "
                              "\n 'Come with me and let's find out what's going on here."
                              "\n You aren't going to get to use the bathroom, are you?")
                        holly = NPCs.NPC("Holly", "shaken", 60)
                        party.append("Holly")
                        holly.mood = "Emboldened"
                        holly.opinion = 85 - knockCount
                        dialogue = "N"
                    if speech == "LIE":
                        print("Ah, wow, a brilliant and morally correct move. You stammer for a lie. 'I'm the captain',"
                              "you say, putting on your best impression of a pilot")
                        print("'You don't really sound like the captain.'")
                        lieSuccess = random.randint(0, 100)
                        print(lieSuccess)
                        speech = input("Uh oh, doesn't sound convinced. (COME CLEAN or LIE MORE)")
                        if speech == "COME CLEAN":
                            print("You can't keep doing this. You answer honestly about your lack of flying ability"
                                  "\n All you hear now is breathing."
                                  "\n..."
                                  "\n A deep sigh is heard as the door unlocks. Before you stands a stewardess, "
                                  "the marks of dried tears running down her cheeks."
                                  "\n'Come on now, let's sort this all out'.")
                            holly = NPCs.NPC("Holly", "shaken", 60)
                            party.append("Holly")
                            holly.mood = "Exhausted"
                            holly.opinion = 48 - knockCount
                            dialogue="N"
                        if speech == "LIE MORE" and lieSuccess <90:
                            print("You try your best to mimic Top Gun, telling the story of your best friend Goose and"
                                  "an incredibly long volleyball montage, you're just getting to the climax-"
                                  "\n 'Please just stop!', a muffled cry from behind the door. It unlocks, revealing"
                                  "a tired and incredibly annoyed stewardess. "
                                  "\n 'Just come along with me, if you are here then *someone* else must be here. ")
                            holly = NPCs.NPC("Holly", "shaken", 60)
                            party.append("Holly")
                            holly.mood = "P.O."
                            holly.opinion = 30 - knockCount
                            dialogue = "N"
                        if speech == "LIE MORE" and lieSuccess >= 90:
                            pilotPath = "Y"
                            print("You really truly insist that you are the pilot, mentioning times of bravery and"
                                  "aviation excellence. You take hold of your role and you truly become the pilot")
                            print("The door opens, a woman dressed in a steward outfit looks at you."
                                  "\n 'Why aren't you wearing your uniform?', she looks incredibly puzzled."
                                  "You, being the excellent liar you are, say you just sort of woke up like this.")
                            print(" 'Is the co-pilot here?' ")
                            print("Her name tag reads Holly. She is now following you around.")
                            holly = NPCs.NPC("Holly", "shaken", 60)
                            party.append("Holly")
                            holly.mood = "Relieved"
                            holly.opinion = 75 - knockCount
                            dialogue = "N"
                subRun = "N"
            if command == "KNOCK" and knockCount >= 5:
                print("The door slams open. You catch the brief glimpse of a stewardess. You drop to the ground as "
                      "she screams 'BEGONE, DEMON!'. The last thing you remember is the smell of stale peanuts. ")
                t_end = time.monotonic()
                subRun = "N"
    elif command == "LOOK AROUND" and location == "seat":
        command = input("Same as how you left it when you zonked out. The SAFETY MANUAL and the In-Flight MAGAZINE sit "
                        "in the pouch in front of you. The call assistance button lies above your head. Press it? (Y/N)")
    elif command == "SLEEP":
        print("Hm, still up in the air. Yeah, back to your nap.")
        t_end = time.monotonic()
    elif command == "COLLECTION":
        collection()
    elif command == "HELP":
        commands()
    elif command == "LOCATION":
        location()
    elif command == "PARTY":
        group()
    else:
        command = ""
        print("You cannot do that right now.")
gameOver()

