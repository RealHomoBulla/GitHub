'''
Task 1
The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
'''

from random import randint

print('\nHello, this is a guessing game. Try to guess a number between 1 and 10! You have 3 attempts.')
print('Also, you may enter "Q" or "q" to quit the game.\n')
# I use While-Loop for endless game and to suggest to play again
play = True

# Body of the game is inside the function to be re-callable
def game():
    print('Hm, let me think of a number...')
    print('Okay, I have one for you.')
    random_number = randint(1, 10)
    # While-Loop counter "attempt" to make maximum 3 attempts possible
    attempt = 0
    # We put this outside Loop so that every new game attempts are equal to Zero and new random number is created.

    while True:
        # Need to make counter-check, and if attempt > 3 suggest to play again
        if attempt >= 3:
            print('You ran out of your 3 attempts. I won!')
            break

        guess = input('\tYour guess: ').strip()

        # One more chance to quit
        if guess == 'Q' or guess == 'q':
            print('Have a nice day!')
            quit()

        else:
            # Now it's good to check if number is within 1-10 range and actually is a number
            if guess.isdigit() and 0 < int(guess) <= 10:
                guess = int(guess)
                # It will check every incorrect attempt, but counting them to not reach over the limit of 3
                while guess != random_number:
                    print(f'No, it\'s not {guess}.')
                    attempt += 1
                    break
                # If guess is correct, we print a "Win-Message" and suggest to play again, to make game infinite
                else:
                    play_again = input(f'Your guess is correct, it\'s {random_number}. You won! \nPress [Enter] to continue')
                    break
            # if it's not number or not in 1-10 range, we suggest to enter number again
            else:
                print('Sorry, wrong input, try a number in range from 1 to 10.')
                continue

while play:
    play_suggest = input('Want to play the game with new number? [Y/N]: ').strip()
    if play_suggest == 'Y' or play_suggest == 'y':
        game()
    else:
        # Player can quit anytime during the game
        print('Have a nice day!')
        quit()