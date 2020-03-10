from place import Place
from item import Item, Weapon
from friends import Friend
from enemy import Enemy
from backpack import Backpack
import sys,time,random
import winsound
from clint.textui import colored

kolegium = Place('Kolegium', 'In the middle of your room, your roommate built a castle of empty \
energetic cans. Over your bed on the wall hang posters of Metallica. Your room extremely needs cleaning.\n')
smok = Place('Smoking spot', 'Almost everyday crowded place today looks abandoned.\n')
park1 = Place('Stryiskyi park', 'Big park with old abandoned soviet buildings. \
Favourite place for drunk people and drug addicts.\n')
center = Place('Center', 'Big and crowded. So noisy.', blocked=True)
pub = Place('100 Rentgen', 'Cheap pub. The favourite place of students.\n', blocked=True)
park2 = Place('Ivan Franko Park', 'Small dark park. Under the dim light of the lantern, \
a female figure can be seen.\n', blocked=True)
station = Place('Vokzal', 'Old large train station surrounded by police cars.\n')

kolegium.set_place(smok)
kolegium.set_place(park1)
smok.set_place(kolegium)
smok.set_place(park1)
park1.set_place(kolegium)
park1.set_place(smok)
park1.set_place(center)
center.set_place(park1)
center.set_place(pub)
pub.set_place(center)
pub.set_place(park2)
park2.set_place(pub)
park2.set_place(station)

roommate = Friend('roommate', action=False)
mate = Friend('Matthew')
policeman = Enemy('Policeman', 100, 50)
bully1 = Enemy('Bully', 75, 10)
bully2 = Enemy('Strong bully', 120, 20)
bully3 = Enemy('Bully with knuckles', 75, 35)
whore = Friend('whore')
boss = Friend('Police captain')

roommate.set_dialogue(colored.blue('\n[roommate]: What are you looking at?\n[you]: ...\n[roommate]: Get lost!'))
mate.set_dialogue(colored.blue("[Matthew]: What an awful miserable day! Won't you miss days like this? \n\
[you]: ...\n[Matthew]: U wanna smoke with me for the last time?"))
whore.set_dialogue(colored.blue('[whore]: WhaT a prEtty yoUng fAcE. Do YoU have somEthinG to wEt my tHroaT?\[you]: ...'))
boss.set_dialogue(colored.red('Near half-hundred policemen point their guns on you. You have no way to run.\n\
[police captain]: Do you think that this is just a game!? Than your game is over!'))
bully1.set_description('A tall, thin man with a cigarret in his mouth and a bottle of beer in hand.\
\nHP:{}\nDamage:{}'.format(bully1.health, bully1.attack))
bully2.set_description('About 6 feet tall... lots of jailhouse tats.\nHP:{}\nDamage:{}'.format(
bully2.health, bully2.attack))
bully3.set_description('Drunk student with the metal knuckles and without front teeth.\nHP:{}\n\
Damage:{}'.format(bully3.health, bully3.attack))
policeman.set_description('Young stinking pig.\nHP:{}\nDamage:{}'.format(policeman.health, policeman.attack))


weapon1 = Weapon('TEC-9', 40)
weapon2 = Weapon('Shotgun', 80)
sig = Item('Cigarette')
beer = Item('Opillia')
ammo = Item('Ammo')

mate.set_gift(ammo)
whore.set_gift(whore)
mate.set_answer(sig, 'You lit a cigar. Slowly smoking, you gazed down at your friend.\n\
[Matthew]: You will need this.')
whore.set_answer(beer, 'You get out beer.\n[whore]: Let`S do tHiS in anOtheR plAce.')
boss.set_answer(whore,'You put the girl in front of you.\n[police captain]: Daughter!?\n\
[whore]: Dad! Help me!\nYou slap a whore.\n[police captain]: Don`t you dare touching her!\n\
You slap a whore again.\n[police captain]: Okay, okay! What do you want!?\n[you]: ...\n\
[police captain]: Everyone fall back! FALL BACK!\nYou jump into the empty train and escape!\n \
Congratulations! You win!')

weapon1.set_description('A gift from your friend. Damage: 40')
weapon2.set_description('Your favourite gun named Arlene. Damage: 80')
sig.set_description('Your favourite cigarrets Marlboro')
beer.set_description('A bottle of dark beer')
ammo.set_description('Few packs of ammos')

kolegium.set_person(roommate)
smok.set_person(mate)
park1.set_person(bully1)
center.set_person(policeman)
pub.set_person(bully2)
pub.set_person(bully3)
park2.set_person(whore)

kolegium.set_item(weapon1)
kolegium.set_item(weapon2)
kolegium.set_item(sig)
pub.set_item(beer)


def slow(text, speed):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        if speed == 1: time.sleep(0.06) 
        else: time.sleep(0.03) 

    print('')

def ending():
    current_room = station
    current_room.get_details()
    slow(colored.red(boss.talk()), 1)
    if whore in backpack.contents:
        slow(colored.red(boss.text), 1)
        print("\n\
 \t\t\t ______ _   _ _____  \n\
 \t\t\t|  ____| \ | |  __ \ \n\
 \t\t\t| |__  |  \| | |  | | \n\
 \t\t\t|  __| | . ` | |  | | \n\
 \t\t\t| |____| |\  | |__| | \n\
 \t\t\t|______|_| \_|_____/ \n\
                      \n\
___________   _______________________________________^__    \n\
 ___   ___ |||  ___   ___   ___    ___ ___  |   __  ,----\  \n\
|   | |   |||| |   | |   | |   |  |   |   | |  |  | |_____\     \n\
|___| |___|||| |___| |___| |___|  | O | O | |  |  |        \    \n\
           |||                    |___|___| |  |__|         )   \n\
___________|||______________________________|______________/    \n\
           |||                                        /-------- \n\
-----------'''---------------------------------------'")
    else:
        slow(colored.red('You had heard half-hundred gunshots. Everything went dark.'), 1)
        sys.exit()
    time.sleep(5)
    sys.exit()

backpack = Backpack()
health = 150
current_room = kolegium
try:
    winsound.PlaySound('retro.wav', winsound.SND_ASYNC)
except:
    import os
    os.system('aplay retro.wav&') #Linux
print(colored.red("\n \
\t\t\t  _____      _          _   __  __ _         _                     \n \
\t\t\t |  __ \    | |        | | |  \/  (_)       (_)                     \n \
\t\t\t | |__) |___| |__   ___| | | \  / |_ ___ ___ _  ___  _ __  ___       \n \
\t\t\t |  _  // _ \ '_ \ / _ \ | | |\/| | / __/ __| |/ _ \| '_ \/ __|       \n \
\t\t\t | | \ \  __/ |_) |  __/ | | |  | | \__ \__ \ | (_) | | | \__ \        \n \
\t\t\t |_|  \_\___|_.__/ \___|_| |_|  |_|_|___/___/_|\___/|_| |_|___/   \n\n\n\n "))
print("Don't forget your headphones. Play only in fullscreen.\n")


while health > 0:
    print('\n')
    current_room.get_details()
    persons = current_room.get_person()
    items = current_room.get_item()
    locations = current_room.get_locations()
    if len(persons) != 0:
        for person in persons:
            if person.__class__.__name__ == 'Friend':
                slow('[talk]: {}'.format(colored.blue(person.name)), 2)
            else:
                slow('[fight]: {}'.format(colored.red(person.name)), 2)
    if len(items) != 0:
        for item in items:
            if item.__class__.__name__ == 'Weapon':
                slow('[take]: {}'.format(colored.cyan(item.name)), 2)
            else:
                slow('[take]: {}'.format(colored.yellow(item.name)), 2)

    command = input("> ")

    if command == 'talk':
        if len(persons) != 0 and persons[0].__class__.__name__ == 'Friend':
            if persons[0].action == False:
                slow(persons[0].talk(), 1)
            else:
                slow(persons[0].talk(), 1)
                if persons[0].required in backpack.contents:
                    slow(colored.blue(persons[0].text), 1) 
                    gift = persons[0].gift
                    if gift.__class__.__name__ == 'Item':
                        slow('You got {}'.format(colored.yellow(gift.name)), 1)
                    else:
                        slow('The {} follows you now.'.format(colored.magenta(gift.name)), 1)
                    backpack.set_contents(gift)
                    del current_room.persons[0]
                else:
                    slow('You need {}'.format(persons[0].required.name), 1)

    elif command == 'fight':
        if len(persons) != 0 and persons[0].__class__.__name__ == 'Enemy':
            for person in persons:
                if weapon1 not in backpack.contents and weapon2 not in backpack.contents:
                    slow('You are too pussy to fight with bare hands. Find some gun!', 1)
                    break
                elif ammo not in backpack.contents:
                    slow('You must be Chuck Norris to shot without ammo. Find ammo!', 1)
                    break
                slow('{}\n{}'.format(colored.red(person.name), person.description), 1)
                while person.health > 0:
                    slow('Choose your weapon: ',1)
                    bag = []
                    if weapon1 in backpack.contents:
                        slow('{}'.format(colored.cyan(weapon1.name)), 1)
                        bag.append(weapon1.name)
                    if weapon2 in backpack.contents:
                        slow('{}'.format(colored.cyan(weapon2.name)), 1)
                        bag.append(weapon2.name)
                    command = 0
                    while command not in bag: 
                        try:
                            command = str(input("> "))
                        except:
                            command = 0
                            continue
                    if command == weapon1.name and command in bag:
                        person.damage(weapon1.damage)
                        slow('{} You hit him with {} damage'.format(colored.red('Bang-Bang-Bang!'), colored.red(weapon1.damage)), 1)
                    elif command == weapon2.name and command in bag: 
                        person.damage(weapon2.damage)
                        slow('{} You hit him with {} damage'.format(colored.red('BANG!', 'red'), colored.red(weapon2.damage)), 1)
                    slow('Your enemy`s health is {}'.format(colored.red(person.health)), 1)
                    if person.health > 0:
                        health -= person.attack
                        slow('{} Your enemy hit you! Your HP is {}'.format(colored.red('WHAT A PITY!', 'red'),colored.red(health)), 1)
                        if health <= 0:
                            break
                    else:
                        del current_room.persons[0]
                        for place in locations:
                            place.blocked = False

    elif command == 'take':
        if len(items) == 1:
            slow('You took {}'.format(items[0].name), 1)
            backpack.set_contents(items[0])
            del current_room.item[0]
        elif len(items) > 1:
            slow('What do you want to take?(Enter number)', 1)
            count = 1
            for item in items: 
                if item.__class__.__name__ == 'Weapon':
                    slow('{}. {} ({})'.format(count, colored.cyan(item.name), item.description), 1)
                else:
                    slow('{}. {} ({})'.format(count, colored.yellow(item.name), item.description), 1)
                count += 1
            command = 0
            while command not in range(1, len(items)+1): 
                try:
                    command = int(input("> "))
                except:
                    command = 0
                    continue
            if command-1 in range(len(items)):
                if items[command-1].__class__.__name__ == 'Weapon':
                    slow('You took {}'.format(colored.cyan(items[command-1].name)), 1)
                else:
                    slow('You took {}'.format(colored.yellow(items[command-1].name)), 1)
                backpack.set_contents(items[command-1])
                del current_room.item[command-1]

    elif command == 'leave':
        count = 1
        slow('Where do you wanna go?(Enter number)', 1)
        if len(locations) == 1:
            current_room = locations[0]
        else:
            for place in locations:
                slow('{}. {}'.format(count, (colored.green(place.name))), 1)
                count += 1
            command = 0
            while command not in range(1, len(locations)+1): 
                try: 
                    command = int(input("> "))
                except:
                    command = 0
                    continue
            if locations[command-1].blocked == False:
                if locations[command-1] != station:
                    current_room = locations[command-1]
                else:
                    ending()
            else:
                slow(colored.red('You wanna leave this bully alive!? Are you kidding!?'), 1)
    
    elif command == 'backpack':
        for item in backpack.contents:
            if item.__class__.__name__ == 'Weapon':
                slow('{} ({})'.format(colored.cyan(item.name), item.description), 1)
            elif item.__class__.__name__ == 'Item':
                slow('{} ({})'.format(colored.yellow(item.name), item.description), 1)
            else:
                slow('{}'.format(colored.magenta(item.name)), 1)
                
    elif command == 'exit':
        sys.exit()
        
print('You weren`t good enough for this game')
    


        








