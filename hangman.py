import os
import random
import getpass
chances = 5
answer = ''
guessedAnswer = ''
os.system('clear')

print('Welcome to Hangman')

answer = getpass.getpass('Enter a Word:')
guessedAnswer = '_'*len(answer)


def makeGuess(answer):
    global guessedAnswer
    checkForWin(answer, guessedAnswer)
    print()
    print('Make a guess')
    print()
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
    if guess not in answer:
        global chances
        chances -= 1
        print()
        print('you have', chances, 'chances left')
        makeGuess(answer)
    else:
        for index, letter in enumerate(answer):
            if guess == letter:
                global guessedAnswer
                listify = list(guessedAnswer)
                listify[index] = guess
                joinGuessedAnswer = "".join(listify)
                guessedAnswer = joinGuessedAnswer

    os.system('clear')
    makeGuess(answer)

def checkForWin(answer, guessedAnswer):
    if answer == guessedAnswer:
        os.system('clear')
        print()
        print('YOU WIN!')
        print()
        exit()

makeGuess(answer)
