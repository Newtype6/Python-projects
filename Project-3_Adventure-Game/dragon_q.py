# Project 3

print('''
            <>=======()
           (/\___   /|\\          ()==========<>_
                 \_/ | \\        //|\   ______/ \)
                   \_|  \\      // | \_/
                     \|\/|\_   //  /\/
                      (oo)\ \_//  /
                     //_/\_\/ /  |
                    @@/  |=\  \  |
                         \_=\_ \ |
                           \==\ \|\_
                        __(\===\(  )\
                       (((~) __(_/   |
                            (((~) \  /
                            ______/ /
                            '------'
''')
print("Welcome to Krindar Island.")
print("A dragon has made its home near your small, sleepy village.\nIt has been taking children and eating them.\nYou weren't too bothered when Timmy went,\nhe always used to drop your sandals in the well.\nBut now it has taken your daughter, Alice.\nYou must brave the dragon's lair and save your child.")

weapon = input("You pick up a stout shield for your left hand, which weapon do you choose for your right?  Type 'spear' or 'axe'\n").lower()

if weapon == "axe":
    print("The axe is heavy in your hand, a good weight, and newly sharpened.")
    entrance = input("You have reached the mountain where the dragon resides.\nThere are two entrances - a grand stone door set deep into the rock, and a path leading upwards to a cave.\nWhich way do you go?  Type 'door' or 'path'\n").lower()
    if entrance == "path":
        print("You follow the path up and through the cave, emerging in the shadows to the side of the dragon.")
        plan = input("The dragon is sleeping.  Alice is pinned under a leathery wing.\nWhat is your plan, Hero?\nDo you try to rescue Alice without waking the dragon, and sneak away?\nDo you take your axe to the dragon's head?\nOr, do you attack the wing with your axe?\nType 'sneak', 'head' or 'wing'\n").lower()
        if plan == "head":
            print("Your axe cleaves through the head of the dragon, its body thrashing wildly.\nYou grab Alice and run back to the village, to a Hero's welcome!\nYOU WIN!!!")
        elif plan == "wing":
            print("Your axe rends the wing like paper.  Alas, it does little but enrage the dragon.  You are food now.\nGame Over.")
        elif plan == "sneak":
            print("You are not built for stealth, more a brawler than a theif.  You trip and stumble, waking the dragon and bringing your doom.\nGame Over.")
        else:
            print("You are frozen in fear.  Too many bones.  Too much death.  You curl up and shudder, helpless.\nGame Over.")
    elif entrance == "door":
        print("The heavy door gives grudgingly and with great noise.\nThe dragon awakes, you become toast.\nGame Over.")
    else:
        print("You have strayed too far from your quest.\nYour time to be a Hero has passed.\nGame Over.")        
elif weapon == "spear":
    print("A spear?  Against a dragon??  The villagers mock your choice of weapon, you hide under the bed and stay there.\nGame Over.")    
else:
    print("You seem to have tried to pick up something which doesn't exist.\nYou have gone mad with grief.\nGame Over.")

print("Thanks for playing!")
