import random

def guessed_number(npclist, userlist):
    cow,bull = (0,0)
    for i in userlist:
        if i in npclist and userlist.index(i) == npclist.index(i):
            cow += 1
        elif i in npclist and userlist.index(i) != npclist.index(i):
            bull +=1
    return  cow, bull




npclist = [random.randint(0,9) for i in range(0,4)]
#print(npclist)


userlist = input("Enter four digits: ")
userlist = list(userlist)
userlist = [int(i) for i in userlist]

cow , bull = guessed_number(npclist, userlist)
print(f"cow: {cow} - bull: {bull}")




