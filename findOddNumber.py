def find_odd():
	odd_num = []
	for num in range(0,100):
		if num%2 == 0:
			odd_num.append(num)
	print(odd_num)
	print(len(odd_num))

find_odd()
