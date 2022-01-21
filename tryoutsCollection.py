import random
chance = False
def dieRolls():
    print('the dice rolls are: ',end='')
    for i in dice:
        print(str(i) , '',end='')
scoreList = []
score =0 
gameOver = False
def counting(numScore):
    global score
    if dice.count(numScore) == 3 or dice.count(numScore) == 4:
        score = score + sum(dice)
    elif 1 in dice and 2 in dice and 3 in dice and 4 in dice:
        print('gefeliciteerd je hebt een straight gewonnen, dat betekent +30 points? ')
        score = score + 30
    elif 2 in dice and 3 in dice and 4 in dice and 5 in dice :
        print('gefeliciteerd je hebt een straight gewonnen, dat betekent +30 points? ')
        score = score + 30
    elif 3 in dice and 4 in dice and 5 in dice and 6 in dice:
        print('gefeliciteerd je hebt een straight gewonnen, dat betekent +30 points? ')
        score = score + 30
    elif 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
        score = score + 40
    elif dice.count(numScore) == 5 :
        print('Yhatzee')
        score = score + 50
        print('gefeliciteerd, jij hebt gewonnen! ')
        gameOver == True
    elif dice.count(numScore) != 3 or dice.count(numScore) != 4:
        for d in dice:
            if d ==  numScore:
                score += d
def kansen():
    global chance
    global dice
    chance = False
    if chance == False:
        global score
        vraagje = input('wil je je kans nu gebruiken?(Y/N) ')
        if vraagje == 'ja' or vraagje == 'y' or vraagje == 'yes':
            score = score + sum(dice)
            chance = True
            print('je score is: ',score)
            somehing()
        elif vraagje == 'nee' or vraagje == 'N' or vraagje == 'No' or vraagje == 'n':
            pass
        
        
def somehing():
    global dice
    while gameOver == False:
        dice = []
        for i in range(5):
            dice.append(random.randint(1,6))
        dieRolls()
        print('')
        if chance == False:
            kansen()
        reroll = input('welke dobblesteen wile je rerollen? ')
        reroll = reroll.split()
        for index, x in enumerate(reroll):
            reroll[index] = int(x)-1
        for index in reroll:
            dice[index]  = random.randint(1,6)
        if chance == False:
            kansen()
        dieRolls()
        scores()
        break
def scores():
    global gameOver
    numberValid = False
    while not numberValid:
        numScore = int(input('welke nummer wil je scoren: '))
        if numScore not in scoreList:
            numberValid = True
        else:
            print('je had dit nummer al gescored!')
            print('de nummer die je al had gescored zijn: ' +str(scoreList)+ '' , end='')
    scoreList.append(numScore)
    counting(numScore)
    print('de nummer die je al had gescored zijn: ' +str(scoreList))
    print('je score is: ',score)
    if len(scoreList) == 6 :
        print('je score is: ',score)
        gameOver = True
        quit()
    somehing()

somehing()
