import os
import random
import getpass
chances = 5
previousGuesses = []
print('Holy fuck')
os.system('clear')

print('Welcome to Hangman')
print()
answer = getpass.getpass('Enter a Word:')
guessedAnswer = '_'*len(answer)


def makeGuess(answer):
    global guessedAnswer
    checkForWin(answer, guessedAnswer)
    checkGameOver()
    print()
    print('Make a guess')
    print()
    print(guessedAnswer)
    global previousGuesses
    print()
    print('Previous Guesses: ', previousGuesses)

    print()
    guess = input().lower()
    if len(guess) > 1:
        makeGuess(answer)
    elif len(guess) < 1:
        makeGuess(answer)
    else:
        checkguess(guess, answer)

def printHangman(chances):
    if chances == 4:
        print('|')
        print('|')
        print('|')
        print('|')
    elif chances == 3:
        print('|--')
        print('|  o')
        print('|')
        print('|')
    elif chances == 2:
        print('|--')
        print('|  o')
        print('| \-/')
        print('|')
    elif chances == 1:
        print('|--')
        print('|  o')
        print('| \/')
        print('| /')
    else:
        print('|--')
        print('|  o')
        print('| \/')
        print('| /\ ')
        print('YOU DIED.')


def checkguess(guess, answer):
    if guess not in answer:
        global chances
        chances -= 1
        global previousGuesses
        previousGuesses.append(guess)
        print()
        printHangman(chances)
        # print('you have', chances, 'chances left')
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
    previousGuesses.append(guess)
    makeGuess(answer)

def checkForWin(answer, guessedAnswer):
    if answer == guessedAnswer:
        os.system('clear')
        print()
        print('YOU WIN!')
        print()
        exit()


def checkGameOver():
    global chances
    if chances == 0:
        print()
        print('GAMEOVER. YOU DIED.')
        print()
        exit()


makeGuess(answer)
