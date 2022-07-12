import random

def flipcoin():
    heads = 0
    tails = 0
    headspercent = 0
    tailspercent = 0
    flip = int(input("Enter number of flips:"))
    for i in range(flip):
        coin=random.randint(1,2)

        if coin==1:
            heads+=1
        else:
            tails+=1

    headspercent = heads / (flip/100)
    tailspercent = 100.0 - headspercent

    print("Heads Percent:" + str(headspercent))
    print("Tails Percent:" + str(tailspercent))

flipcoin()