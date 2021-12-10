import random
def cardGame():
    harten   = ['harten 1','harten  2','harten 3','harten 4','harten 5','harten 6','harten 7','harten 8','harten 9','harten 10','harten boer',' harten vrouw','harten heer',]
    klaveren = ['klaveren 1','klaveren 2','klaveren 3','klaveren 4','klaveren 5','klaveren 6','klaveren 7 ',' klaveren 8','klaveren 9','klaveren 10','klaveren boer','klaveren vrouw','klaveren heer',]
    schoppen = ['schoppen 1','schoppen 2','schoppen  3','schoppen 4','schoppen 5','schoppen 6','schoppen 7','schoppen 8','schoppen 9','schoppen 10','schoppen boer','schoppen vrouw','schoppen heer']
    ruiten   = ['ruiten 1','ruiten 2','ruiten 3','ruiten 4','ruiten 5','ruiten 6','ruiten 7','ruiten 8','ruiten 9','ruiten 10','ruiten boer','ruiten vrouw','ruiten heer',]
    joker    = ['Joker','Joker']
    cards = harten+klaveren+schoppen+ruiten+joker
    random.shuffle(cards)
    number = 0
    for i in range(7):
        hand = []
        hand.append(cards.pop(random.randint(1,len(cards)-1)))
        number +=1
        print('kaart ',number, ':' , hand)
    print('')
    print('Deck (kaarten -> 47):',cards)

cardGame()