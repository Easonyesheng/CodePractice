'''
def zero(list = None):
    if list == None:
        return 0
    elif list[0] == 'a':
        return 0 + list[1]
    elif list[0] == 'b':
        return 0 - list[1]
    elif list[0] == 'c':
        return 0 * list[1]
    elif list[0] =='d':
        return int(0 / list[1])

def one(list = None):
    if list == None:
        return 1
    elif list[0] == 'a':
        return 1 + list[1]
    elif list[0] == 'b':
        return 1 - list[1]
    elif list[0] == 'c':
        return 1 * list[1]
    elif list[0] =='d':
        return int(1 / list[1])

def two(list = None):
    if list == None:
        return 2
    elif list[0] == 'a':
        return 2 + list[1]
    elif list[0] == 'b':
        return 2 - list[1]
    elif list[0] == 'c':
        return 2 * list[1]
    elif list[0] =='d':
        return int(2 / list[1])

def three(list = None):
    if list == None:
        return 3
    elif list[0] == 'a':
        return 3 + list[1]
    elif list[0] == 'b':
        return 3 - list[1]
    elif list[0] == 'c':
        return 3 * list[1]
    elif list[0] =='d':
        return int(3 / list[1])

def four(list = None):
    if list == None:
        return 4
    elif list[0] == 'a':
        return 4 + list[1]
    elif list[0] == 'b':
        return 4 - list[1]
    elif list[0] == 'c':
        return 4 * list[1]
    elif list[0] =='d':
        return int(4 / list[1])

def five(list = None):
    if list == None:
        return 5
    elif list[0] == 'a':
        return 5 + list[1]
    elif list[0] == 'b':
        return 5 - list[1]
    elif list[0] == 'c':
        return 5 * list[1]
    elif list[0] =='d':
        return int(5 / list[1])

def six(list = None):
    if list == None:
        return 6
    elif list[0] == 'a':
        return 6 + list[1]
    elif list[0] == 'b':
        return 6 - list[1]
    elif list[0] == 'c':
        return 6 * list[1]
    elif list[0] =='d':
        return int(6 / list[1])

def seven(list = None):
    if list == None:
        return 7
    elif list[0] == 'a':
        return 7 + list[1]
    elif list[0] == 'b':
        return 7 - list[1]
    elif list[0] == 'c':
        return 7 * list[1]
    elif list[0] =='d':
        return int(7 / list[1])

def eight(list = None):
    if list == None:
        return 8
    elif list[0] == 'a':
        return 8 + list[1]
    elif list[0] == 'b':
        return 8 - list[1]
    elif list[0] == 'c':
        return 8 * list[1]
    elif list[0] =='d':
        return int(8 / list[1])

def nine(list = None):
    if list == None:
        return 9
    elif list[0] == 'a':
        return 9 + list[1]
    elif list[0] == 'b':
        return 9 - list[1]
    elif list[0] == 'c':
        return 9 * list[1]
    elif list[0] =='d':
        return int(9 / list[1])

def plus(num):
    list = ['a',num]
    return list

def minus(num):
    list = ['b',num]
    return list

def times(num):
    list = ['c',num]
    return list

def divided_by(num):
    if num == 0:
        return "wrong"
    list = ['d',num]
    return list
'''


#codewars

def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y

#print(zero(plus(two())))
#lambda is coooooo!
