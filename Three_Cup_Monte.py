#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [' ','O',' ']


# In[2]:


from random import shuffle
import sys


# In[3]:


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# In[4]:


def player_guess():
    
    guess = ''
    
    while guess not in ['0','1','2']:
        guess = input('Please choose index number 0, 1, or 2:  ')
    
    return int(guess)


# In[5]:


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print(f'Correct!, {mylist}')
    else:
        print('You wrong!, the answer is {}'.format(mylist))


# In[6]:


def resume(play_game):
    ask = input("Type 'yes' to resume game, or 'no' to exit:  ")
    if ask == 'yes':
        play_game()
    else:
        pass


# In[7]:


def play_game():
    # INITIAL LIST
    mylist = [' ','O',' ']

    # SHUFFLE LIST
    mixedup = shuffle_list(mylist)

    # USER GUESS
    guess = player_guess()

    # CHECK GUESS
    check_guess(mixedup,guess)
    
    # RESTART GAME
    resume(play_game)


# In[8]:


play_game()

