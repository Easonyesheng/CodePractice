def longest_consec1(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    a = ""
    lenth = len(strarr)
    sub_len = []
    sub_len2 = []
    times = lenth-k+1
    for i in range(lenth):
     sub_len.append(len(strarr[i]))
    for i in range(times):
     b = 0
     for j in range(i,k+i):
      b =b + sub_len[j]
     sub_len2.append(b)
    
    
    flag = sub_len2.index(max(sub_len2))
    for i in range(flag,flag+k):
     a += strarr[i]
    
    return a
str =["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
str1 = ["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"]
longest_consec(str1,2)

#codewars download
def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""
