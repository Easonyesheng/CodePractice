#it's so hard 
#I don't know how to solve this kata 


def next_smaller(n):
    l1 = list(map(int,str(n)))
    lenth = len(l1)
    if lenth == 1:
        return -1
    
    l_sorted = []
    l_sorted = sorted(l1)
    order = []
    for i in l1:
        order.append(l_sorted.index(i))
    print('sorted num: ',l_sorted)    
    print('sort: ',order)
    print('orgin num: ',l1)
    if l1 == l_sorted:
        return -1
    m,h = fin(order,lenth)
    tmp = l1[m]
    l1[m] = l1[h]
    l1[h] = tmp
    num = list(map(str,l1))
    num = "".join(num)
    num = int(num)
    return(num)
    
    
    






def fin(order,lenth):
    for i in range(lenth-1,-1,-1):
        for j in range(i-1,-1,-1):
            #print (i,j)
            if order[i] < order[j]:
                m = i
                h = j
                return m,h



#fin([2,3,1,4,5],len([2,3,1,4,5]))
print(next_smaller(2017))