def init():
    choice = int(input("Welcome to Madlibs! Choose a madlib type: 1. Kindness \n"))
    if (choice == 1):
        kindness()
    else:
        print("Invalid choice")
    

def input_friendName():
    global friendName
    friendName = input("Enter a name of a friend \n")

def input_yourName():
    global yourName
    yourName = input("Enter your name \n")

def input_presentVerb_1():
    global presentVerb_1
    presentVerb_1 = input("Enter a verb in present tense \n")

def input_presentVerb_2():
    global presentVerb_2
    presentVerb_2 = input("Enter another verb in present tense \n")
    
def input_presentVerb_3():
    global presentVerb_3
    presentVerb_3 = input("Enter yet another verb in present tense \n")

def input_contVerb_1():
    global contVerb_1
    contVerb_1 = input("Enter a verb in present continuous (it's a verb ending in -ing. \n For example, walking.) \n")
    
def input_contVerb_2():
    global contVerb_2
    contVerb_2 = input("Enter another continuous verb in present tense \n")

def input_contVerb_3():
    global contVerb_3
    contVerb_3 = input("Enter yet another continuous verb in present tense \n")    
    
def input_noun_1():
    global noun_1
    noun_1 = input("Enter a singular noun \n")

def input_noun_2():
    global noun_2
    noun_2 = input("Enter another singular noun \n")

def input_pluNoun_1():
    global pluNoun_1
    pluNoun_1 = input("Enter a plural noun \n")

def input_pluNoun_2():
    global pluNoun_2
    pluNoun_2 = input("Enter another plural noun \n")

def input_adverb():
    global adverb
    adverb = input("Enter an adverb \n")

def kindness():
    input_yourName()
    input_friendName()
    input_presentVerb_1()
    input_presentVerb_2()
    input_presentVerb_3()
    input_pluNoun_1()
    input_pluNoun_2()
    input_contVerb_1()
    input_adverb()

    print("Dear %s" % friendName)
    print("On World Kindness Day, I’m here with a friendly reminder of just")
    print("how much you %s my world. In my eyes, you’re better" % presentVerb_1)
    print("than %s and %s combined.  I can't wait until" % (pluNoun_1,pluNoun_2))
    print("the next time we get to %s together.  You have a knack" % presentVerb_2)
    print("for %s and nobody knows how to %s quite" % (contVerb_1,presentVerb_3))
    print("like you.  But most importantly, Mother Earth is happier with")
    print("you in her world.  Keep doing you!")
    print("Yours %s," % adverb)
    print(yourName)
    init()

init()



