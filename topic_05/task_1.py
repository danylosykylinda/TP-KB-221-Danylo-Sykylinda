from random import choice

def game():
    player = 0
    program = 0

    while True:
        choice_player = input("What's your choice?(stone, scissors or paper) or end game(q): ")
        choice_program = choice(['stone', 'scissors', 'paper'])
        if choice_player == choice_program:
            print(f"It's draw! Score: {player}:{program}")
        elif (choice_player == 'stone' and choice_program == 'scissors') or (choice_player == 'scissors' and choice_program == 'paper') or (choice_player == 'paper' and choice_program == 'stone'):
            player = player + 1
            print(f"You won! Score: {player}:{program}")
        elif (choice_program == 'stone' and choice_player == 'scissors') or (choice_program == 'scissors' and choice_player == 'paper') or (choice_program == 'paper' and choice_player == 'stone'):
            program = program + 1
            print(f"You lost! Score: {player}:{program}")
        elif choice_player == 'q':
            print(f'Bye! Score: {player}:{program}')
            break
        else:
            print("You entered something wrong! Try again!")

while True:
    consent = input("Hello! Do you wanna play the game 'stone, scissors, paper'?(y or n): ")
    if consent == 'y':
        game()
        break
    elif consent == 'n':
        print("Bye!")
        break
    else:
        print('You entered something wrong! Try again, please!')
