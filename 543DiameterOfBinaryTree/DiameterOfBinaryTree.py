"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
注意：两结点之间的路径长度是以它们之间边的数目表示。
"""

# Wrong
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root): 
        temp_node = []
        if root == None:
            return 0
        # judge leaf
        def judge_leaf(node):
            if node.left == None and node.right == None:
                return True
            return False

        # dfs function
        def search(node):
            if node == None or judge_leaf(node):
                return 0
            step = 0
            search_temp_node = []
            search_temp_node.append((node,0))
            while len(search_temp_node) != 0:
                # print(len(search_temp_node))
                temp, step =  search_temp_node.pop()
                if not judge_leaf(temp):
                    step += 1
                else:
                    continue
                if temp.left != None:
                    if not judge_leaf(temp.left):
                        search_temp_node.append((temp.left,step))
                if temp.right != None :
                    if not judge_leaf(temp.right):
                        search_temp_node.append((temp.right,step))
            # print("Search: ",node.val," has ",step)
            return step
        
        diameter = 0
        temp_node.append(root)
        while len(temp_node) != 0:
            d_temp_node = temp_node.pop()
            

            if judge_leaf(d_temp_node):
                continue
            new_way = 0
            if d_temp_node.left != None:
                new_way += (search(d_temp_node.left)+1)
            if d_temp_node.right != None:
                new_way += (search(d_temp_node.right)+1)
            
            diameter = max(diameter,new_way)

            if d_temp_node.left != None :
                if not judge_leaf(d_temp_node.left):
                    temp_node.append(d_temp_node.left)
            if d_temp_node.right != None: 
                if not judge_leaf(d_temp_node.right):
                    temp_node.append(d_temp_node.right)

            
        return diameter
    
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