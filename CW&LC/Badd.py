#给定两个二进制字符串，返回他们的和（用二进制表示）。
#输入为非空字符串且只包含数字 1 和 0。
def iszero(a):
    a = list(a)
    count = 0
    for i in a:
        if i == '0':
            count+=1
    if count == len(a):
        return True
    else:
        return False
    
def addBinary(a, b):
    #print(a)
    #print(b)
    a = a[::-1]
    b = b[::-1]
    if iszero(a):
        #rint(b,"!")
        return b
    if iszero(b):
        #print(a,"!")
        return a
    s = ""
    ls = list(b) if len(a) < len(b) else list(a)
    l = len(a) if len(a) < len(b) else len(b)
    la = len(a)
    lb = len(b)
    #print(ls[0])
    for i in range(l):
        if a[la-i-1] != b[lb-i-1]:
            #print(a[i],"*",b[i])
            ls[i] = '1'
        else:
            ls[i] = '0'
        #print(ls)
        if a[i] == '1' and b[i] == '1':
            s += '1'
        else:
            s += '0'
    #s = s[::-1]
   
    s += '0'
    s = s[::-1]
    #print(s) 
    ls = "".join(ls)
    ls = ls[::-1]
    
    return addBinary(ls,s)

print(addBinary('1','100'))
#print(iszero('0010'))