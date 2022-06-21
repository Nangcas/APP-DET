# MALICDEM, ANTONIEL D
# NANGCAS, CHAISKA

#THE PROGRAM WILL ALLOW THE USER TO CUSTOMIZE TWO (2) CHARACTER
#, USE OBJECTS TO CREATE THE TWO CHARACTERS WITH THE FOLLOWING
# CHARACTERISTICS(PARAMETER): CLASS, WEAPON, AND ABILITY.

from ast import Break, Continue, If, While
from secrets import choice


class CHARACTERISTICS:
    def __init__(ATTACKER, CHARACTERISTICCLASS, WEAPON, ABILITY1, ABILITY2):
        ATTACKER.CHARACTERISTICCLASS = CHARACTERISTICCLASS
        ATTACKER.WEAPON = WEAPON
        ATTACKER.ABILITY1 = ABILITY1
        ATTACKER.ABILITY2 = ABILITY2

    def SETCLASS(ATTACKER):
        while True:
            print("Enter a Class:")
            print("\t1. WIZARD")
            print("\t2. KNIGHT")
            print("\t3. ARCHER")
            print("\t4. ASSASSIN")
            choice = int(input("SELECT THE CHARACTER: "))

            if choice in (1, 2, 3, 4):
                if choice == 1:
                    ATTACKER.CHARACTERISTICCLASS = "WIZARD"
                    print("CHARACTER SELECTED: WIZARD")
                elif choice == 2:
                    ATTACKER.CHARACTERISTICCLASS = "KNIGHT"
                    print("CHARACTER SELECTED: KNIGHT")
                elif choice == 3:
                    ATTACKER.CHARACTERISTICCLASS = "ARCHER"
                    print("CHARACTER SELECTED: ARCHER")
                elif choice == 4:
                    ATTACKER.CHARACTERISTICCLASS = "ASSASSIN"
                    print("CHARACTER SELECTED: ASSASSIN")
                Break
            else:
                print("INCORRECT CHOICE OF CHARACTER.CHOOSE AGAIN FROM 1-4")
                Continue
    def SETWEAPON(ATTACKER):
        while True:
            print("\nEnter A Weapon:")
            print("\t1. WIZARD STAFF")
            print("\t2. SWORD")
            print("\t3. BOW $ ARROW")
            print("\t4. KATAR")
            choice = int(input("SELECT THE WEAPON: "))

            if choice in (1, 2, 3, 4):
                if choice == 1:
                    ATTACKER.WEAPON = "WIZRD STAFF"
                    print("WEAPON SELECTED: WIZARD STAFF")
                elif choice == 2:
                    ATTACKER.WEAPON = "SWORD"
                    print("WEAPON SELECTED: SWORD")
                elif choice == 3:
                    ATTACKER.WEAPON = "BOW & ARROW"
                    print("WEAPON SELECTED: BOW & ARROW")
                elif choice == 4:
                    ATTACKER.WEAPON = "KATAR"
                    print("WEAPON SELECTED: KATAR")
                break
            else:
                print("INCORRECT CHOICE OF WEAPOM. CHOOSE AGAIN FROM 1-4")
                continue
    
    def SETABILITY(ATTACKER):
        while True:
            if(ATTACKER.CHARACTERISTICCLASS == "WIZARD"):
                print("\nSELECT THE ABILITY FOR ATTACKER:")
                print("\t1. ENEGRY BALL")
                print("\t2. DRAGONS BREATH")
                print("\t3. CROWN OF FLAME")
                print("\t4. HAIL STORM")
                choice1 = int(input("SELECT THE ABILITY 1: "))
                choice2 = int(input("SELECT THE ABILITY 2: "))
                
                if choice1 in (1, 2, 3, 4):
                    if choice1 == 1:
                        ATTACKER.ABILITY1 = "ENEGRY BALL"
                        print("ABILITY 1: ENEGRY BALL")
                    elif choice1 == 2:
                        ATTACKER.ABILITY1 = "DRAGONS BREATH"
                        print("ABILITY 1: DRAGONS BREATH")
                    elif choice1 == 3:
                        ATTACKER.ABILITY1 = "CROWN OF FLAME"
                        print("ABILITY 1: CROWN OF FLAME")
                    elif choice1 == 4:
                        ATTACKER.ABILITY1 = "HAIL STORM"
                        print("ABILITY 1: HAIL STORM")
                else:
                    print(" INCORRECT CHOICE OF ABILITY 1 FOR THE ATTACKER. CHOICE AGAIN FORM 1-4")
                    continue

                if choice1 in (1, 2, 3, 4):
                    if choice1 == 1:
                        ATTACKER.ABILITY2 = "ENEGRY BALL"
                        print("ABILITY 2: ENEGRY BALL")
                    elif choice1 == 2:
                        ATTACKER.ABILITY2 = "DRAGONS BREATH"
                        print("ABILITY 2: DRAGONS BREATH")
                    elif choice1 == 3:
                        ATTACKER.ABILITY2 = "CROWN OF FLAME"
                        print("ABILITY 2: CROWN OF FLAME")
                    elif choice1 == 4:
                        ATTACKER.ABILITY2 = "HAIL STORM"
                        print("ABILITY 2: HAIL STORM")
                else:
                    print(" INCORRECT CHOICE OF ABILITY 2 FOR THE ATTACKER. CHOICE AGAIN FORM 1-4")
                    continue

            if(ATTACKER.CHARACTERISTICCLASS == "KNIGHT"):
                print("\nSELECT THE ABILITY  FOR ATTACKER:")
                print("\t1. FIRE SLASH")
                print("\t2. POWER SLASH")
                print("\t3. GIGANTIC STORM")
                print("\t4. CHAOTIC DISASTER")
                choice1 = int(input("SELECT THE ABILITY 1: "))
                choice2 = int(input("SELECT THE ABILITY 2: "))
                
                if choice1 in (1, 2, 3, 4):
                    if choice1 == 1:
                        ATTACKER.ABILITY1 = "FIRE SLASH"
                        print("ABILITY 1: FIRE SLASH")
                    elif choice1 == 2:
                        ATTACKER.ABILITY1 = "POWER SLASH"
                        print("ABILITY 1: POWER SLASH")
                    elif choice1 == 3:
                        ATTACKER.ABILITY1 = "GIGANTIC STORM"
                        print("ABILITY 1: GIGANTIC STORM")
                    elif choice1 == 4:
                        ATTACKER.ABILITY1 = "CHAOTIC DISASTER"
                        print("ABILITY 1: CHAOTIC DISASTER")
                else:
                    print("INCORRECT CHOICE OF ABILITY 1 FOR THE ATTACKER. CHOICE AGAIN FROM 1-4.")
                    continue

                if choice1 in (1, 2, 3, 4):
                    if choice1 == 1:
                        ATTACKER.ABILITY2 = "FIRE SLASH"
                        print("ABILITY 2: FIRE SLASH")
                    elif choice1 == 2:
                        ATTACKER.ABILITY2 = "POWER SLASH"
                        print("ABILITY 2: POWER SLASH")
                    elif choice1 == 3:
                        ATTACKER.ABILITY2 = "GIGANTIC STORM"
                        print("ABILITY 2: GIGANTIC STORM")
                    elif choice1 == 4:
                        ATTACKER.ABILITY2 = "CHAOTIC DISASTER"
                        print("ABILITY 2: CHAOTIC DISASTER")
                else:
                    print("INCORRECT CHOICE OF ABILITY 2 FOR THE ATTACKER. CHOICE AGAIN FROM 1-4.")
                    continue

                if(ATTACKER.CHARACTERISTICCLASS == "ARCHER"):
                    print("\nSELECT THE ABILITY FOR ATTACKER:")
                    print("\t1. TAKE AIM")
                    print("\t2. QUICK SHOT")
                    print("\t3. BLAZING ARROW")
                    print("\t4. FROST ARROW")
                    choice1 = int(input("SELECT THE ABILITY 1: "))
                    choice2 = int(input("SELECT THE ABILITY 2: "))

                    if choice1 in (1, 2, 3, 4):
                        if choice1 == 1:
                            ATTACKER.ABILITY1 = "TAKE AIM"
                            print("ABILITY 1: TAKE AIM")
                        elif choice1 == 2:
                            ATTACKER.ABILITY1 = "QUICK SHOT"
                            print("ABILITY 1: QUICK SHOT")
                        elif choice1 == 3:
                            ATTACKER.ABILITY1 = "BLAZING ARROW"
                            print("ABILITY 1: BLAZING ARROW")
                        elif choice1 == 4:
                            ATTACKER.ABILITY1 = "FROST ARROW"
                            print("ABILITY 1: FROST ARROW")
                else:
                    print("INCORRECT CHOICE OF ABILITY 1 FOR THE ATTACKER. CHOICE AGAIN FROM 1-4.")
                    continue

                    if choice1 in (1, 2, 3, 4):
                        if choice1 == 1:
                            ATTACKER.ABILITY2 = "TAKE AIM"
                            print("ABILITY 2: TAKE AIM")
                        elif choice1 == 2:
                            ATTACKER.ABILITY2 = "QUICK SHOT"
                            print("ABILITY 2: QUICK SHOT")
                        elif choice1 == 3:
                            ATTACKER.ABILITY2 = "BLAZING ARROW"
                            print("ABILITY 2: BLAZING ARROW")
                        elif choice1 == 4:
                            ATTACKER.ABILITY2 = "FROST ARROW"
                            print("ABILITY 2: FROST ARROW")
                    else:
                        rint("INCORRECT CHOICE OF ABILITY 2 FOR THE ATTACKER. CHOICE AGAIN FROM 1-4.")
                        continue

                if(ATTACKER.CHARACTERISTICCLASS == "ASSASIN"):
                    print("\nSELECT THE ABILITY FOR ATTACKER:")
                    print("\t1. CLOAKING")
                    print("\t2. ENCHANT POISON")
                    print("\t3. SONIC ACCELERATION")
                    print("\t4. METEOR ASSAULT")
                    choice1 = int(input("SELECT THE ABILITY 1: "))
                    choice2 = int(input("SELECT THE ABILITY 2: "))

                    if choice1 in (1, 2, 3, 4):
                        if choice1 == 1:
                            ATTACKER.ABILITY1 = "CLOAKING"
                            print("ABILITY 1: CLOAKING")
                        elif choice1 == 2:
                            ATTACKER.ABILITY1 = "ENCHANT POISON"
                            print("ABILITY 1: ENCHANT POISON")
                        elif choice1 == 3:
                            ATTACKER.ABILITY1 = "SONIC ACCELERATION"
                            print("ABILITY 1: SONIC ACCELERATION")
                        elif choice1 == 4:
                            ATTACKER.ABILITY1 = "METEOR ASSAULT"
                            print("ABILITY 1: METEOR ASSAULT")
                    else:
                        print("INCORRECT CHOICE OF ABILITY 1 FOR THE ATTACKER. CHOICE AGAIN FROM 1-4.")
                        continue

                    if choice1 in (1, 2, 3, 4):
                        if choice1 == 1:
                            ATTACKER.ABILITY2 = "CLOAKING"
                            print("ABILITY 2: CLOAKING")
                        elif choice1 == 2:
                            ATTACKER.ABILITY2 = "ENCHANT POISON"
                            print("ABILITY 2: ENCHANT POISON")
                        elif choice1 == 3:
                            ATTACKER.ABILITY2 = "SONIC ACCELERATION"
                            print("ABILITY 2: SONIC ACCELERATION")
                        elif choice1 == 4:
                            ATTACKER.ABILITY2 = "METEOR ASSAULT"
                            print("ABILITY 2: METEOR ASSAULT")
                    else:
                        print("INCORRECT CHOICE OF ABILITY 2 FOR THE ATTACKER. CHOICE AGAIN FROM 1-4.")
                        continue

print("\nCustomize your first character:")
char1 = CHARACTERISTICS("initCHARACTERISTICCLASS", "initWEAPON", "initABILITY1", "initABILITY2")
char1.SETCLASS()
char1.SETWEPON()
char1.SETABILITY()

print("\nCustomize your second character:")
char2 = CHARACTERISTICS("initCHARACTERISTICCLASS", "initWEAPON", "initABILITY1", "initABILITY2")
char2.SETCLASS()
char2.SETWEAPON()
char2.SETABILITY()

print("\nCharacter 1 Details:")
print("CHARACTER: " + char1.CHARACTERISTICCLASS)
print("WEAPON: " + char1.WEAPON)
print("ABILITIES: " + char1.ABILITY1 + ", " + char1.ABILITY2 +"\n")

print("\nCharacter 2 Details:")
print("CHARACTER: " + char2.CHARACTERISTICCLASS)
print("WEAPON: " + char2.WEAPON)
print("ABILITIES: " + char2.ABILITY1 + ", " + char2.ABILITY2 +"\n")

    
    
   

    
