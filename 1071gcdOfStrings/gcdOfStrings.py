"""
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str):
        '''
            first calculate all the common divisor(cd) of str length
            use str.replace(str2,'') == ''
        '''

        # get the length
        L1 = len(str1)
        L2 = len(str2)

        if L1 == 0 or L2 == 0:
            return ''

        L_short = min(L1,L2)
        L_long = max(L1,L2)
        str_short = str1 if L1<L2 else str2
        str_long = str2 if L2>L1 else str1

        cd_list = []

        #get the length-cd list
        for i in range(1,L_short+1):
            if (L_short%i==0) and (L_long%i==0):
                cd_list.append(i)
        cd_list = cd_list[::-1]
        
        # get the str gcd
        for cd in cd_list:
            if str_short.replace(str_short[:cd],'') != '':
                continue
            else:
                if str_long.replace(str_short[:cd],'') != '':
                    continue
                else:
                    return str_short[:cd]
        return ''

if __name__ == "__main__":
    s = Solution()
    str1 = "ABABABABABA"
    str2 = "AB"
    print(s.gcdOfStrings(str1,str2))




