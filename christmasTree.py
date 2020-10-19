#Exercise! Christmas Tree!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
#you can use this (list comprehension)
for list in picture:
    str1 = ' '.join(('*' if i == 1 else ' ') for i in list)
    print(str1)

#or this

for list in picture:
    for i in list:
        if i:
            print('*', end=' ')#normally print function will start a new line after execution, so use 'end'
        else:
            print(' ', end=' ')
    print('')#to override 'end' in print function so the string will not be printed horizontally