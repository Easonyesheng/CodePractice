"""
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。

例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。

对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。

那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

 

示例：

输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/short-encoding-of-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# TIME OUT

class Solution:
    def minimumLengthEncoding(self, words) -> int:
        '''Solution
            A compressed string should be in the end of another longer string
            The final length should be the all_string_length - compressed_string_length + nums_of_unique_string
                unique_string_length + nums_of_unique_string
            First
                sort the words by length
            Second
                find unique string

        '''
        if not words : return 0
        final_length = 0
        nums_unique = 0
        word_length_dict = {}
        for word in words:
            word_length_dict.update({word:len(word)})
        # print(word_length_dict)
        sorted_words_set = sorted(word_length_dict.items() ,key=lambda x: x[1])
        sorted_words = [x[0] for x in sorted_words_set ]
        # print(sorted_words)
        for i in range(len(sorted_words)-1):
            # print(sorted_words[i])
            final_length += len(sorted_words[i])
            nums_unique += 1
            for j in range(i+1,len(sorted_words)):
                if not self.judge_unique(sorted_words[i],sorted_words[j]):
                    # print(sorted_words[i],sorted_words[j])
                    final_length -= len(sorted_words[i])
                    nums_unique -= 1
                    break
        return final_length+nums_unique+len(sorted_words[-1])+1


    def judge_unique(self,s1,s2):
        '''Judge whether s1 can be hidden in s2's end
            output:
                False means s1 is not unique
        '''
        # print('judge:',s1,s2)
        for i in range(1,len(s1)+1):
            if s1[-i] != s2[-i]:
                return True
        return False



if __name__ == "__main__":
    s = Solution()
    words = ['time','me','bell','ell','xcedr']
    # print(s.judge_unique('me','time'))
    print(s.minimumLengthEncoding(words))