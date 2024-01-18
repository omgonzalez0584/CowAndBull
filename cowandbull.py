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

rounds = 1
cow, bull = (0,0)    
while True:
    userlist = input("Enter four digits(You have five round): ")
    if rounds == 5:
        print("You complete the five rounds - Good Bye!")
        print(f"The 4 digits were {npclist}")
        break
    else:
        userlist = list(userlist)
        userlist = [int(i) for i in userlist]
        result = guessed_number(npclist, userlist)
        cow += result[0]
        bull += result[1]
        print(f"cow: {cow} - bull: {bull}  - You have {rounds} rounds")

    rounds += 1



