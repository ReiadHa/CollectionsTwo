import random

scoreList = []

score = 0

def dices():
    global dice,gameOver
    gameOver = False
    if len(scoreList) == 6: 
            gameOver == True
    while gameOver == False:
        dice = []
        for x in range(5):
            dice.append(random.randint(1,6))
        print('jou dobbelestenen nummers zijn: ',end='')
        for i in dice:
            print(str(i), '',end='')
        reroll = input(', welke dobellestenen wile je rerollen? ')
        reroll = reroll.split()
        for index, x in enumerate(reroll):
            reroll[index] = int(x)-1
        for index in reroll:
            dice[index] = random.randint(1,6)
        print('jou dobbelstenen set: ', end='')
        for i in dice:
            print(str(i), '',end='')
        print('')
        scores()
def scores():
    global dice,score
    numberValid = False
    while not numberValid:
        numScore = int(input('welke nummer wil je scoren? '))
        if numScore not in scoreList:
            numberValid = True
        else:
            print('dit nummer had je al gescored!')
            print('de nummer die je al had gescored zij: ',str(scoreList))
        for d in dice:
            if d == numScore:
                score += d
        scoreList.append(numScore)
        print('de gescoorde nummers zij: ',str(scoreList))
        print('je score is: ',score)
dices()
