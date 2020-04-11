class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if str == []:
            return str
        l = len(str) #5
        #print(l)
        if offset < 0 :
            return "Input Error."

      

        if offset > l:
            offset = offset - l * int(offset/l)

        m = l - offset  #numbers of str need to move
        for i in range(offset):
            a = str[l - offset + i]
            for j in range(m):
                str[l - offset - j + i] = str[l - offset - j - 1 + i]
            str[i] = a
        return str


M = Solution()
str = ['a','b','c','d','e']
print(M.rotateString("",2))