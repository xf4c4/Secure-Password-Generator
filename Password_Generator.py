import os
import random

def Is_UpperCase(upperCase):
    random_Number = random.randint(0,26)
    letter = upperCase[random_Number]
    return letter
def Is_LowerCase(lowerCase):
    ramdom_Number = random.randint(0,26)
    letter = lowerCase[ramdom_Number]
    return letter
def Is_Nums(nums):
    random_Number = random.randint(0,9)
    num = nums[random_Number]
    return num
def Is_Symbols(symbols):
    random_Number = random.randint(0,7)
    symbol = symbols[random_Number]
    return symbol
def Custom_Passwords():
    have_UpperCase = input("¿Lleva mayusculas?[y/n]: ")
    have_LowerCase = input("¿Lleva minusculas?[y/n]: ")
    have_Nums = input("¿Lleva numeros?[y/n]: ")
    have_Symbols = input("¿Lleva simbolos?[y/n]: ")
    lenght = int(input("Dime cuantos caracteres quieres que contenga tu contraseña en numero: "))

    if have_UpperCase == "n" and have_LowerCase == "n" and have_Nums == "n" and have_Symbols == "n":
        print("""    
              TROLEA A TU PRIMA
                     ---
                     | |
                     | |
               ------   ---
               (-- -- -- --)
                (         )
                 \       /
                  |     /""")
    elif have_UpperCase == "y" and have_LowerCase == "n" and have_Nums == "n" and have_Symbols == "n":
        for x in range(lenght):
            print(Is_UpperCase(upperCase), end="")

    elif have_UpperCase == "y" and have_LowerCase == "y" and have_Nums == "n" and have_Symbols == "n":
        for x in range(lenght):
            random_Functions = {
                1: Is_UpperCase(upperCase),
                2: Is_LowerCase(lowerCase)
            }
            ramdom_Number = random.randint(1, 2)
            caracter = random_Functions[ramdom_Number]
            print(caracter, end="")
    elif have_UpperCase == "y" and have_LowerCase == "y" and have_Nums == "y" and have_Symbols == "n":
        for x in range(lenght):
            random_Functions = {
                1: Is_Nums(nums),
                2: Is_UpperCase(upperCase),
                3: Is_LowerCase(lowerCase)
            }
            ramdom_Number = random.randint(1, 3)
            caracter = random_Functions[ramdom_Number]
            print(caracter, end="")
    elif have_UpperCase == "y" and have_LowerCase == "y" and have_Nums == "y" and have_Symbols == "y":
        for x in range(lenght):
            random_Functions = {
                1: Is_Symbols(symbols),
                2: Is_Nums(nums),
                3: Is_UpperCase(upperCase),
                4: Is_LowerCase(lowerCase)
            }
            ramdom_Number = random.randint(1, 4)
            caracter = random_Functions[ramdom_Number]
            print(caracter, end="")
    elif have_UpperCase == "n" and have_LowerCase == "y" and have_Nums == "y" and have_Symbols == "y":
        for x in range(lenght):
            random_Functions = {
                1: Is_Symbols(symbols),
                2: Is_Nums(nums),
                3: Is_LowerCase(lowerCase)
            }
            ramdom_Number = random.randint(1, 3)
            caracter = random_Functions[ramdom_Number]
            print(caracter, end="")
    elif have_UpperCase == "n" and have_LowerCase == "n" and have_Nums == "y" and have_Symbols == "y":
        for x in range(lenght):
            random_Functions = {
                1: Is_Symbols(symbols),
                2: Is_Nums(nums)
            }
            ramdom_Number = random.randint(1, 2)
            caracter = random_Functions[ramdom_Number]
            print(caracter, end="")
    elif have_UpperCase == "n" and have_LowerCase == "n" and have_Nums == "n" and have_Symbols == "y":
        for x in range(lenght):
            print(Is_Symbols(symbols), end="")
    elif have_UpperCase == "n" and have_LowerCase == "y" and have_Nums == "n" and have_Symbols == "n":
        for x in range(lenght):
            print(Is_LowerCase(lowerCase), end="")
    elif have_UpperCase == "n" and have_LowerCase == "n" and have_Nums == "y" and have_Symbols == "n":
        for x in range(lenght):
            print(Is_Nums(nums), end="")
    elif have_UpperCase == "y" and have_LowerCase == "n" and have_Nums == "y" and have_Symbols == "y":
        for x in range(lenght):
            random_Functions = {
                1: Is_Symbols(symbols),
                2: Is_Nums(nums),
                3: Is_UpperCase(upperCase),
            }
            ramdom_Number = random.randint(1, 3)
            caracter = random_Functions[ramdom_Number]
            print(caracter, end="")
    elif have_UpperCase == "y" and have_LowerCase == "n" and have_Nums == "n" and have_Symbols == "y":
        for x in range(lenght):
            random_Functions = {
                1: Is_Symbols(symbols),
                2: Is_UpperCase(upperCase),
            }
            ramdom_Number = random.randint(1, 2)
            caracter = random_Functions[ramdom_Number]
            print(caracter, end="")
    elif have_UpperCase == "y" and have_LowerCase == "n" and have_Nums == "y" and have_Symbols == "n":
        for x in range(lenght):
            random_Functions = {
                1: Is_Nums(nums),
                2: Is_UpperCase(upperCase),
            }
            ramdom_Number = random.randint(1, 2)
            caracter = random_Functions[ramdom_Number]
            print(caracter, end="")
    elif have_UpperCase == "n" and have_LowerCase == "y" and have_Nums == "y" and have_Symbols == "n":
        for x in range(lenght):
            random_Functions = {
                1: Is_Nums(nums),
                2: Is_LowerCase(lowerCase)
            }
            ramdom_Number = random.randint(1, 2)
            caracter = random_Functions[ramdom_Number]
            print(caracter, end="")
    elif have_UpperCase == "n" and have_LowerCase == "y" and have_Nums == "n" and have_Symbols == "y":
        for x in range(lenght):
            random_Functions = {
                1: Is_Symbols(symbols),
                2: Is_LowerCase(lowerCase)
            }
            ramdom_Number = random.randint(1, 2)
            caracter = random_Functions[ramdom_Number]
            print(caracter, end="")
    else :
        print("Falta programar")

def Menu(boolean):
    bienvenida = "|            PASSWORD GENERATOR                |"
    print(("\n"+"-" * len(bienvenida)) + "\n" + bienvenida + "\n" + ("-" * len(bienvenida)))
    if boolean:
        print("Por favor, elige una opcion numerica [1,2]\n")
    print("Elige una opcion: \n")
    print("""    1. Quiero una contraseña segura 
    2. Quiero personalizar mi contraseña
    3. Salir del programa""")
    choose = int(input("----> "))
    while choose < 1 or choose > 3:
        if choose == 3:
            break
        choose = Menu(True)
    return choose


#Main program
if __name__ == '__main__':

    upperCase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lowerCase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","q","p","q","r","s","t","u","v","w","x","y","z"]
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    symbols = ["@","#","$","&","?","¿","+","!"]
    run_Program = True
    #Main loop
    while run_Program:
        choose = Menu(False)
        if choose == 1:
            lenght = int(input("¿Cuantos caracteres quieres que tenga tu contraseña?: "))
            for x in range(lenght):
                random_Functions = {
                    1: Is_Symbols(symbols),
                    2: Is_Nums(nums),
                    3: Is_UpperCase(upperCase),
                    4: Is_LowerCase(lowerCase)
                }
                ramdom_Number = random.randint(1, 4)
                caracter = random_Functions[ramdom_Number]
                print(caracter, end="")
        elif choose == 2:
            Custom_Passwords()
        else:
            run_Program = False