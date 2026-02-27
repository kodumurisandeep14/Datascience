import random

position = 0

for step in range(10):
    action = random.choice(["right","left"])
    if action == "right":
        position +=1
    else:
        position -+1
    position =max(0,min(position,4))

    print("step:",step, "Position:",position)

    if position ==4:
        print("goal reached")
        break
