from hangman import Hangman

print(len([83, 105, 32,113,117,105,101,114,101,115,32,112,97,115,97,114,32,97,35,101,115,116,101,32,101,100,105,102,105,99,105,111,32,102,101,103,101,110,100,91,114,105,111,44,32,100,101,98,101,115,32,99,111,110,115,101,103,117,105,114,32,101,108,32,99,111,100,105]))
word = input("Which word do you want?: ")

game = Hangman(word)
while True:
    sol = input("Guess the word or a character: ")
    correct = game.guess(sol)
    if correct:
        print("You guessed correctly!")
    else:
        game + 1

