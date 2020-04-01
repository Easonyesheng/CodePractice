"""
要求划分出使得最大嵌套深度最小的分组，我们首先得知道如何计算嵌套深度。我们可以通过栈实现括号匹配来计算：

维护一个栈 s，从左至右遍历括号字符串中的每一个字符：

如果当前字符是 (，就把 ( 压入栈中，此时这个 ( 的嵌套深度为栈的高度；

如果当前字符是 )，此时这个 ) 的嵌套深度为栈的高度，随后再从栈中弹出一个 (。

下面给出了括号序列 (()(())()) 在每一个字符处的嵌套深度：
括号序列   ( ( ) ( ( ) ) ( ) )
下标编号   0 1 2 3 4 5 6 7 8 9
嵌套深度   1 2 2 2 3 3 2 2 2 1 



作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/solution/you-xiao-gua-hao-de-qian-tao-shen-du-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list(int):
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            if c == ')':
                ans.append(d % 2)
                d -= 1
        return ans
