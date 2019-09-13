# Carrie West
# A Choose-Your-Own-Adventure Game
import threading
import Main
from Commands import gameover

inventory=[]
name=input("Hello! Before we start, what is your name?")
# Getting the user's pronouns for usage in in-game dialogue/descriptions
heHim=["he", "him", "his"]
sheHer=["she", "her", "her's"]
theyThem=["they", "them', their's"]
otherPronouns=[]
acceptedPronouns="N"
pronounSet=input("What pronouns do you use? (He,She,They,Other)")
if pronounSet == "He":
    pronounSet = heHim
elif pronounSet == "She":
    pronounSet = sheHer
elif pronounSet == "They":
    pronounSet = theyThem
elif pronounSet == "Other":
    print("Awesome! You're valid.")
    while acceptedPronouns != "Y":
        otherPronounsOne=input("What should others use to refer to you? (ex: 'he' or 'she') ")
        otherPronouns.append(otherPronounsOne)
        otherPronounsTwo = input("What should others use to refer to you? (ex: 'her' or 'them')")
        otherPronouns.append(otherPronounsTwo)
        otherPronounsThree = input("What should others use to refer to your possessions? (ex: 'their's' or 'his')")
        otherPronouns.append(otherPronounsThree)
        print(otherPronouns)
        acceptedPronouns=input("Are these pronouns correct? (Y/N)")
        pronounSet=otherPronouns

t = threading.Timer(3600.0, gameover)
run=input("Ready to begin, " + name + "? (Y/N))")
if run == "Y":
    t.start()
    collect("book")
    print(inventory)

