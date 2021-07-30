print("*******  *******  ******* ******SNAKES AND LADDERS*******  ********  *******  *******  ")
print("=======================================================================================")
print("                                  START!                                                                               ")
print("=======================================================================================")
import random
ladder = {1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}
snake = {32:10, 34:6, 48:26, 62:18, 88:24, 95:56, 97:78}
posn1 = 0
posn2 = 0

def move(pos):
    dice = random.randint(1, 6)
    print(f"Dice:{dice}")
    pos = pos + dice
    if pos in snake:
        print("Bitten by snake")
        pos = snake[pos]
        print(f"Position:{pos}")
    elif pos in ladder:
        print("Climbed the ladder")
        pos = ladder[pos]
        print(f"Position:{pos}")
    else:
        print(f"Positon:{pos}")
    print("\n")
    return pos

while True:
    A = input("Player 1 Enter R to throw the dice:")
    posn1 = move(posn1)
    if posn1 >= 100:
        print("Game over!!\nPlayer 1 wins.")
        break

    B = input("Player 2 Enter R to throw the dice:")
    posn2 = move(posn2)
    if posn2 >= 100:
        print("Game over!!\nPlayer 2 wins.")
        break


