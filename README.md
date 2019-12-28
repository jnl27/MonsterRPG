# MonsterRPG

My first major coding project, completed in AP Computer Science Principles in Spring 2017

MonsterRPG is a text-based turn-based Role Playing Game (RPG), inspired by the battle system in Pokemon. The player begins with a set amount of HP as well as a base attack damage range that can both be upgraded throughout the course of the game. The aim of the game is to successfully advance through 10 fights against monsters of increasing difficulty.

The player also can carry items such as potions and bombs to use during battle. 

###Disclaimer

This game only simulates the battle mechanics of games like Pokemon, Final Fantasy, etc. The mechanics are very simplified to make this first coding project easier.

##Battle Mechanics

###Player's turn

On the player's turn, they will be prompted to type a battle command: "attack", "items", or "run"

**Attack**: Swings the player's sword and uses a random number generator to deal damage to the enemy based on the type of sword equipped
**Items**: Pulls out a menu of possible item selections that the player can then use in combat
**Run**: Quits the game

Upon successful completion of a battle command, it will then be the enemy's turn

###Enemy's turn

On the Enemy's turn, the enemy simply uses their standard attack to deal damage to the player based on a random number generator with range specified in the enemy's description

###Defeating an Enemy

Once the player successfully defeats an enemy by reducing their HP to 0, they will be awarded with an amount of gold based on the range specified for that specific enemy

##After battle & Item Shop

After certain battles, the player will be asked if they would like to shop for items or heal themselves using the gold they've earned from battles. These items can then be purchased and subsequently used in combat to assist the player.
In addition, the player may choose to upgrade their armor (increasing their max HP) or upgrade their sword (increasing their attack damage) in the shop.
