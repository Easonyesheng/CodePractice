def duplicate_count(text):
	l = len(text)
	cup = []
	for i in range(l):
	 cup.append(text[i])
	count = []
	for i in range(i):
	 count.append(cup.count(cup[i]))
	return max(count)
	
	
	
duplicate_count('abbxd')