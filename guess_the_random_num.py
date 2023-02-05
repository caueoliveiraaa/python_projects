import random
from termcolor import colored
import os


def guess_number_game():
    game_on = True
    while game_on:
        try:
            # Get random number limitors
            os.system('cls')
            print('\n###### GUESS THE NUMBER ######\n')
            max_num = int(input('Enter the max limit: '))
            min_num = int(input('Enter the min limit: '))

            if max_num > min_num:
                if (max_num - min_num) > 10:
                    # Display the limitors
                    ran_num = random.randint(min_num, max_num)
                    print(f'\nYou will have to guess a number between {min_num} and {max_num}!')
                    print('You will have 10 attempts to guess it correctly!')

                    # Check if input number is equal to random number
                    attempt = 0
                    while attempt < 10:
                        attempt += 1
                        print(f'\nAttempt {attempt}')
                        try:
                            guess_num = int(input('Enter your guess number: '))
                            if guess_num > max_num or guess_num < min_num:
                                print(f'Inform a number with the range: {min_num} and {max_num}')

                            elif guess_num < ran_num:
                                print(f'You guessed a small number!')

                            elif guess_num > ran_num:
                                print(f'You guessed a large number!')
                                
                            elif guess_num == ran_num:
                                print(f'\nCONGRATULATIONS!!! You guessed the right number! # {guess_num}')
                                answer = input('Do you wish to play again?\ntype yes to continue playing:\n')
                                answer = answer.lower()

                                if 'yes' in answer:
                                    attempt = 0
                                    break
                                else:
                                    game_on = False
                                    break

                            if attempt == 10:
                                game_on = False
                                print('\nYou have run out of changes!')
                                print(f'The number was # {ran_num}!\nBetter luck next time!')
                                answer = input('Do you wish to play again?\ntype yes to continue playing:\n')
                                answer = answer.lower()

                                if 'yes' in answer:
                                    attempt = 0
                                    break
                                else:
                                    game_on = False
                                    break

                            elif attempt == 9:
                                print(f'\nWARNING: This is your LAST chance!')
                                
                        except KeyboardInterrupt:
                            os.system('cls')
                            print('You have quit the game!')
                            quit()
                        except:
                            print(f'Try informing a number between {min_num} and {max_num}')

                else:
                    os.system('cls')
                    print('The difference between the highest number and the lowest number')
                    print('needs to be more than 10, because there are only 10 guesses!\n')

            else:
                os.system('cls')
                print('The first number needs to be higher than the second number.')

        except KeyboardInterrupt:
            os.system('cls')
            print('You have quit the game!')
            quit()

        except Exception as e:
            os.system('cls')
            print(f'An error occurred: {e}')
            print('Try to inform two whole numbers!')
            print('The first one being higher than the second!')


if __name__ == '__main__':
    os.system('cls')
    guess_number_game()