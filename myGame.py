import random

print('Welcome to my simple game!')
print('In this game you will predict the location of \'x\' between 3 given cups!')
print('Enjoy!')
print('[Cup  1][Cup  2][Cup  3]')
print('|      ||      ||      |')
print('|______||______||______|')

ball = [' ','x',' ']
random.shuffle(ball)
answer = ball.index('x')
user_loc = int(input("Choose between cup 1, 2, or 3: "))

if ball[user_loc - 1] == 'x':
	print('You win!')
else:
	print(f'You wrong! The ball is inside cup number {answer + 1}')
