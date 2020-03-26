"""
在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。

车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。

返回车能够在一次移动中捕获到的卒的数量。

输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
输出：3
解释：
在本例中，车能够捕获所有的卒。

示例 2：
输入：[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
输出：0
解释：
象阻止了车捕获任何卒。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/available-captures-for-rook
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import numpy as np 

class Solution:
    def numRookCaptures(self, board) -> int:
        '''
        '''
        pawns = 0
        pawn_list_h = []
        bishop_list_h = []
        pawn_list_v = []
        bishop_list_v = []
        check_board = np.array(board)
        # print(check_board.shape)

        pawn_loc = np.argwhere(check_board == 'p')
        rook_loc = np.argwhere(check_board == 'R')
        bishop_loc = np.argwhere(check_board == 'B')
        # print(bishop_loc[:,1])

        # horizontal
        pawn_h = np.argwhere(pawn_loc[:,0] == rook_loc[0,0]) # pawns in the same horizon with rock
        # print(pawn_loc[pawn_h])
        for i in range(pawn_h.shape[0]):
            pawn_list_h.append(pawn_loc[pawn_h][i][0][1])

        bishop_h = np.argwhere(bishop_loc[:,0] == rook_loc[0,0]) # bishops ..
        # print(bishop_h) 
        for i in range(bishop_h.shape[0]):
            bishop_list_h.append(bishop_loc[bishop_h][i][0][1])
        if pawn_list_h:
            if not bishop_list_h : 
                # print(pawn_list_h)
                if min(pawn_list_h) < rook_loc[0,1]:
                    pawns+=1
                if max(pawn_list_h) > rook_loc[0,1]:
                    pawns+=1
            else:
                blh_left = [i-rook_loc[0,1] for i in bishop_list_h if i-rook_loc[0,1]<=0]
                plh_left = [i-rook_loc[0,1] for i in pawn_list_h if i-rook_loc[0,1]<=0]
                if not blh_left and plh_left: pawns+=1
                if (blh_left and plh_left) and max(blh_left) < max(plh_left) : pawns+=1
                blh_right = [i-rook_loc[0,1] for i in bishop_list_h if i-rook_loc[0,1]>0]
                plh_right = [i-rook_loc[0,1] for i in pawn_list_h if i-rook_loc[0,1]>0]
                if not blh_right and plh_right: pawns+=1
                if (blh_right and plh_right) and min(blh_right) > min(plh_right) : pawns+=1
                
        print('h',pawns)
        # vertical
        pawn_v = np.argwhere(pawn_loc[:,1] == rook_loc[0,1])
        # print(pawn_v)
        for i in range(pawn_v.shape[0]):
            # print('$',pawn_loc[pawn_v])
            pawn_list_v.append(pawn_loc[pawn_v][i][0][0])
            
        bishop_v = np.argwhere(bishop_loc[:,1] == rook_loc[0,1])
        # print(bishop_v)
        for i in range(bishop_v.shape[0]):
            # print(bishop_v)
            # print(bishop_loc[bishop_v].shape)
            bishop_list_v.append(bishop_loc[bishop_v][i][0][0])
        if pawn_list_v:
            if not bishop_list_v : 
                # print(pawn_list_v)
                if min(pawn_list_v) < rook_loc[0,0]:
                    pawns+=1
                if max(pawn_list_v) > rook_loc[0,0]:
                    pawns+=1
            else:
                blh_up = [i-rook_loc[0,0] for i in bishop_list_v if i-rook_loc[0,0]<=0]
                plh_up = [i-rook_loc[0,0] for i in pawn_list_v if i-rook_loc[0,0]<=0]
                # print(blh_up)
                # print(plh_up)
                if not blh_up and plh_up: pawns+=1
                if (blh_up and plh_up) and max(blh_up) < max(plh_up) : pawns+=1
                blh_down = [i-rook_loc[0,0] for i in bishop_list_v if i-rook_loc[0,0]>0]
                plh_down = [i-rook_loc[0,0] for i in pawn_list_v if i-rook_loc[0,0]>0]
                if not blh_down and plh_down: pawns+=1
                if (blh_down and plh_down) and min(blh_down) > min(plh_down) : pawns+=1


        return pawns

if __name__ == "__main__":
    s = Solution()
    board = [[".",".",".",".",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             ["p","p",".",".",".","p","B","."],
             [".",".",".",".",".",".",".","."],
             [".",".",".","B","R",".",".","."],
             [".",".",".","p",".",".",".","."],
             [".",".",".",".",".",".",".","."]]
    print(s.numRookCaptures(board))