"""
给定一个字符串，逐个翻转字符串中的每个单词。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
            1. remove other blanks
            2. switch every words
        '''
        words = []
        s = s.replace('\xa0',' ')
        l = len(s)
        if l == 1: return s.replace(' ','')
        # get the list
        i = 0
        j = 0
        while i<l:
            if s[i] != ' ':
                print(i,s[i])
                if i == l-1:
                    words.append(s[i:])
                for j in range(i+1,l):
                    if s[j] == ' ':
                        words.append(s[i:j])
                        i = j
                        break
                    if j == l-1:
                        words.append(s[i:j+1])
                        i = j
                        break
                    
            i+=1
        
        words_s = words[::-1]
        print(words_s)
        sw = ' '.join(words_s)
        return sw


if __name__ == "__main__":
    s = Solution()
    c = s.reverseWords(" a")
    print('c:',c)