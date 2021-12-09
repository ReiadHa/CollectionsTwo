boodschappen = []
def add(): 
    global boodschappen
    quantity = 0
    vraag = input('wat wil je kopen? schrijf de item naam: ')
    hoeveel = int(input('hoeveel {} wilt u? '.format(vraag)))
    quantity = quantity + int(hoeveel)
    amount = quantity, vraag
    boodschappen.insert(1,amount)
    weer()
def weer():
    vragen = input('wilt u nog meer item toevoegen? ')
    if vragen == 'y' or vragen == 'Y':
        add()
    elif vragen == 'n' or vragen == 'N':
        print('bedankt voor je hulp! ')
        print('hier is uw lijst: ')
        print(boodschappen)
        pass
    else : 
        print('sorry dat begrijp ik niet! ')
        weer()
add()
weer()