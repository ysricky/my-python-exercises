#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'm']
duplicate_item = []
for i in my_list:
    if my_list.count(i) > 1:
        if i not in duplicate_item:
            duplicate_item.append(i)
print(duplicate_item)