from pyamaze import maze,agent,textLabel,COLOR
from collections import deque

def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch=[]

    while len(frontier) > 0:
        currCell = frontier.popleft()
        if currCell == m._goal:
            break
        poss = 0
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)
                poss += 1
        if poss > 1:
            m.markCells.append(currCell)
    # print(f'{bfsPath}')
    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath

if __name__=='__main__':
    m=maze(7,7)
    m.CreateMaze(7,7,loadMaze='maze1.csv')
    bSearch,bfsPath,fwdPath=BFS(m,(5,1))
    a=agent(m,5,1,goal=(7,7),footprints=True,shape='square',color=COLOR.blue)
    b=agent(m,7,7,goal=(5,1),footprints=True,shape='square', color=COLOR.green)
    d=agent(m,5,1,color=COLOR.blue, filled=True)
    m.tracePath({a: bSearch},showMarked=True)
    m.tracePath({b: bfsPath})

    m.run()