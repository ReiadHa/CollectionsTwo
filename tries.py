import random
def wachtwoord():
    length = 24
    numbers = list('1234567890')
    lowerC = list('abcdefghijklmnopqrstuvwxyz')
    upperC = list('ABDCEFGHIJKLMNOPQRSTUVWXYZ')
    symbols = list('@#$%&_')
    num = []
    up = []
    low = []
    sym = []                                 
    password = []
    for i in range(random.randint(4,7)):
        num.append(random.choice(numbers))
    for i in range(8):
        low.append(random.choice(lowerC))
    for i in range(3):
        sym.append(random.choice(symbols))
    for i in range(random.randint(2,6)):
        up.append(random.choice(upperC))
    password = num + up +low +sym
    amount = 24-len(password)
    if len(password)< length:
        choice3 = [random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(amount)]
        password = num + up +low +sym+choice3
    elif  password [0:2] == num and password[0:2] ==sym  and password[0:-1] == sym :
        wachtwoord()
    random.shuffle(password)
    print(''.join(password))

    
wachtwoord()
