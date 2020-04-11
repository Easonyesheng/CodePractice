def delete_nth1(order,max_e):
	l1 = []
	
	#print("order = ", order)
	
	[l1.append(i) for i in order if not i in l1]
	
	#print("l1 = ",l1)
	
	l2 = []
	for c in l1:
		l2.append(order.count(c))
	
	#print("l2 = ",l2)
	
	for i in range(0,len(l2)):
		while l2[i] - max_e > 0:
			order.reverse()
			order.remove(l1[i])
			#print(l1[i])
			order.reverse()
			l2[i] -= 1
	#print(order)
	
	return order


delete_nth1([1,1,3,3,7,2,2,2,2], 3)

	
#codewars:
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans