def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    flag = 0
    if x<0:
        x = -x
        flag = 1
    a_ = 0
    ans = []
    Max = 0xffffffff
    while True:
        m = divmod(x,10)
        x = m[0]
        ans.append(m[1])
        if x == 0:
            break
    #print(ans)
    while ans[0] == 0:
        ans.remove(ans[0])

    #print(ans)
    b = len(ans)
    c = 1
    for i in ans:
        a_ += i*(10**(b-c))
        c+=1
    if a_ > Max:
        return 0
    if flag:
        a_ = -a_
    return a_
print(reverse(1))