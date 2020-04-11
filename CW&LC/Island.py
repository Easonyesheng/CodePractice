'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格
计算岛屿的数量
一个岛被水包围并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。
'''
# ACß

def numIslands(grid):
    h = len(grid[0]) # 列
    w = len(grid) # 行
    '''
    这里w和h的定义有些混淆，按英文意应该互换
    '''
    #print("**",w,"**",h)
    island_num = 0
    # get the label list to mark the already get one
    label = []
    for i in range(w*h):
        label.append(0)

    # firstly we set the 0s marked coz they don't need to find
    for i in range(w):
        for j in range(h):
            if grid[i][j] == 0:
                label[i*h+j] = 1
    # print(label)
    while(label.count(0)!=0):
        # find an island and mark it in label
        FindAnIsland(grid,label,w,h)

        island_num+=1
    
    return island_num
    

def FindAnIsland(islandmap,label,w,h):
    stack = []
    start = label.index(0)
    label[start] = 1
    i = int(start/h)
    j = start%h
    stack.append(i)
    stack.append(j)
    # 深度优先搜索    
    while(stack != []):
        #up
        if stack[0] == 0:
            pass
        else:
            if islandmap[stack[0]-1][stack[1]] == 1 and label[(stack[0]-1)*h+stack[1]] == 0:
                label[(stack[0]-1)*h+stack[1]] = 1
                stack.append(stack[0]-1)
                stack.append(stack[1])
        #down
        if stack[0]+1 == w:
            pass
        else:
            if islandmap[stack[0]+1][stack[1]] == 1 and label[(stack[0]+1)*h+stack[1]] == 0:
                label[(stack[0]+1)*h+stack[1]] = 1
                stack.append(stack[0]+1)
                stack.append(stack[1])
        #right
        if stack[1]+1 == h:
            pass
        else:
            if islandmap[stack[0]][stack[1]+1] == 1 and label[(stack[0])*h+stack[1]+1] == 0:
                label[(stack[0])*h+stack[1]+1] = 1
                stack.append(stack[0])
                stack.append(stack[1]+1)
        #left
        if stack[1] == 0:
            pass
        else:
            if islandmap[stack[0]][stack[1]-1] == 1 and label[(stack[0])*h+stack[1]-1] == 0:
                label[(stack[0])*h+stack[1]-1] = 1
                stack.append(stack[0])
                stack.append(stack[1]-1)
        # print(stack)
        # print('-----')
        stack.pop(0)
        stack.pop(0)










if __name__ == "__main__":
    a = []
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(eval(input("0 or 1: ")))
    #print(a)

    island = numIslands(a)
    print('There are ',island,'islands.')    