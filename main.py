print('''░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█
░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█
░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█
░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌
░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█
▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌ Doge is watching
█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█
█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█
▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌
▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌
█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█''')
input('press Enter to start M-E v1.1 WIP')



import time
import code
#lines describe the game with lore and what the goal is
print('Welcome to M-E, a text based adventure game based on the books by R.R.Tolkin')
time.sleep(2)
print('The goal of the game is to deliver an item of great value')
time.sleep(2)
print('------------------------------------------------------------------------------------')
#legal info if any
print('this script/game was written in Python 3 with help from PyCharm')
print('both are open source programs')
time.sleep(4)
print('M-E the game was created by ModDayHippie under a Free-to-Use licence')
print('that mean you are able to download and use this game for free')
print('but not distribute for profit')
print('-------------------------------------------------------------------------------------------')
time.sleep(4)
print('Lord of the rings, The Hobbit, and the silmarillion were all written by R.R.Tolkin')
print('and owned by the Saul Zaentz Company')
print('the story in the program below was written by ModDayHippie using assets from middle earth')
print('if you have any questions you can message me at kelloggs989@live.com')
print('---------------------------------------------------------------------------------------------')
time.sleep(4)

print('by agreeing to the EULA you agree to not make a copy of the game, or reverse engineer the game')
print('you also agree to not make any profit off the game in any way either streaming or direct sales')
print('you agree that M-E the game is owned by ModDayHippie')
print('you agree that Lord of The Rings, The Hobbit ect are owned by the Saul Zaentz Company')

EULA = input('do you agree to these conditions? (y/n):')
if EULA == 'n':
    print('please have yourself an amazing day. relaunch the .py to restart the program')
    time.sleep(3)
    input(exit())

print('--------------------------------------------------------------------------------------------')



print('''Please make sure your spelling is correct with the promt. i know i cant spell correctly but
if you don't spell them the way i did the program wont work.
at some point ill fix all the spelling mistakes''')
print('only questions with (y/n) have to be answered with y or n')
print('the bard class is more for jokes, crazy random things will happen')
print('--------------------------------------------------------------------------------------------')
time.sleep(4)
print('''The story is set in the 3rd age of middle earth.
Just after the events of the hobbit but before the events of lord of the Rings.
You are a traveling mercenary protecting a traveling merchant.
You stop for the night to rest but you know its not safe''')

print('---------------------------------------------------------------------------------------------')

time.sleep(4)

print('I hope you enjoy the game')
print('------------------------------------------------------------------------------------------')
time.sleep(2)
#this is the caractar creation menu
print('character creation')

name = input('what is your name:')

age = input('what is your age:')

race = input('what race are you human, orc or elf:')

Class = input('what class do you want to be? hero, bard, archer, mage:')

print('---------------------------------------------------------------------')

#these lines are for stat setup for your character
print('You have 10 point to distribute among your 3 stats:')
muc = input('What is your strength stat:')
hlt = input('What is your health stat:')
mag = input('What is your magic stat:')

print('--------------------------------------------------------------')

print('character review')
time.sleep(1)
print('name:' + name)
print('age:' + age)
print('race:' + race)
print('Class:' + Class)
print('------------------------------------------------------------------------------------------')
time.sleep(1)
print('stats')
print('strength:' + muc)
print('health:' + hlt)
print('magic:' + mag)
print('-------------------------------------------------------------------------------------------')
time.sleep(3)

Correct = input('are these stats correct, you will not be able to change after (y/n):')
print('----------------------------------------------------------------------------------------')
if Correct == 'n':
    #make this command restart the program not kill it**
    input(exit())

#this area is a test for a stat check for word stats
#print('this is a basic stat check, only humans can open this door')
#if race == 'human':
    #print('you are a human and can open the door')
#elif race == 'elf':
    #print('you are an elf and cant open this door')
#elif race == 'orc':
    #print('you are an orc and cant open this door')


#this is a stat check test area for numberd stats

#print('this is a numberd stat check, only strength 3+ can enter')
##elif muc <3:
    #print('you did not pass the stat check')

#this is the start of the game
print('''you start of at your camp, you hear a rustle in the nearby bushes.
you wake up the merchant your protecting and tell him to get ready for a fight''')
time.sleep(3)
#your class determins what weapon you draw
if Class == 'hero':
    print('you ready your sword for battle')
elif Class == 'archer':
    print('you ready your bow for battle')
elif Class == 'mage':
    print('you ready your staff')
elif Class == 'bard':
    print('''you ready your harp for battle.....it wont do much so you also grab
    your dagger''')

time.sleep(4)
print('you yell into the night who goes there')
time.sleep(4)
print('from the darkness your hear "SHIT!!! TOLD YOU NOT TO WEAR THE IRON BOOTS"')
time.sleep(4)
print('just shh SSHH...i got this')
time.sleep(4)
print('''you just better surrender all your good, we got 4..i mean 8 guys here
its just better if you surrender''')

time.sleep(4)

print('''you think to yourself "who the fuck are these idiots and what shit hole
from Gondor did they come from''')
time.sleep(3)
#start of first encounter
print('you notice by sound exactly where your foe is, you could get a drop on them')
pounce = input('do you want to jump into the shadows and attack your foe? (y/n):')
print('-------------------------------------------------------------------------------------------')

#many option here depending on your race and users first desicicon that changes the game
if pounce == 'y':
    print('you decide to attack your foe')
    if Class == 'hero':
        print('''You get the jump on your foe giving you huge advantage.
        you easily take the first foe out with a single slash
        and the second is easily finished of in seconds''')
    if Class == 'archer':
        print('''you draw your bow and fire a shot into the dark
        "ahh he got me"
        "your on your own im out of here
        you shoot a second arrow at the sound of the footsteps of the second foe
        "AGGH"
        you draw your dagger and proceed to the darkness and finish them off''')
    if Class == 'bard':
        print('''You decide to lay down a fresh beat from the 2nd era.
        "aha his is going to be to easy"
        the 2 foes walk out to greet you
        "ah, a simple bard. what a horrible choice for for protection in the dark....
        before he could finish his sentence you throw your dagger into the neck of the 1st foe
        "fuck you killed him"
        "your done for now"
        as your foe approaches you yeet your harp directly at his face causing -300 look damage
        "ahh my nose i have no will to live" he then takes his own life''')
    if Class == 'mage':
        print('''you cast AOE fireball attack into the darkness of the bushes
        "AHHHHHHHHGGGG"
        ..........
        ..........
        you go to look behind the bush and there are two charred bodies.''')

#again more option for first encounter
if pounce == 'n':
    print('you decided not to attack your foe and wait')
    if Class == 'hero':
        print('''you draw your sword and stand at the ready
        two figures walk from the bushes
        "aha, so its just the two of you, and one of you has no weapon"
        "i guess well just be taking your stuff and going then"
        "theres no use in trying to fight, your surrounded"
        "its time to die"
        the first foe lunges at you with his axe but you manage to just block it, the second foe
        decided this is a good time to attack and swings at you cutting your arm.
        you swing your sword cutting the leg of foe two
        and then block an incoming attack from foe one
        then quickly spin around to decapitate him
        the first foe say "i give up please don't kill me, i have gold"
        but you decide not to listen and drive your sword though his chest''')
    if Class == 'bard':
        print('''you pull your harp out and lay down a fresh tune from the second era
        "haha about to be killed and he plays music"
        "this is gonna be easy"
        the foe walks towards you sword drawn
        but you quickly drive  your dagger into his neck killing him
        the second foe lunges towards you but you yeet your harp into his face causing -300 charisma
        damage and life long self hate for his looks
        "ahh i cant live like this"
        the foe takes his one life''')
    if Class == 'archer':
        print('''you pull out your bow, and get a arrow ready
        the figures walk out from the bush
        "aha a single elf and a merchant. this should be easy
        the first foe walks towards you and you place an arrow right between the eyes
        "arrg"
        "thats if you stupid elf, you die here"
        the second foe lunges towards you
        you have no time to set another arrow so you grab your dagger
        your foe swings at you but misses, but takes you to the ground
        you lay your dagger into his back multiple times''')
    if Class == 'mage':
        print('''you ready your staff as two figures appear
        "aha just a simple mage to protect this merchant
        tisk tisk, thats not alot"
        the first foe lunges towards you and you cast a fire ball spell
        "ahhhgs it burns, it hurts"
        before you can cast another spell your second foe takes you to the ground
        you are able to push him away and cast and AOE sole capture on him
        "AHAHHA WHAT IS THIS, i cant take it just end me......THE PAIN......THe pai.......''')
print('-----------------------------------------------------------------------------------------------------------')
#end of choses for first encounter start of outto dialog
time.sleep(15)
print('after the struggle you hear a thud from behind')
print('you look over and the merchant has an arrow in his chest')
time.sleep(4)
print('you run over to check on him')
print('-----------------------------------------------------------------------------------------------')
time.sleep(3)
print('in his last breaths the merchant says')
print('listen ' + name + ' im not gonna make it.')
time.sleep(3)
print('take this box, but dont open it')
print('take it to Rivendale')
time.sleep(3)
print('the elf lords will pay you a great amount for it ' + name)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(3)
print('the eyes of the merchant go empty, he has passed')
print('-----------------------------------------------------------------------------------------------------------')
time.sleep(2)
print('you have to get out of here fast, there is clearly another foe nearby....maybe more')
time.sleep(1)

#depending on class the weapon you pick up changes
if Class == 'hero':
    print('you grab your sword, a bit of food laying around and run towards the north')
if Class == 'archer':
    print('you grab your bow, and a bit of food and run towards the north')
if Class == 'bard':
    print('you grab your harp, and a bit of food nearby, before you run off you grab the gold tooth off the merchant')
    print('he wont need it much now...and his shoes')
    print('after 15 minuts of looting you now have his shoes, hat, gold and the deed to his wife')
if Class == 'mage':
    print('you grab your staff, and a bit of food nearby and run to the north')
print('-------------------------------------------------------------------------------------------------------------')
input('press ENTER to Continue')
print('-------------------------------------------------------------------------------------------------')
#filler story
print('after running for what felt like forever, the sun begins to rise')
print('you see a log nearby and decide to catch your breath')
time.sleep(6)
print('you pull out your map and relize your just west of a small down')
print('after what you have been though you think that a bed and a cup of mead will do you good')
time.sleep(6)
print('"well ' + name + ', you really have nothing better to do. i guess we should deliver this box"')
print('"if the elf lords are very rich and if they want this box they could look favortable apon me if i deliver it"')
time.sleep(6)
print('"yea lets do this"')
print('you grab all your belonging and head west to the village to prepare for your trip to rivendale')

print('-------------------------------------------------------------------------------------------------------')
time.sleep(3)

#small town story
print('you get to the edge of the town and are greeted by a poor farmer')
print('"please sir please come here for a moment')
time.sleep(3)

farmer = input('do you want to walk over to the farmer? (y/n):')
print('-----------------------------------------------------------------------------------------')
if farmer == 'y':
    print('you walk over to the farmer')
    print('"oh thank you sir, what is your name')
    time.sleep(3)
    print('you tell the farmer your name')
    time.sleep(3)
    print('please sir ' + name + ', please could i have a single coin')
    print('last night a theif stole my beloved cow, and now i have no way to feed my child')
    time.sleep(3)
    print('i just need a single coin to buy some milk for my child')
    time.sleep(3)
    help_farmer = input('do you want to give the farmer a coin? (y/n):')
    print('---------------------------------------------------------------------------------------------------')
    if help_farmer == 'y':
        print('why thank you. you helped me so much here take this')
        farmer_item = input('the farmer hand you a medalion press "y" to continue:')

    if help_farmer == 'n':
        print('you have dammed me and my family. curse you and your whole bloodline')
        curse = input('you have been given a curse, press "y" to continue:')
if farmer == 'n':
    print('the farmer yells "curse you and your whole bloodline')
    if farmer == 'n':
        curse = input('you have been cursed, press enter "y" to continue:')
print('------------------------------------------------------------------------------------------------------')

#filler story from farmer to town and bar into
print('you continue your way to the nearest pub for a nice cold ale')
print('you you notice a sign with a mug on it, "well there we go" you think to yourself')
time.sleep(5)
print('as you walk in the door you notice its not that busy, so you pull up a seat right at the bar')
print('good day there ' + race +', what can i get you?')
time.sleep(5)
print('"just your strongest ale and maybe some soup if you got some"')
print('"yea the soup of the day is pig snout chowder" says the bartender')
time.sleep(5)
print('"ill pass on the chowder but the ale sounds great"')
print('----------------------------------------------------------------------------------------------------------')
time.sleep(5)
#bar encounter
print('after a few ales you call the bartender over once again')
print('wheres the nearest blacksmith" you say')
time.sleep(5)
print('"ahaa on an adventure are we?"the bar tender says')
print('thats not really any of your bisness"')
time.sleep(5)
print('"now wheres the nearest blacksmith"')
print('"no need to get hostile there freind, other side of town. big place red roof" the bartend says')
time.sleep(5)
print('after another ale you decide its a good time to head out')
print('you gather your belonging and leave')
print('test line for github')
#outtro message at the end of the game, always at bottom of script
print('--------------------------------------------------------------------------------------------------------')
time.sleep(3)
print('thanks for playing M-E v1.1 WIP, more will be released soon')
print('thanks for the support and feedback')
print('ModDayHippie')
input('press ENTER to exit')