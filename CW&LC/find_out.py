def find_outlier(list):
	a = list[0]%2
	b = list[1]%2
	c = list[2]%2
	if(a == b):
		flag = a
	elif(a == c):
		flag = a
	else:
		flag = b
		
	for num in list:
		if(num%2 != flag):
			N = num
	return N
	
M = find_outlier([2, 4, 6, 8, 10, 3])
print(M)

