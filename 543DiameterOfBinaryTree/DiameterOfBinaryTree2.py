"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
注意：两结点之间的路径长度是以它们之间边的数目表示。
"""

# 用递归算法
# 考虑节点而不是边
# 两条简单的规则作为基础
#   1. diameter_of_tree(Node) = depth_of_nodes(Node.left)+depth_of_nodes(Node.right) + 1
#   2. depth_of_nodes(root) = max(depth_of_nodes(root.left),depth_of_nodes(root.right)) + 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root): 
        
        self.diam = 0

        def depth(node):
            '''
            calculate the numbers of nodes of the node
            '''
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.diam = max(self.diam,L+R)
            # print(int(node.left!=None or node.right!=None))
            return max(L,R)+ 1
        
        depth(root)
        return self.diam 



if __name__ == "__main__":
    node = dict()
    for i in range(20):
        node[str(i)] = TreeNode(i)
    
    node['1'].left = node['2']
    # node['1'].right = node['3']
    node['2'].left = node['4']
    node['2'].right = node['5']
    # node['3'].left = node['6']
    node['4'].left = node['7']
    node['5'].right = node['8']
    node['7'].left = node['9']
    node['9'].left = node['10']
    s = Solution()
    
    print(s.diameterOfBinaryTree(node['1']))