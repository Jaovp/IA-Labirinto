from BFSDemo import BFS
from aStarDemo import aStar
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit
from DFSDemo import DFS

###########################
## Comparison One by One ##

# First Run this for BFS:
# m=maze(20,30)
# m.CreateMaze(loadMaze='mazeComparison1.csv')
# bSearch,bfsPath,fwdPath=BFS(m)


# l=textLabel(m,'BFS Distância',len(fwdPath)+1)
# l=textLabel(m,'BFS Espaços buscados',len(bSearch)+1)


# a=agent(m,footprints=True,color=COLOR.blue,filled=True)
# b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
# c=agent(m,footprints=True,color=COLOR.red)
# m.tracePath({a:bSearch},delay=1)
# m.tracePath({b:bfsPath},delay=100)
# m.tracePath({c:fwdPath},delay=100)

# m.run()


# Then run this for A*
# m=maze(20,30)
# m.CreateMaze(loadMaze='mazeComparison1.csv')
# aSearch,aPath,fwdPath=aStar(m)

# l=textLabel(m,'A* Distância',len(fwdPath)+1)
# l=textLabel(m,'A* Espaços buscados',len(aSearch)+1)

# a=agent(m,footprints=True,color=COLOR.blue,filled=True)
# b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
# c=agent(m,footprints=True,color=COLOR.red)
# m.tracePath({a:aSearch},delay=1)
# m.tracePath({b:aPath},delay=100)

# m.tracePath({c:fwdPath},delay=100)


# m.run()




###########################
## Combined Comparison ##

myMaze=maze(50,70)
myMaze.CreateMaze(1,59,loopPercent=100, loadMaze='mazeComparacao.csv')
# myMaze.CreateMaze()
searchPath,aPath,fwdPath=aStar(myMaze)
bSearch,bfsPath,fwdBFSPath=BFS(myMaze)
dSeacrh,dfsPath,dfwdPath=DFS(myMaze)


#l=textLabel(myMaze,'A* Distância',len(fwdPath)+1)
#l=textLabel(myMaze,'BFS Distância',len(fwdBFSPath)+1)
l=textLabel(myMaze,'DFS distancia',len(dfwdPath)+1)

#l=textLabel(myMaze,'A* Espaços buscados',len(searchPath)+1)
#l=textLabel(myMaze,'BFS Espaços buscados',len(bSearch)+1)
l=textLabel(myMaze,'DFS Espaços buscados',len(dSeacrh)+1)

a=agent(myMaze,footprints=True,color=COLOR.yellow)
b=agent(myMaze,footprints=True,color=COLOR.yellow)
c=agent(myMaze,footprints=True,color=COLOR.red,filled=True)
d=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)
e=agent(myMaze,footprints=True,color=COLOR.yellow)
f=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)
#myMaze.tracePath({c:searchPath},delay=1)
#myMaze.tracePath({b:fwdPath},delay=1)
#myMaze.tracePath({d:bSearch},delay=1)
#myMaze.tracePath({a:fwdBFSPath},delay=1)
myMaze.tracePath({f:dSeacrh},delay=5)
myMaze.tracePath({e:dfwdPath},delay=5)


#t1=timeit(stmt='aStar(myMaze)',number=10,globals=globals())
#t2=timeit(stmt='BFS(myMaze)',number=10,globals=globals())
t3=timeit(stmt='DFS(myMaze)',number=10,globals=globals())

#textLabel(myMaze,'A* Tempo',t1)
#textLabel(myMaze,'BFS Tempo',t2)
textLabel(myMaze,'DFS Tempo',t3)


myMaze.run()