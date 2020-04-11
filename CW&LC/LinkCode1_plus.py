#不使用加号来实现两个数相加。
'''
'^':异或运算，即为无进位的加法
‘&’：与运算，结果左移一位即为应该有的进位，将其与异或结果相加--递归直到与出来为0，则异或结果是相加结果
负数的处理：会溢出！==> python溢出时用&0xFFFFFFFF来避免溢出
'''
def aplus(a,b):
    mask = 0xFFFFFFFF
    while(b != 0):
        a1 =(a^b)&mask   
        b1 = ((a&b) << 1)&mask 
        a = a1
        b = b1
    return a 
    
def getSum(a, b):
    MAX = 0X7fffffff
    MIN = 0X80000000
    while b != 0 :
        a,b = a^b,(a&b)<<1
        print(" a = {0:b},b =  {1:b}".format(a,b))
    return a 
'''
--------------------- 
作者：mans-men 
来源：CSDN 
原文：https://blog.csdn.net/man_sion/article/details/72510284 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''

#处理了负数溢出问题的版本
def getSum_(a, b):
    MAX = 0x7FFFFFFF
    MIN = 0x80000000
    mask = 0xFFFFFFFF
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask #a&mask = a
        print(type(a))
        print(" a = {0:b},b =  {1:b}".format(a,b))
    return a if a <= MAX else ~(a^mask) #a^mask = ~a?

'''
--------------------- 
作者：mans-men 
来源：CSDN 
原文：https://blog.csdn.net/man_sion/article/details/72510284 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
print(aplus(1,-1))
#getSum_(-1,1)