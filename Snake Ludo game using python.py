
import random
print("-----------------------------------------")
print("######### WELCOME TO SNAKE GAME #########")
print("**BEWARE OR SNAKES ! THEY MIGHT EAT YOU**")
print("-----------------------------------------")
score = 0
while True:
    input("Press 'Enter' to roll the dice.")
    dice = random.randint(1, 6)

    score += dice

    if score == 15 :
        print("ROLLED  = ", dice)
        print("Score is = ", score)
        print("YOU ARE EATEN BY SNAKE")
        print("GAME OVER")
        break
    elif score == 29 :
        print("ROLLED  = ", dice)
        print("Score is = ", score)
        print("YOU ARE EATEN BY SNAKE")
        print("GAME OVER")
        break
    elif score == 37 :
        print("ROLLED  = ", dice)
        print("Score is = ", score)
        print("YOU ARE EATEN BY SNAKE")
        print("GAME OVER")
        break
    elif score == 51 :
        print("ROLLED  = ", dice)
        print("Score is = ", score)
        print("YOU ARE EATEN BY SNAKE")
        print("GAME OVER")
        break
    elif score == 82:
        print("ROLLED  = ", dice)
        print("Score is = ", score)
        print("YOU ARE EATEN BY SNAKE")
        print("GAME OVER")
        break
    elif score == 91 :
        print("ROLLED  = ", dice)
        print("Score is = ", score)
        print("YOU ARE EATEN BY SNAKE")
        print("GAME OVER")
        break
    elif score == 94 :
        print("ROLLED  = ", dice)
        print("Score is = ", score)
        print("YOU ARE EATEN BY SNAKE")
        print("GAME OVER")
        break

    if score >= 100:
        print("ROLLED  = ", dice)
        print("")
        print("YOU HAVE REACHED 100 OR ABOVE.")
        print("******** YOU HAVE WON ********")
        break


    print("ROLLED  = ", dice)
    print("Score is = ", score)

