import random

def lootjes():
    nameDict ={}
    listt = []
    secondList =[]
    vraag = int(input('hoeveel namen wil je invullen? '))
    for x in range(vraag):
        name = input("vul hier een naam: ")
        nameDict[name]= ""
        listt.append(name)
        secondList.append(name)
    while len(secondList) != 0:
        for x in listt:
                something = random.choice(secondList)
                if x != something:
                    nameDict[x]=something
                    secondList.remove(something)
                else:
                    secondList= listt.copy()
                    break
    return nameDict
        
print(lootjes())