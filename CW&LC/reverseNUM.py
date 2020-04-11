#测试回文数
def ispalindrome(x):
    x_ = str(x)
    xr = x_[::-1]
    #切片翻转字符串！
    return True if x_ == xr else False


print(ispalindrome(121))