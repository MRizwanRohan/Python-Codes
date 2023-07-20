import random
print("")
print("************** GUSSING GAME *************")
print("")
top_value = int(input("Input the top number of guessing game: "))

random_value = random.randint(0, top_value)

guessed = 0

print("__________________________________")
while True:
    guessed += 1
    guess_number= input("Guess a value: ")
    if guess_number.isdigit():
        guess_number=int(guess_number)
    else:
        print("Please enter a number next time")
        continue

    if guess_number==random_value:
        print("")
        print("Ye!!!! YOU GOT IT RIGHT ")
        break
    else:
        if guess_number > random_value:
            print("__________________________________")
            print("You guessed above")
        else:
            print("__________________________________")
            print("You guessed under")

print("-------------------------------------------")
print("|IT TOOK YOU "+str(guessed)+" TIME TO GET THE CORRECT ONE|")
print("-------------------------------------------")