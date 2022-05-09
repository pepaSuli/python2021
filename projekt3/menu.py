
menu_options = {
    1: 'Menüpont 1',
    2: 'Menüpont 2',
    3: 'Menüpont 3',
    4: 'Kilépés',
}

def print_menu():
    #print(menu_options)
    for menupontIndex in menu_options:
        minta="{} --- {}"
        print(minta.format(menupontIndex,menu_options[menupontIndex]))
        #print(menu_options[menupontIndex])
    pass


while(True):
    print_menu()
    try:
        option = int(input('Válassz: '))
    except:
        option="nincsilyen"
        pass

    if option==1:
        print("egy")
    elif option==2:
        print("kettő")
    elif option==3:
        print("három")
    elif option==4:
        print("Viszlát!")
        exit()

    else:
        print("Nincs ilyen menüpont!")
        
