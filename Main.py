""" Carrie West
 A Choose-Your-Own-Adventure Game"""
import random
import time
import NPCs


def game_over():
    """
    Prints a message informing the user of their failure.
    :return:
    """
    print("You have failed")


def collect(item):
    """
    Takes an item from the environment and
    places it in the user's inventory.
    :param item: item
    :return:
    """
    inventory.append(item)


def collection():
    """
    Displays the user's inventory.
    :return:
    """
    print(inventory)


def location():
    """
    Gives the user the name of their current location.
    :return:
    """
    print(area)


def group():
    """
    Displays the Names, Moods and Opinion Levels of each party member
    :return:
    """
    if "Holly" in party:
        print(holly.name)
        print("Mood: ", holly.mood)
        print("Opinion: ", holly.opinion)
    if "Louis" in party:
        print(louis.name)
        print("Mood: ", louis.mood)
        print("Opinion: ", louis.opinion)


def commands():
    """
    Displays a list of possible commands for the user to use.
    :return:
    """
    print("HELP: Display the commands list"
          "\nGO (area): Move to the inputted area"
          "\nLOOK AROUND: Look around your current area"
          "\nCOLLECT (item): Add an item to your collection."
          "\nUSE (item): Put an item to good use."
          "\nCOLLECTION: Take a look at your collection."
          "\nSEARCH (place): Take a thorough search of a specific place"
          "\nLOCATION: Gives you the name of your current location."
          "\nPARTY: Gives you a look at your current party and their status")


name = input("Hello! Before we start, what is your name?")
inventory = []
party = []
area = ""
knockCount = 0
pilotPath = "N"
safetyInfo = "N"
heHim = ["he", "him", "his", "is"]  # Getting the user's pronouns for dialogue
sheHer = ["she", "her", "her's", "is"]
theyThem = ["they", "them', their's", "are"]
otherPronouns = []
acceptedPronouns = "N"
pronounSet = input("What pronouns do you use? (He,She,They,Other,Just Use "
                   "My Name)")
if pronounSet == "He":
    pronounSet = heHim
elif pronounSet == "She":
    pronounSet = sheHer
elif pronounSet == "They":
    pronounSet = theyThem
elif pronounSet == "Other":
    print("Awesome! You're valid.")
    while acceptedPronouns != "Y":
        otherPronounsOne = input("What should others use to refer to you? ("
                                 "ex: 'he' or 'she') ")
        otherPronouns.append(otherPronounsOne)
        otherPronounsTwo = input("What should others use to refer to you? ("
                                 "ex: 'her' or 'them')")
        otherPronouns.append(otherPronounsTwo)
        otherPronounsThree = input("What should others use to refer to your "
                                   "possessions? (ex: 'their's' or 'his')")
        otherPronouns.append(otherPronounsThree)
        isOrAre = input("Do these pronouns work with is, or are? (ex. 'They "
                        "are' or 'She is')")
        print(otherPronouns)
        acceptedPronouns = input("Are these pronouns correct? (Y/N)")
        otherPronouns.append(isOrAre)
        pronounSet = otherPronouns
elif pronounSet == "Just Use My Name":
    otherPronounsOne = name
    otherPronouns.append(otherPronounsOne)
    spacer1 = ""
    otherPronouns.append(spacer1)
    otherPronounsTwo = name + "'s"
    otherPronouns.append(otherPronounsTwo)
    otherPronounsThree = "is"
    otherPronouns.append(otherPronounsThree)
    pronounSet = otherPronouns

run = "N"
sub_run = "N"
dialogue = "N"
print("From here on out, type everything in UPPER CASE!")
while run != "Y":  # User Controlled Start
    run = input("Ready to begin, " + name + "? (Y/N))")
    if run == "Y":
        print("You awake to a deafening silence.\n Your 5 o'clock flight "
              "should have landed by now, right?")
        print("(LOOK AROUND CABIN or SLEEP)")
    else:
        print("Alright, how about now?")
t_end = time.monotonic() + 60 * 60  # Timer Set
print(time.monotonic())
print(t_end)
while time.monotonic() < t_end:  # Main Loop Begins
    print(time.monotonic())
    command = input("What are you going to do?")
    if command == "LOOK AROUND CABIN":
        area = "coach"
        print(
            "You peek up over the seat in front of you, apparently missing "
            "the whimsical sound of your fellow "
            "passenger's hacking cough. "
            "\n'They must be in the bathroom', you think. "
            "\nBut wait. Wasn't there someone in the seat next to them? (GET "
            "UP or STAY PUT)")
        command = ""
        sub_run = "Y"
        while sub_run == "Y":
            command = input("What are you going to do?")
            if command == "STAY PUT":
                area = "seat"
                print("You're right, you're probably just imagining things. "
                      "And I mean, just look what you have all "
                      "around you. "
                      "\nThe assistance BUTTON, your in-flight MAGAZINE and "
                      "your SAFETY MANUAL, you're all set in your seat! "
                      "Speaking of the button, you feel a little parched "
                      "don't you?")
                button = "Y"
                while button != "N":
                    button = input("Would you like to press the button? (Y/N)")
                    if button == "Y":
                        print("DING DONG. Hm, no help in sight. They "
                              "probably just didn't hear it.")
                    else:
                        command = input("Well, that button was a sure hoot "
                                        "wasn't it? "
                                        "I hope you got to give it a real "
                                        "whirl. "
                                        "\n Well, looks like no one is "
                                        "coming. Should you GET UP or GO BACK "
                                        "TO SLEEP?")
                        if command == "GET UP":
                            area = "coach"
                            print("Well, you needed to use the BATHROOM"
                                  "anyway."
                                  "\n'Maybe that's where they are' you think "
                                  "to  yourself. "
                                  "\n Hm, apparently not. There is no one "
                                  "here, or anywhere in Coach as far as you"
                                  " can see.")
                sub_run = "N"
            elif command == "GET UP":
                print("There is no way you are imagining things. Worst case, "
                      "you can use the BATHROOM. "
                      "\n'Maybe that's where they are' you think to yourself. "
                      "\n Hm, apparently not. There is no one here, "
                      "or anywhere in Coach as far as you can see.")
                sub_run = "N"
            else:
                command = ""
                print("You cannot do that right now.")
    elif command == "GO BATHROOM" and "Holly" not in party:
        area = "bathroom"
        print("You've had too many drinks to think about anything but sweet "
              "release. "
              "\nYou move to the back of Coach, still unnerved by the "
              "absence of your fellow passengers "
              "(at least I hope you are)."
              "\n Hm. Occupied. Figures that would happen the exact time you "
              "need to go. "
              "\n You hear crying from the other side of the door. Should "
              "you KNOCK or SPEAK?")
        command = ""
        sub_run = "Y"
        while sub_run == "Y":
            command = input("What are you going to do?")
            if command == "KNOCK" and knockCount <= 5:
                print("'Please go away', you hear in between sobs from "
                      "behind the thin plastic door.")
                knockCount += 1
            elif command == "SPEAK":
                dialogue = "Y"
                while dialogue == "Y":
                    speech = input("It's usually rude to speak to strangers "
                                   "while they are in the bathroom, but go on "
                                   "ahead \n 'Who are you?', you hear in a "
                                   "meek and muffled voice.(ANSWER HONESTLY "
                                   "OR LIE)")
                    if speech == "ANSWER HONESTLY":
                        print("'A passenger? But you all...', the voice "
                              "trails off. "
                              "\nThe door unlocks and out comes a "
                              "stewardess. The marks of dried tears run down "
                              "her cheeks. "
                              "\n 'Come with me and let's find out what's "
                              "going on here. "
                              "\n You aren't going to get to use the "
                              "bathroom, are you?")
                        holly = NPCs.NPC("Holly", "shaken", 60)
                        party.append("Holly")
                        holly.mood = "Emboldened"
                        holly.opinion = 85 - knockCount * 2
                        dialogue = "N"
                    if speech == "LIE":
                        print("Ah, wow, a brilliant and morally correct "
                              "move. You stammer for a lie. 'I'm the "
                              "captain', you say, putting on your best "
                              "impression of a pilot")
                        print("'You don't really sound like the captain.'")
                        lieSuccess = random.randint(0, 100)
                        speech = input("Uh oh, doesn't sound convinced. ("
                                       "COME CLEAN or LIE MORE)")
                        if speech == "COME CLEAN":
                            print("You can't keep doing this. You answer "
                                  "honestly about your lack of flying ability "
                                  "\n All you hear now is breathing."
                                  "\n..."
                                  "\n A deep sigh is heard as the door "
                                  "unlocks. Before you stands a stewardess, "
                                  "the marks of dried tears running down her "
                                  "cheeks. "
                                  "\n'Come on now, let's sort this all out'."
                                  "\n You aren't gonna be able to go, are "
                                  "you?")
                            holly = NPCs.NPC("Holly", "shaken", 60)
                            party.append("Holly")
                            holly.mood = "Exhausted"
                            holly.opinion = 48 - knockCount
                            dialogue = "N"
                        if speech == "LIE MORE" and lieSuccess < 90:
                            print("You try your best to mimic Top Gun, "
                                  "telling the story of your best friend "
                                  "Goose and an incredibly long volleyball "
                                  "montage, you're just getting to the climax-"
                                  "\n 'Please just stop!', a muffled cry "
                                  "from behind the door. It unlocks, "
                                  "revealing "
                                  "a tired and incredibly annoyed stewardess. "
                                  "\n 'Just come along with me, if you are "
                                  "here then *someone* else must be here. ")
                            holly = NPCs.NPC("Holly", "shaken", 60)
                            party.append("Holly")
                            holly.mood = "P.O."
                            holly.opinion = 30 - knockCount
                            dialogue = "N"
                        if speech == "LIE MORE" and lieSuccess >= 90:
                            pilotPath = "Y"
                            print("You really truly insist that you are the "
                                  "pilot, mentioning times of bravery and "
                                  "aviation excellence. You take hold of "
                                  "your role and you truly become the pilot")
                            print("The door opens, a woman dressed in a "
                                  "steward outfit looks at you. "
                                  "\n 'Why aren't you wearing your "
                                  "uniform?', she looks incredibly puzzled. "
                                  "You, being the excellent liar you are, "
                                  "say you just sort of woke up like this.")
                            print(" 'Is the co-pilot here?' ")
                            print("Her name tag reads Holly. She follows you "
                                  "as you head back to COACH")
                            holly = NPCs.NPC("Holly", "shaken", 60)
                            party.append("Holly")
                            holly.mood = "Relieved"
                            holly.opinion = 75 - knockCount
                            dialogue = "N"
                sub_run = "N"
            if command == "KNOCK" and knockCount >= 5:
                print("The door slams open. You catch the brief glimpse of "
                      "a stewardess. You drop to the ground as "
                      "she screams 'BEGONE, DEMON!'. The last thing you "
                      "remember is the smell of stale peanuts. ")
                t_end = time.monotonic()
                sub_run = "N"
            area = "coach"
    elif command == "GO FIRST CLASS":
        area = "first class"
        print("Snowpiercer who? You say goodbye to bourgeois class "
              "delineations and push towards the land of "
              "in-flight lobsters and leg room."
              "\nWait, this place is a mess! Piles of empty bottles and"
              " half-eaten meals cover the floor; alongside things that make "
              "you hesitate to step without care.")
    elif command == "GO BATHROOM" and "Holly" in party:
        area = "bathroom"
        print("Ah, just like old times. You reminisce on your meeting with "
              "Holly. I hope for your sake she's okay right now")
    elif command == "LOOK AROUND":
        if area == "seat":
            command = input("Same as how you left it when you zonked out. T"
                            "he SAFETY MANUAL and the In-Flight MAGAZINE"
                            " sit in the pouch in front of you. The call "
                            "assistance button lies above your head. "
                            "\nPress it? (Y/N)")
        if area == "coach":
            print("Behind you sits the BATHROOM. Looking around you see "
                  "nothing but empty seats. Above those seats "
                  "lie the OVERHEAD compartments. "
                  "\nTowards the front of the rows there is a curtain "
                  "dividing COACH and FIRST CLASS. You can guess which side "
                  "you are on, based on your former "
                  "'proximity' to your fellow passengers.")
        if area == "bathroom":
            print("A lovely place for lovely people. Ever wonder how for a "
                  "lot of locations on the Earth, "
                  "this would be the closest bathroom?"
                  "\n The MIRROR sits on the wall, giving you a perfect view "
                  "of yourself as you would use the TOILET")
        if area == "first class" and "Louis" not in party:
            if "Holly" in party:
                print("Holly looks incredibly disgusted, 'Everyone suddenly"
                      "disappears on a plane with no"
                      "explanation and people lose their minds.' ")
            print("Treading very lightly, you attempt to ignore a worrying"
                  "stench. Finally, you find the culprit. "
                  "\nCrawled up alongside a bottle of scotch, a well-dressed "
                  "old man is asleep in the front of the cabin.")
            command = input("Wake him?(Y/N)")
            if command == "Y":
                dialogue = "Y"
                while dialogue == "Y":
                    speech = input("RESPECTFUL or DISRESPECTFUL?")
                    party.append("Louis")
                    if speech == "RESPECTFUL":
                        louis = NPCs.NPC("Louis", "Relieved", 75)
                        print("You gently nod him awake. It takes him a moment"
                              " to stop grunting and pushing you away, but it "
                              "seems as though he is now lucid."
                              "\n'Oh my god, there are others!', he exclaims."
                              "\nHe pulls you in close, the stench of liquor "
                              "pungent."
                              "\n'My name is Louis', he slurs out."
                              "\nWell, it seems Louis is here to stay.")
                        dialogue = "N"
                    elif speech == "DISRESPECTFUL":
                        print("Yeah, this dude doesn't deserve anything else "
                              "but a rude awakening! You shake him awake "
                              "shouting your favorite expletives.")
                        void = input("Feel free to input your favorite "
                                     "expletives here:")
                        print("'How dare you call me " + void + "? Did your "
                              "parents not teach you to be a proper human?', "
                              "the old man questions.")
                        if pilotPath == "Y":
                            louis = NPCs.NPC("Louis", "Proud", 95)
                            print("You were panicked to find some kind of"
                                  "response, but Holly comes to your aid."
                                  "\n'Excuse me, " + pronounSet[0] + " " +
                                  pronounSet[3] + " the pilot, you cretin!"
                                  "', shouting down the"
                                  " boomer."
                                  "\nOh yes, you're the captain aren't you?"
                                  "\nThe man looks resigned and says 'Oh, "
                                  "I am so sorry! I deeply apologize.' He"
                                  " gives you an attempt at a salute."
                                  "\nLouis has joined your party. Or at least"
                                  " he won't stop following you now.")
                            dialogue = "N"
                        else:
                            speech = input("Uh oh, he looks pretty mad. "
                                           "Better talk your way out of this "
                                           "one. (APOLOGIZE or DOUBLE DOWN)")
                            if speech == "APOLOGIZE":
                                apology = random.randint(0, 100)
                                print("Yes, the time to grovel is now if any."
                                      " You speak quietly, asking for "
                                      "forgiveness for your transgression,"
                                      " being sure to throw in some 'Sirs'"
                                      " for good measure.")
                                if apology >= 65:
                                    louis = NPCs.NPC("Louis", "Appeased", 75)
                                    print("He takes a moment."
                                          "\n 'Hm, alright. I suppose these"
                                          " are stressful times. It is nice"
                                          "to see other people are still here"
                                          ". Mind if I tag along?' "
                                          "\nYou feel too embarrassed to say "
                                          "no."
                                          "\nLouis is now following you.")
                                    dialogue = "N"
                                else:
                                    louis = NPCs.NPC("Louis", "P.O", 30)
                                    print("Uh oh. He lays a hand on your "
                                          "shoulder"
                                          "\n'Let's see if there is an air "
                                          "marshall around here'."
                                          "\n Louis is now following you, "
                                          "keeping a very close eye.")
                                    dialogue = "N"
                            if speech == "DOUBLE DOWN":
                                print("Yeah you know what? This guy deserved"
                                      "that! You assure him you meant every "
                                      "word. Right down to the letter."
                                      "\nHe lunges for you!"
                                      "\nYou dodge swiftly. He falls to the "
                                      "ground, deciding to stay there after."
                                      "\nThose tiny bottles add up.")
                                dialogue = "N"
                    else:
                        print("Well some choice needs to be made.")
    elif command == "COLLECT MAGAZINE":
        collect("MAGAZINE")
        print("The finest deals available at 30,000 feet!")
    elif command == "COLLECT MANUAL":
        collect("MANUAL")
        safetyInfo = "Y"
        print("Better safe than sorry!")
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
        print("You cannot do that right now. (Hint: Responses need to be in"
              "UPPER CASE)")
game_over()
