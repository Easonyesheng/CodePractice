#human readable time


def make_readable1(seconds):
    if seconds < 60:
        ss = seconds
        mm = 0
        hh = 0
    elif seconds <= 59*60 + 59:
        mm = seconds//60
        ss = seconds - mm*60
        hh = 0
    elif seconds <= 99 * 3600 + 59*60 + 59:
        hh = seconds//3600
        mm = (seconds-(hh*3600))//60
        ss = seconds - mm*60 -hh*3600
    else:
        hh = 99
        mm = 59
        ss = 59
    
    print(ss)
    ss = comp(ss)
    mm = comp(mm)
    hh = comp(hh)

 
    return (str(hh)+':'+str(mm)+':'+str(ss))


def comp(num):
    if num < 10:
        return '0'+str(num)
    else:
        return str(num)





#from codewars!!!
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)
#this is fucking cooooool!


print(make_readable(359999))