import random

words = ["algeria", "tunisia", "egypt", "france"]
chooseWords = random.choice(words)
wordDis = ["_" for _ in chooseWords]
attemps = 8
##################################

print("Welcome to The Game")
print("Created By Rabah")
print("Enjoy!! :)")

while attemps > 0 and '_' in wordDis:
    print("\n" + " ".join(wordDis))
    guess_= input("Guss a letter: ").lower()

    if guess_ in chooseWords:
        for index, letter in enumerate(chooseWords):
            if letter == guess_:
              wordDis[index] = guess_
    else:
        print("That Word not found")
        attemps -=1

if "_" not in wordDis:
    print("You guessed the word")
    print(" ".join(wordDis))
    print("You Win")
else:
    print("The word was " + chooseWords)
    print("game lost")