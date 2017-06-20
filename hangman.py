import os
import random
import getpass
chances = 5

os.system('clear')

print('Welcome to Hangman')

words = ['howdy']

answer = getpass.getpass('Enter a Word:')
guessedAnswer = '_'*len(answer)

def makeGuess(answer):
    global guessedAnswer
    checkForWin(answer, guessedAnswer)
    print()
    print('Make a guess')
    print(guessedAnswer)

    print()
    guess = input().lower()
    if len(guess) > 1:
        makeGuess(answer)
    elif len(guess) < 1:
        makeGuess(answer)
    else:
        checkguess(guess, answer)

def checkguess(guess, answer):
    if guess in answer:
        print('Got one!')
        guess_index = answer.find(guess)

        global guessedAnswer
        listify = list(guessedAnswer)
        listify[guess_index] = guess
        joinGuessedAnswer = "".join(listify)
        guessedAnswer = joinGuessedAnswer
    else:
        global chances
        chances -= 1
        print('you have', chances, 'chances left')
        makeGuess(answer)

    makeGuess(answer)

def checkForWin(answer, guessedAnswer):
    if answer == guessedAnswer:
        os.system('clear')
        print('YOU WIN!')
        print()
        print('Play Again? Y/N')
        playAgain = input().lower()
        if playAgain == 'y':
            makeGuess(answer)
        else:
            exit()

makeGuess(answer)
