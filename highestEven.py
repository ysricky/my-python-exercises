def highest_even(list):
	even_num = [i for i in list if i%2 == 0] # using if with list comprehension
	return max(even_num)

print(highest_even([1,2,3,4,5,6,7,8,9,10]))