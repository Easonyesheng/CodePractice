def f_max(lis,s,e):
    a = []
    b = []
    b.append(s)
    b.append(e)
    s = min(b)
    e = max(b)
    if s == e:
        return lis[s-1]
    for i in range(e-s+1):
        
        a.append(lis[s-1+i])

    print(a)
    return max(a)



s_num,times = input().split(' ')
score = input().split(' ')
for i in range(int(times)):
    ope = input().split(' ')
    if ope[0] == 'Q':
        max_ = f_max(score,int(ope[1]),int(ope[2]))
        print(max_)

    if ope[0] == 'U':
        score[int(ope[1])-1] = ope[2]
        print(score)
