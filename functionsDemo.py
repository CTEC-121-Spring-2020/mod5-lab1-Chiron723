"""
CTEC 121
<Stephen Guild>
<Mod 5 Lab 1>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    print("happy birthday to you!")
    print("happy birthday to you!")
    print("Happy birthday, dear Fred...")
    print("happy birthday to you!")
    print()

""" IPO template
Input(s): none
Process: prints/outputs chorus of happy birthday song
Output: prints to terminal screen
"""

def happy():
    print("Happy birthday to you!")

def main2():
    print()
    happy()
    happy()
    print("Happy birthday, dear Fred...")
    happy()
    print()

#generalize for any person
""" IPO template
Input(s): a name
Process: prints/outputs chorus of happy birthday song
Output: prints to terminal screen
"""
def happyBDay(name):
    print("Happy birthday, dear", name, "...", sep="")

def main3():
    print()
    happy()
    happy()
    happyBDay("Yoshi")
    happy()
    print()

#combine song into function
""" IPO singHappy Birthday
Input(s): a name
Process: prints/outputs happy birthday song
Output: prints to terminal screen
"""

def singHappyBDay(name):
    print()
    happy()
    happy()
    happyBDay(name)
    happy()
    print()

def main4():
    print()
    singHappyBDay("Fred")
    singHappyBDay("Lucy")
    singHappyBDay("Bill")

main4()    