"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:

 输入："aabcccccaaa"
 输出："a2b1c5a3"
示例2:

 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
提示：

字符串长度在[0, 50000]范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compress-string-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# force 

class Solution:
    def compressString(self, S: str) -> str:
        '''
        '''
        if not S: return ''
        if len(S)<=2: return S 
        def get_top_part(S):
            '''get the top repeat part

            '''
            if not S: return -1
            # print(S)
            temp = S[0]
            count = 1
            for i in range(1,len(S)):
                if S[i] == S[i-1]:
                    count += 1
                else:
                    return temp+str(count)
            return temp+str(count)
        
        i = 0
        ori_l = len(S)
        comp_S = ''
        while i < len(S):
            get = get_top_part(S[i:])
            # print('get: ',get)
            if get == -1: break
            comp_S += get
            step = int(get[1:])
            i += step
        
        if len(comp_S) < ori_l:
            return comp_S
        else:
            return S

if __name__ == "__main__":
    s = Solution()
    S = "ab"
    print(s.compressString(S))