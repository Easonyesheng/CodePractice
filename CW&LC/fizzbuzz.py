#fizz buzz question
def fizzBuzz(n):
    F = 'fizz'
    B = 'buzz'
    ls = []
    for i in range(n):

        f_ = ((i+1)%3 == 0)
        b_ = ((i+1)%5 == 0)
        b = " "
        #1:can be divided
        if (f_==1) or (b_ == 1):
            ls.append(f_*F +(f_+b_ == 2)*b +b_*B) 
        else:
            ls.append(str(i+1))
    return ls

print(fizzBuzz(15))