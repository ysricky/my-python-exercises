import random
import os

#field
def show_field(pos):
	print('--------' + '[  ' + pos[22] + '  ]' + '--------')
	print('[  ' + pos[19] + '  ]' + '[  '+ pos[20] + '  ]' + '[  ' + pos[21] + '  ]')
	print('[  ' + pos[16] + '  ]' + '[  '+ pos[17] + '  ]' + '[  ' + pos[18] + '  ]')
	print('[  ' + pos[13] + '  ]' + '[  '+ pos[14] + '  ]' + '[  ' + pos[15] + '  ]')
	print('[  ' + pos[10] + '  ]' + '[  '+ pos[11] + '  ]' + '[  ' + pos[12] + '  ]')
	print('[  ' + pos[7] + '  ]' + '[  '+ pos[8] + '  ]' + '[  ' + pos[9] + '  ]')
	print('[  ' + pos[4] + '  ]' + '[  '+ pos[5] + '  ]' + '[  ' + pos[6] + '  ]')
	print('[  ' + pos[1] + '  ]' + '[  '+ pos[2] + '  ]' + '[  ' + pos[3] + '  ]')
	print('--------' + '[  ' + pos[0] + '  ]' + '--------')

pos = ['G1','D1','A1','A2','D1','D1','D1','D1','D2','D2','D2','D2','D2','D1','R ','D2','G2','D1','D1','D1','D2','D2','D2']

goal_one = 0
goal_two = 0

while True:
	os.system('clear')
	random.shuffle(pos)
	show_field(pos)
	if pos[16] == 'A1':
		goal_one += 1
		print('Player 1 GOAL!')
		print(f'SCORE: {goal_one} VS {goal_two}')
	elif pos[0] == 'A2':
		goal_two += 1
		print('Player 2 GOAL!')
		print(f'SCORE: {goal_one} VS {goal_two}')
	elif pos[0] == 'A1' and pos[22] == 'A2':
		print('FULL TIME!')
		print(f'SCORE: {goal_one} VS {goal_two}')
		break

