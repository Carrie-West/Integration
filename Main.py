#Carrie West
#A Choose-Your-Own-Adventure Game

name=input("Hello! Before we start, what is your name?")
heHim=["he", "him", "his"]
sheHer=["she", "her", "her's"]
theyThem=["they", "them', their's"]
otherPronouns=[]
pronounSet=input("What pronouns do you use? (He,She,They,Other)")
if pronounSet == "he":
elif pronounSet == "She":
elif pronounSet == "They":
elif prnounsSet == "Other":
    otherPronounsOne=input("Valid! What should others use to refer to you? (ex: 'he' or 'she' ")
    otherPronouns.append(otherPronounsOne)
    otherPronounsTwo = input("What should others use to refer to you? (ex: 'her' or 'them')")
    otherPronouns.append(otherPronounsTwo)
    otherPronounsThree = input("What should others use to refer to your possessions? (ex: 'their's' or 'his')")
    otherPronouns.append(otherPronounsThree)
    print(otherPronouns)
    acceptedPronouns=input("Are these pronouns correct? (Y/N)")
    if acceptedPronouns = Y:
        break