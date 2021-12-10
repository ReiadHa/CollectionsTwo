from random import randint


import random
def wachtwoord():
    numbers = list('1234567890')
    lowerC = list('abcdefghijklmnopqrstuvwxyz')
    upperC = list('ABDCEFGHIJKLMNOPQRSTUVWXYZ')
    symbols = list('@#$%&_')
    password = []
    for i in range(7):
        password.append(random.choice(numbers))
    for i in range(8):
        password.append(random.choice(lowerC))
    for i in range(3):
        password.append(random.choice(symbols))
    for i in range(6):
        password.append(random.randint(upperC))
    print(password)
wachtwoord()