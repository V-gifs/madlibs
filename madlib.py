def init():
    choice = int(input("Welcome to Madlibs! Choose a madlib type: \n 1. Kindness \n 2. Naughty (18+) \n 3. Madlibs are dumb. I want to leave \n"))
    if (choice == 1):
        kindness()
    elif (choice ==2):
        age = int(input("How old are you? \n"))
        if (age < 18):
            print("You are too young for this content.")
            init()
        else:
            naughty()
    elif (choice == 3):
        exit()
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

def input_adjective_1():
    global adjective_1
    adjective_1 = input("Enter an adjective \n")

def input_adjective_2():
    global adjective_2
    adjective_2 = input("Enter another adjective \n")

def input_adjective_3():
    global adjective_3
    adjective_3 = input("Enter yet another adjective \n")

def input_adjective_4():
    global adjective_4
    adjective_4 = input("Yes, another adjective \n")

def input_adjective_5():
    global adjective_5
    adjective_5 = input("Last adjective. Promise \n")

def input_bodypart_1():
    global bodypart_1
    bodypart_1 = input("Enter a body part \n")

def input_bodypart_2():
    global bodypart_2
    bodypart_2 = input("Enter another body part \n")

def input_bodypart_3():
    global bodypart_3
    bodypart_3 = input("Enter yet another body part \n")

def input_petname():
    global petname
    petname = input("Enter a pet name \n")

def input_noise():
    global noise
    noise = input("Enter a noise \n")

def input_location():
    global location
    location = input("Enter a location \n")



    

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

def naughty():
    input_adjective_1()
    input_adjective_2()
    input_adjective_3()
    input_adjective_4()
    input_adjective_5()
    input_contVerb_1()
    input_noun_1()
    input_bodypart_1()
    input_bodypart_2()
    input_bodypart_3()
    input_presentVerb_1()
    input_petname()
    input_noise()
    input_location()
    input_presentVerb_2()
    input_adverb()
    
    print("Turning on a woman can be a %s challenge, similar to %s a(n) %s. " % (adjective_1,contVerb_1,noun_1))
    print("Look right in her %s and %s her! If that seems too %s," % (bodypart_1,presentVerb_1,adjective_2))
    print("there is another way to make your %s %s." % (petname,noise))
    print("It's simple, walk into the %s and %s for her. She will" % (location,presentVerb_2))
    print("%s be able to resist you! There is only one %s" % (adverb,adjective_3))
    print("rule you must not break. Never put your %s into her %s" % (bodypart_2, bodypart_3))
    print("in a %s way. If you follow this guide, you are sure to turn" % adjective_4)
    print("on your %s woman!" % adjective_5)
    init()
init()
    


