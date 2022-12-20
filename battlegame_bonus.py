#wizard
wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150
#elf
elf = "Elf"
elf_damage = 100
elf_hp = 100
#human
human = "Human"
human_hp = 150
human_damage = 20
#witch
witch = "Witch"
witch_hp = 150
witch_damage = 100
#dragon
dragon_hp = 300
dragon_damage = 50

#Loop for Character selection below
#Keep characters inside loop, so it keeps the ability to re-enter your choice in the inginite loop.
while True:
    print('1. wizard')
    print('2. elf')
    print('3. human')
    print('4. Witch')
    character= input("Choose Your Character:").lower()
    if character == "1":
        character = wizard
        my_damage= wizard_damage
        my_hp = wizard_hp
        break
    elif character == "2":
        character = elf
        my_damage = elf_damage
        my_hp = elf_hp       
        break
    elif character == "3":
        character = human
        my_damage = human_damage
        my_hp = human_hp      
        break
    elif character == "4":
        character = witch
        my_damage = witch_damage
        my_hp = witch_hp
        break
    else:
        print("Unknown Character")
print("You have chosen: " + character)
print("Health: " + str(my_hp))
print("Damage: " + str(my_damage) + "\n")
#while loop used for the battle
while True:
    dragon_hp = dragon_hp - my_damage
    print("The " + character + " damaged the Dragon!")
    print("The Dragon's hitpoints are now: " + str(dragon_hp) + "\n")
    if dragon_hp <= 0:
        print("The Dragon Has Lost the Battle!")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at the " + character)
    print("The " + character + "'s hitpoints are now: " + str(my_hp) + "\n")
    if my_hp <= 0:
        print("The " + character + " has lost the battle.")
        break