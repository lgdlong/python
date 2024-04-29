import random

def menu():
        print("1. Keo")
        print("2. Bua")
        print("3. Bao")

def input_choice():
    menu()
    your_choice = int(input("Lua chon: "))
    return your_choice

def print_choice(your_choice):
    if (your_choice == 1):
        return "Keo"
    elif (your_choice == 2):
        return "Bua"
    else: # your_choice == 3
        return "Bao"


def print_2_side_choices(random_choice, your_choice):
    print("Ban chon:", print_choice(your_choice))
    print("Doi phuong chon:", print_choice(random_choice))

def print_result(random_choice, your_choice):
    if (random_choice == your_choice): # Ket qua Hue
        print("Hue!")
        print_2_side_choices(random_choice, your_choice)
        return True # Cap nhat gia tri cho dont_win
    elif (your_choice < random_choice): # Keo < Bua | Bua < Bao
        print("Ban thua!")
        print_2_side_choices(random_choice, your_choice)
        return True # Cap nhat gia tri cho dont_win
    else:
        print("Ban thang!")
        print_2_side_choices(random_choice, your_choice)
        return False # Cap nhat gia tri cho dont_win
        
        
        
        
        
# START PROGRAM

dont_win = True
while dont_win: 
    your_choice = input_choice()

    # Kiem tra lua chon khong hop le
    while your_choice not in [1, 2, 3]:
        print("Lua chon khong hop le!")
        your_choice = input_choice()
        
    # Khi lua chon hop le
    random_choice = random.randint(1, 3)
    dont_win = print_result(random_choice, your_choice, dont_win)
    


    
