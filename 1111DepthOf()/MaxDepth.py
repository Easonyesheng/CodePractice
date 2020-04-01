"""
有效括号字符串 仅由 "(" 和 ")" 构成，并符合下述几个条件之一：

空字符串
连接，可以记作 AB（A 与 B 连接），其中 A 和 B 都是有效括号字符串
嵌套，可以记作 (A)，其中 A 是有效括号字符串
类似地，我们可以定义任意有效括号字符串 s 的 嵌套深度 depth(S)：

s 为空时，depth("") = 0
s 为 A 与 B 连接时，depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是有效括号字符串
s 为嵌套情况，depth("(" + A + ")") = 1 + depth(A)，其中 A 是有效括号字符串
例如：""，"()()"，和 "()(()())" 都是有效括号字符串，嵌套深度分别为 0，1，2，而 ")(" 和 "(()" 都不是有效括号字符串。

 

给你一个有效括号字符串 seq，将其分成两个不相交的子序列 A 和 B，且 A 和 B 满足有效括号字符串的定义（注意：A.length + B.length = seq.length）。

现在，你需要从中选出 任意 一组有效括号字符串 A 和 B，使 max(depth(A), depth(B)) 的可能取值最小。

返回长度为 seq.length 答案数组 answer ，选择 A 还是 B 的编码规则是：如果 seq[i] 是 A 的一部分，那么 answer[i] = 0。否则，answer[i] = 1。即便有多个满足要求的答案存在，你也只需返回 一个。

 

示例 1：

输入：seq = "(()())"
输出：[0,1,1,1,1,0]
示例 2：

输入：seq = "()(())()"
输出：[0,0,0,1,1,0,1,1]
 

提示：

1 <= text.size <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list:
        '''
        '''
        encode_list = [0]*len(seq)
        seq_ori = seq # origin seq
        depth = 1
        # depth = 1
        index_list = self.find_all_brakets(seq)
        for index in index_list:
            encode_list[index] = 1
            encode_list[index+1] = 1
        seq = seq.replace('()','')
        print('depth 1 encode list:',encode_list)

        while seq != '':
            index_list = self.find_all_brakets(seq)
            depth+=1
            print('depth',depth,' brakets index:', index_list)
            j = 0
            for i in range(len(index_list)):
                if i == 0: 
                    gap = index_list[i]
                    start = -1
                else: 
                    gap = index_list[i] - index_list[i-1] - 2
                    start = j
                
                
                loc = start # loc is the index of '('

                if gap == 0 and loc == 0:
                    pass
                else:
                    while gap >= 0:
                        loc+=1
                        if encode_list[loc] == 0:
                            gap-=1 
                        

                j = self.find_half_left(loc, seq_ori, encode_list)
                print(j)
                encode_list[j] = depth
                encode_list[loc] = depth
            seq = seq.replace('()','')
            print('depth ',depth,'encode list:',encode_list)

        # threshold = depth // 2
        for i in range(len(encode_list)):
            if encode_list[i] %2 == 0:
                encode_list[i] = 1
            else:
                encode_list[i] = 0

        return encode_list

    def find_all_brakets(self, seq):
        '''find all () and return index
        '''
        index_list = []
        index = seq.find('()')
        while index != -1:
            index_list.append(index)
            index = seq.find('()',index+1)
        
        return index_list

    def find_half_left(self, start, seq_ori, encode_list):
        '''find the ")"
        :para
            start: index of '(' in seq_ori
            seq_ori: original seq
            encode_list: encode list
        :output
            j: index of ')' in seq_ori
        '''
        j = 0
        i = start
        while j == 0:
            i+=1
            if seq_ori[i] == ')' and encode_list[i] == 0:
                j = i
        return j


if __name__ == "__main__":
    s = Solution()
    seq = "()(()())"
    print(s.maxDepthAfterSplit(seq))