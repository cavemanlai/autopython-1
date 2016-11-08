import random

print('Guess the number form 1 to 20 in 6 times.')
SecretNum = random.randint(1,20)

for times in range(1,7):
    GuessNum = int(input('Input your guessed number:'))
    # if times < 6:
    #     if GuessNum != SecretNum:
    #         if GuessNum > SecretNum:
    #             print('Too high')
    #         elif GuessNum < SecretNum:
    #             print('Too low')
    #     elif GuessNum == SecretNum:
    #         print('You guessed the number in ' + str(int(times)) + ' guesses')
    #         break
    # else:
    #     print('Bad luck.You have no chance.')
    if GuessNum > SecretNum:
        print('Too high')
    elif GuessNum < SecretNum:
        print('Too low')
    else:
        break
if GuessNum == SecretNum:
    print('You guessed the number in ' + str(int(times)) + ' guesses')
else:
    print('Bad luck.You have no chance.')