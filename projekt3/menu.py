import beker


menu_options = {
    1: 'Menüpont 1',
    2: 'Menüpont 2',
    3: 'Menüpont 3',
    4: 'Kilépés',
}

def menu1():
    print(menu_options[1])

    
def menu2():
    print(menu_options[2])
    
def menu3():
    print(menu_options[3])
    
def print_menu():
    #print(menu_options)
    print("============= Menüpontok ==================")
    for menupontIndex in menu_options:
        minta="{} --- {}"
        print(minta.format(menupontIndex,menu_options[menupontIndex]))
        #print(menu_options[menupontIndex])
    print("============================================")
    pass


while(True):
    print_menu()
    try:
        option = int(input('Válassz: '))
    except:
        option="nincsilyen"
        pass

    if option==1:
        menu1()
    elif option==2:
        menu2()
    elif option==3:
        menu3()
    elif option==4:
        print("Viszlát!")
        #exit()
        break

    else:
        print("Nincs ilyen menüpont!")
        
