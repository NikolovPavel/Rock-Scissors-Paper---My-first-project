import random
player_move = input('Choose from: [S]cissors or [R]ock or [P]aper : ')
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

if player_move == 'S':
    player_move = scissors
elif player_move == 'R':
    player_move = rock
elif player_move == 'P':
    player_move = paper
else:
    print('Invalid input! Try again...')
    exit()
computer_move = random.randint(1, 3)

if computer_move == 1:
    computer_move = rock
elif computer_move == 2:
    computer_move = scissors
else:
    computer_move = paper
print(f'Computer: My choice is: {computer_move}')

if player_move == computer_move:
    print('Draw!')
elif (player_move == rock and computer_move == paper) or \
     (player_move == paper and computer_move == scissors) or \
     (player_move == scissors and computer_move == rock):
    print('You lose!')
else:
    print('You win !!!')
