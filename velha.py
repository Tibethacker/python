###########################################
#										  #
#		      Jogo da Velha 			  #
#										  #
###########################################

import random

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,4,9], [3,4,7]]
over = False

def board_show():
	count = 1

	for i in board:
		if count % 3 == 0:
			print i
		else:
			print i,
		count = count + 1

def player_time():
	move = raw_input('Digite um numero: ')
	for i in board:
		if int(move) == i:
			board[i - 1] = 'o';

def machine_time():
	move = random.randint(1, 9)
	
	if board[move - 1] == 'o':
		machine_time()
	
	for i in board:
		if move == i:
			board[i - 1] = 'x'

def check_game():
	global over

	for i in win:
		if board[i[0] - 1] == 'o' and board[i[1] - 1] == 'o'  and board[i[2] - 1] == 'o':
			print 'Player ganhou'
			over = True

		elif board[i[0] - 1] == 'x' and board[i[1] - 1] == 'x' and board[i[2] - 1] == 'x':
			print 'Maquina ganhou'
			over = True

board_show()

while over == False:
	player_time()
	machine_time()
	board_show()
	check_game()