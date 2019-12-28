import random
import time
import os 
print("Welcome to MonsterFightRPG! A game where you randomly fight monsters to earn gold and glory. Have fun!")
print()
#playerStats
playerHP = 50
sword = "Wooden Sword"
armor = "Wooden Armor"
#items & misc
potions = 3
superpotions = 0
bombs = 0
playergold = 0
#keeps track of fight #
fightcount = 0

boughtironarmor = False
boughtsteelsword = False
boughtplatarmor = False
boughtdiamondsword = False

def fight(enemy, enemyHP, mindmg, maxdmg):
    global playerHP, potions, superpotions, playerdmg, playergold, bombs, sword
    while playerHP>0 and enemyHP>0:
        print()
        print("You have ", playerHP, "HP left.")
        fighttypo = True
        while fighttypo == True:
            action = input("What do you do? [attack, items, run]")
            #ATTACK
            if action.lower() == "attack":
                print("You swing your sword at the", enemy)
                time.sleep(1)
                if sword == "Wooden Sword":
                    playerdmg = random.randrange(1,10)
                elif sword == "Steel Sword":
                    playerdmg = random.randrange(7,15)
                elif sword == "Diamond Sword":
                    playerdmg = random.randrange(10,30)
                enemyHP-=playerdmg
                print("Your swing did ", playerdmg, "damage!")
                if enemyHP>0:
                    print("Enemy", enemy, "has", enemyHP, "HP left!")
                fighttypo = False
            #ITEMS
            elif action.lower() == "items":
                print("Type item EXACTLY as shown")
                print("You have:\n\t", potions, "Potions\n\t", superpotions, "Super Potions\n\t", bombs, "Bombs")
                use = input("Which item to use?")
                if use.lower() == "potions" or use.lower() == "potion":
                    if potions>0:
                        print("You used a potion!")
                        potions-=1
                        time.sleep(1)
                        print("You healed yourself for 30HP")
                        playerHP+=30
                        if armor == "Wooden Armor":
                            if playerHP>50:
                                playerHP = 50
                        elif armor == "Iron Armor":
                            if playerHP>100:
                                playerHP = 100
                        print("Your HP is now ", playerHP)
                        print("You have", potions, "potion(s) left.")
                    else:
                        print("You have no more potions")
                elif use.lower() == "super potions" or use.lower() == "super potion":
                    if superpotions>0:
                        print("You used a Super Potion!")
                        superpotions-=1
                        time.sleep(1)
                        print("You healed yourself for 60HP")
                        playerHP+=60
                        if armor == "Wooden Armor":
                            if playerHP>50:
                                playerHP = 50
                        elif armor == "Iron Armor":
                            if playerHP>100:
                                playerHP = 100
                        print("Your HP is now", playerHP)
                        print("You have", superpotions, "Super Potion(s) left.")
                    else:
                        print("You have no more Super Potions")
                elif use.lower() == "bombs" or use.lower() == "bomb":
                    if bombs>0:
                        print("You used a bomb against the", enemy)
                        bombs-=1
                        time.sleep(1)
                        print("BOOM")
                        time.sleep(1)
                        print("The bomb did 20 damage!")
                        enemyHP-=20
                        if enemyHP>0:
                            print("Enemy", enemy, "has", enemyHP, "HP left!")
                        print("You have", bombs, "bomb(s) left.")
                    else:
                        print("You have no more bombs")
                else:
                    print("Unrecognized item.")
                fighttypo = False
            #RUN   
            elif action.lower() == "run":
                print("You have fled from battle.")
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                os._exit(0) 
            else:
                print("Incorrect option.")
            
        if enemyHP<=0:
            print("You have killed the", enemy, "!")
        print()
        if enemyHP>0:
            print("Enemy", enemy, "attacks!")
            time.sleep(1)
            enemydmg = random.randrange(mindmg, maxdmg)
            playerHP-=enemydmg
            print("Ouch! Enemy", enemy, "did", enemydmg, "damage!")
        if playerHP<=0:
            print("You have been killed by the", enemy, ".")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            os._exit(0)

def itemshop():
    global yesshop
    global playergold
    global playerHP
    global playerdmg
    global potions
    global superpotions
    global bombs
    global sword
    global armor
    global fightcount
    global boughtironarmor
    global boughtsteelsword
    global boughtplatarmor
    global boughtdiamondsword
    while yesshop != -1:
        print("What would you like to buy? (Type the item EXACTLY as shown to buy the item)")
        print("\n\tpotions (Restores 30 health) - 15 gold each")
        print("\n\tbombs (One-time use, instantly deals 20 dmg) - 10 gold each")
        if fightcount>=5:
            print("\n\tSuper Potions (Restores 60 health) - 35 gold each")
        if boughtsteelsword!=True:
            print("\n\tUpgrade to Steel Sword (Increases damage to 5-15dmg) - 70 gold")
        if boughtironarmor!=True:
            print("\n\tUpgrade to Iron Armor (Increases HP to 100) - 100 gold")
        if fightcount>=8:
            if boughtdiamondsword!=True:
                print("\n\tUpgrade to Diamond Sword (Increases damage to 10-30dmg) - 150 gold")
            if boughtplatarmor!=True:
                print("\n\tUpgrade to Platinum Armor (Increases HP to 200) - 225 gold")
        shopping = input("Type here: ")
        #POTIONS
        if shopping.lower() == "potions":
            potionnum = int(input("How many potions would you like to buy?(Type the number, not word)"))
            if playergold>=15*potionnum:            
                print("You have bought", potionnum, "potions")
                potions+=potionnum
                playergold-=potionnum*15
                print("You now have", potions, "potions.")
            else:
                print("You do not have enough gold for that")
        elif shopping.lower() == "super potions":
            if fightcount>=5:
                spotionnum = int(input("How many Super Potions would you like to buy? (Type the number, not word)"))
                if playergold>=35*spotionnum:
                    print("You have bought", spotionnum, "Super Potions.")
                    superpotions+=spotionnum
                    playergold-=spotionnum*35
                    print("You now have", superpotions, "Super Potions.")
                else:
                    print("You do not have enough gold for that")
            else:
                print("Invalid item.")
        #BOMBS
        elif shopping.lower() == "bombs":
            print("You can only have a maximum of 3 bombs in hand!")
            bombnum = int(input("How many bombs would you like to buy?(Type the number, not word)"))
            if playergold>=10*bombnum:
                if bombs+bombnum>3:
                    print("Too many! You can only hold 3 bombs!")
                else:
                    print("You have bought", bombnum, "bombs")
                    bombs+=bombnum
                    playergold-=bombnum*10
                    print("You now have", bombs, "bombs")
            else:
                print("You do not have enough gold for that")
        #STEEL SWORD
        elif shopping.lower() == "upgrade to steel sword":
            if playergold>=70:
                print("You have upgraded your weapon to Steel Sword!")
                print("Your sword now deals 5-15 damage!")
                sword = "Steel Sword"
                boughtsteelsword = True
                playergold-=70
            else:
                print("You do not have enough gold for that")    
        #IRON ARMOR
        elif shopping.lower() == "upgrade to iron armor":
            if playergold>=100:
                print("You have upgraded to Iron Armor!")
                print("Your HP is now 100!")
                armor = "Iron Armor"
                boughtironarmor = True
                playerHP = 100
                playergold-=100
            else:
                print("You do not have enough gold for that")
        #DIAMOND SWORD
        elif shopping.lower() == "upgrade to diamond sword":
            if playergold>=150:
                print("You have upgraded your weapon to Diamond Sword!")
                print("Your sword now deals 10-30 damage!")
                sword = "Diamond Sword"
                boughtdiamondsword = True
                playergold-=150
            else:
                print("You do not have enough gold for that")
        #PLATINUM ARMOR
        elif shopping.lower() == "upgrade to platinum armor":
            if playergold>225:
                print("You have upgraded to Platinum Armor!")
                print("Your HP is now 200!")
                armor = "Plat Armor"
                boughtplatarmor = True
                playerHP = 200
                playergold-=225
            else:
                print("You do not have enough gold for that")
        else:
            print("Invalid item.")
        print()
        print("You have", playergold, "gold left.")
        shop = input("Would you like to buy more items?[y/n]")
        if shop.lower() == "n" or shop.lower() == "no":
            yesshop = -1


def healer():
    global playergold
    global playerHP
    global armor
    print("You have", playergold, "gold")
    error = True
    while error!=False:
        heal = input("Would you like to fully restore your health for 30 gold?[y/n]")
        if heal.lower() == "y" or heal.lower() == "yes":
            print("You have paid 30 gold to restore your health.")
            time.sleep(1)
            playergold-=30
            if armor == "Wooden Armor":
                playerHP = 50
            elif armor == "Iron Armor":
                playerHP = 100
            elif armor == "Plat Armor":
                playerHP = 200
            print("Your HP is now", playerHP)
            print("You have", playergold, "gold left.")
            error = False
        elif heal.lower() == "n" or heal.lower() == "no":
            print("You have decided not to restore your health.")
            error = False
        else:
            print("Invalid Option.")
        
def afterbattle():
    global gold
    global playergold
    time.sleep(1)
    print("You have earned", gold, "gold!")
    playergold+=gold
    time.sleep(1)
    print("You have", playergold, "gold")
    print("You have", playerHP, "HP left.")
    print()

def afterbattle2():
    afterbattle()
    healer()
    
def afterbattleshop():
    global yesshop
    afterbattle()
    healer()
    print()
    print("The travelling merchant Reggi has appeared!")
    shop = input("Would you like to buy some items?[y/n]")
    if shop.lower() == "y" or shop.lower() == "yes":
        yesshop = 0
    elif shop.lower() == "n" or shop.lower() == "no":
        yesshop = -1
    itemshop()

def roundbegin():
    global fightcount
    fightcount+=1
    print()
    print("~~~~~~~~~~~ FIGHT", fightcount, "~~~~~~~~~~~")
    print()
    

typo = True
while typo == True:
    begin = input("Are you ready to begin the fight? [y/n]" )
    if begin.lower() == "y" or begin.lower() == "yes":
        start = True
        typo = False
        while start!=False:
            global name
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~GAME START~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("You are an adventurer seeking to destroy all enemies you encounter. You have 50HP and deal 1-10 damage. Good luck!")
            time.sleep(2)
            name = input("What shall your name be? ")
            print("Welcome adventurer", name)
            time.sleep(1)
            print("Protip: The game is over once you defeat all monsters or die.")
            print("Protip: Running away will quit your adventure.")
            print("Protip: Item: potion will heal you for 30HP.")
            #fight1
            roundbegin()
            print("A wild mini goblin has appeared! It has 10HP and deals 3-6 damage. It will drop 20-50 gold when defeated.")
            gold = random.randrange(20,50)
            fight("Goblin", 10, 3, 6)
            afterbattle()
            print()
            print("Protip: Starting from after fight 2, if you're low on HP, you can pay the healer for 30 gold to fully restore your HP.")
            #fight2
            roundbegin()
            print("A wicked troll has appeared! It has 15HP and deals 5-8 damage. It will drop 40-60 gold when defeated.")
            gold = random.randrange(40,60)
            fight("Troll", 15, 5, 8)
            afterbattle2()
            #fight3
            roundbegin()
            print("A gang of goblins has appeared! They have 25HP and deal 2-10 damage. They will drop 20-50 gold when defeated.")
            gold = random.randrange(20,50)
            fight("Goblin Gang", 25, 2, 10)
            afterbattleshop()
            #fight4
            roundbegin()
            print("A Masked Ghoul has appeared! It has 30HP and deals 5-12 damage. It will drop 50 gold when defeated.")
            gold = 50
            fight("Masked Ghoul", 30, 5, 12)
            afterbattle2()
            print()
            print("Protip: You may not always get a chance to heal or shop after every battle, so spend that gold!")
            time.sleep(1)
            print("Protip: After fight 5, the Super Potion will be available for purchase in the item shop!\n\tThe Super Potion will heal you for 60HP!")
            time.sleep(1)
            #fight5
            roundbegin()
            print("A Shadow Knight has appeared! It has 45HP and deals 10-20 damage! It will drop 70-100 gold when defeated.")
            time.sleep(1)
            print()
            print("Shadow Knight: 'You have come far enough. This is where you end!'")
            time.sleep(1)
            print()
            print("Protip: WARNING - Shadow Knight is a mini-boss. He is significantly stronger than all the enemies you have faced so far. Be careful!")
            time.sleep(1)
            gold = random.randrange(70,100)
            fight("Shadow Knight", 45, 12, 20)
            afterbattleshop()
            #fight6
            roundbegin()
            print("A Large Goblin has appeared! It has 35HP and deals 7-12 damage. It will drop 30-70 gold when defeated.")
            gold = random.randrange(30,70)
            fight("Large Goblin", 35, 7, 12)
            afterbattle()
            print()
            #fight7
            roundbegin()
            print("A Haunting Banshee has appeared! It has 30HP and deals 10-20 damage! It will drop 50-80 gold when defeated.")
            print("Banshee: 'EEEEEEEEEEEEEEEEEEEEEEE'")
            gold = random.randrange(50,80)
            fight("Haunting Banshee", 30, 10, 20)
            afterbattleshop()
            print()
            print("Protip: After fight 8, you can upgrade your equipment even further!")
            #fight8
            roundbegin()
            print("A Sturdy Golem has appeared! It has 70HP and deals 3-15 damage! It will drop 100-150 gold when defeated.")
            print("Golem: '...'")
            gold = random.randrange(100,150)
            fight("Sturdy Golem", 70, 3, 15)
            afterbattleshop()
            #fight9
            roundbegin()
            print("A Two-Headed Hydra has appeared! It has 60HP and deals 12-20 damage! It will drop 80-130 gold when defeated.")
            gold = random.randrange(80,130)
            fight("Two-Headed Hydra", 60, 12, 20)
            print()
            print("Protip: This is your LAST chance to shop/heal, make sure you're ready for the next fight!")
            afterbattleshop()
            #fight10
            print("Protip: This is the final battle. Get ready!")
            print()
            roundbegin()
            print("The Mighty Dragon has appeared! It has a whopping 100HP and deals 20-40 damage! It will drop 500 gold when defeated.")
            print()
            time.sleep(2)
            print("Dragon: 'NYYYYYYYYEEEEEEeEEEEEeeEEeEEEEEEAAAAAHHHHHHHH!!!'")
            print()
            time.sleep(2)
            print("Dragon: 'So you have made it this far, yea? You came here to steal my gold, yea? You and your stupid adventurers, I hate all of you! PREPARE TO MEET YOUR DOOM!")
            print()
            time.sleep(2)
            print("Protip: EXTREME WARNING - The Dragon is the FINAL-BOSS. It is the strongest monster you have yet to conquer. It is incredibly strong. Exercise EXTREME Caution!")
            time.sleep(2)
            gold = 500
            fight("Lord Dragon", 100, 20, 40)
            print()
            time.sleep(2)
            print("Dragon: '. . .'")
            print()
            time.sleep(2)
            print("Dragon: 'You have beaten me this time, foolish human.'")
            print()
            time.sleep(2)
            print("Dragon: 'Nggh, I guess I must forfeit my treasure thus far.'")
            print()
            time.sleep(2)
            print("Dragon: 'Do NOT think you've have defeated me. This was just but a battle. I WILL win next time, you hear?'")
            print()
            time.sleep(2)
            print("Dragon: 'Until then. Farewell.'")
            print()
            time.sleep(2)
            print("Dragon: 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'")
            print()
            time.sleep(2)
            print("The mysterious dragon teleported away.")
            afterbattle()
            time.sleep(2)
            print("AND so, the brave adventurer known as", name, "has finally defeated the Mighty Dragon, securing themselves the title of Greatest Adventurer in the Land.")
            time.sleep(2)
            print()
            print("~~~~~~~~~~~~~~~CONGRATULATIONS! YOU HAVE BEAT THE GAME!~~~~~~~~~~~~~~~")
            print("                      Thanks for playing!")
            print()
            print()
            start = False


    elif begin.lower() == "n" or begin.lower() == "no":
        print("You have decided that you are not ready to fight. Come back later!")
        typo = False
    else:
        print("Invalid selection, try again")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
       
