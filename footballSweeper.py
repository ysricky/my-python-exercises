import random

#field
def show_field(pos):
	print('-------' + '[  ' + pos[16] + '  ]' + '-------')
	print('[  ' + pos[13] + '  ]' + '[  '+ pos[14] + '  ]' + '[  ' + pos[15] + '  ]')
	print('[  ' + pos[10] + '  ]' + '[  '+ pos[11] + '  ]' + '[  ' + pos[12] + '  ]')
	print('[  ' + pos[7] + '  ]' + '[  '+ pos[8] + '  ]' + '[  ' + pos[9] + '  ]')
	print('[  ' + pos[4] + '  ]' + '[  '+ pos[5] + '  ]' + '[  ' + pos[6] + '  ]')
	print('[  ' + pos[1] + '  ]' + '[  '+ pos[2] + '  ]' + '[  ' + pos[3] + '  ]')
	print('-------' + '[  ' + pos[0] + '  ]' + '-------')

pos = [' ','D','1','2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

goal_one = 10
goal_two = 0

while True:

	random.shuffle(pos)
	show_field(pos)
	if pos[16] == '1':
		goal_one += 1
		print('Player 1 GOAL!')
		print(f'SCORE: {goal_one} VS {goal_two}')
	elif pos[0] == '2':
		goal_two += 1
		print('Player 2 GOAL!')
		print(f'SCORE: {goal_one} VS {goal_two}')
	elif goal_one < goal_two:
		print(f'SCORE: {goal_one} VS {goal_two}')
		break

