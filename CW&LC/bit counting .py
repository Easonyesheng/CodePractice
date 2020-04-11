# receive a integer than count the number of "1"s in it's binary form
#my :
def countBits(n):
    i = 0
    while n > 2:
        if n % 2 == 1:
            i = i + 1
            n = (n-1)/2
        else:
            n = n/2
    return (i + 1) if n != 0 else 0



