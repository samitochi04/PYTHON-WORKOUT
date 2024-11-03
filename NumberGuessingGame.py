from random import randint as r


def guessing_game():
    number = r(0, 100)
    count = 3

    while count:
        user_guess = int(input("Guess which number hes been choosen? "))

        if user_guess < number:
            count -= 1
            if count < 1:
                print(f'Sorry, you didn’t guess in time, You have {count} guesses left.')
                break

            print(f'Your guess of {user_guess} is too low!👇, you have {count} guess(es) left.')

        elif user_guess > number:
            count -= 1
            if count < 1:
                print(f'Sorry, you didn’t guess in time, You have {count} guesses left.')
                break

            print(f'Your guess of {user_guess} is too high!👆, you have {count} guess(es) left.')

        else:
            print(f'Just right👌! The answer is {user_guess}')
            play = input("Would you like to play again Y/N? ")

            if play == "Y":
                number = r(0, 100)
            else:
                break

guessing_game()