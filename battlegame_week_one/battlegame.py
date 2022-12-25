#wizard
wizard = "Wizard"
wizard_start_hp=70
wizard_hp = wizard_start_hp
wizard_damage = 150
#elf
elf = "Elf"
elf_damage = 100
elf_start_hp=100
elf_hp = elf_start_hp
#human 
human = "Human"
human_start_hp=150
human_hp = human_start_hp
human_damage = 20
#witch
witch = "Witch"
witch_start_hp=150
witch_hp = witch_start_hp
witch_damage = 100
#dragon
dragon_start_hp=300
dragon_hp = dragon_start_hp
dragon_damage = 50

#Loop for Character selection below
#Keep characters inside loop, so it keeps the ability to re-enter your choice in the infinite loop.   
play_again="Y"
while play_again == "Y":
    while play_again=="Y":
        print('1. Wizard')
        print('2. Elf')
        print('3. Human')
        print('4. Witch')
        print('5. EXIT')
        character= input("Choose Your Character:")
        if character == "1" or character.lower() == "wizard":
            character = wizard
            my_damage= wizard_damage
            wizard_hp=wizard_start_hp
            my_hp = wizard_hp
            dragon_hp=dragon_start_hp
            break
        elif character == "2" or character.lower() == "elf":
            character = elf
            my_damage = elf_damage
            elf_hp=elf_start_hp
            my_hp = elf_hp
            dragon_hp=dragon_start_hp       
            break
        elif character == "3" or character.lower() == "human":
            character = human
            my_damage = human_damage
            human_hp=human_start_hp
            my_hp = human_hp
            dragon_hp=dragon_start_hp      
            break
        elif character == "4" or character.lower() == "witch":
            character = witch
            my_damage = witch_damage
            witch_hp=witch_start_hp
            my_hp = witch_hp
            dragon_hp=dragon_start_hp
            break
        elif character == '5' or character.lower() == "exit":
            quit()
        else:
            print("Unknown Character")
    print("You have chosen: " + character)
    print("Health: " + str(my_hp))
    print("Damage: " + str(my_damage) + "\n")
#while loop used for the battle
    while play_again=="Y":
        dragon_hp = dragon_hp - my_damage
        print("The " + character + " damaged the Dragon!")
        print("The Dragon's hitpoints are now: " + str(dragon_hp) + "\n")
        if dragon_hp <= 0:
            print("The Dragon Has Lost the Battle!")
            play_again = input("Would you like to play again? Yes or No?")
            if play_again.lower() == "yes":
                play_again ="Y"
                break
        my_hp = my_hp - dragon_damage
        print("The Dragon strikes back at the " + character)
        print("The " + character + "'s hitpoints are now: " + str(my_hp) + "\n")
        if my_hp <= 0:
            print("The " + character + " has lost the battle.")
            play_again = input("Would you like to play again? Yes or No?")
            if play_again.lower() == "yes":
                play_again ="Y"
                break