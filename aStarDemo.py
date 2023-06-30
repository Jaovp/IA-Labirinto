from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
import math
# Função de Heurística - Distância de Manhattan
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))

# Função de Heurística - Distância euclidiana
#def h(cell1, cell2):
 #  x1, y1 = cell1
  # x2, y2 = cell2
   #return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
# Função A*
def aStar(m, start=None):
    if start is None:
        start = (m.rows, m.cols) 

    open = PriorityQueue()  # Fila de prioridade para armazenar os nós a serem explorados
    open.put((h(start, m._goal), h(start, m._goal), start))  # Insere o nó inicial na fila com seus custos
    aPath = {}  # Dicionário para armazenar os caminhos percorridos
    g_score = {row: float("inf") for row in m.grid} 
    g_score[start] = 0  # Define o custo g da célula inicial como 0
    f_score = {row: float("inf") for row in m.grid} 
    f_score[start] = h(start, m._goal)  # Define a pontuação f da célula inicial usando a heurística

    searchPath = [start]

    while not open.empty():
        currCell = open.get()[2]  # Obtém o próximo nó da fila (célula atual)
        searchPath.append(currCell)  # Adiciona a célula atual à lista de caminho percorrido

        if currCell == m._goal: #Condição de parada = Célula destino alcançada
            break 

        for d in 'ESNW':  # Verifica as direções possíveis
            if m.maze_map[currCell][d] == True:  # Verifica se é possível mover-se na direção atual
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)  
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)  
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])  
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])  
                temp_g_score = g_score[currCell] + 1  # Custo g atualizado para a próxima célula
                temp_f_score = temp_g_score + h(childCell, m._goal)  # Pontuação f atualizada para a próxima célula

                if temp_f_score < f_score[childCell]:
                    aPath[childCell] = currCell 
                    g_score[childCell] = temp_g_score  # Atualiza o custo g e pontuação f para a próxima célula
                    f_score[childCell] = temp_f_score  
                    open.put((f_score[childCell], h(childCell, m._goal), childCell))  # Insere a próxima célula na fila

    fwdPath = {} #Armazenamento dos dados de busca: estados visitados e caminho solucionado
    cell = m._goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]

    return searchPath, aPath, fwdPath

if __name__=='__main__':  #Função main para visualização do labirinto e agentes
    m = maze(7, 7)
    m.CreateMaze(7, 7, loadMaze='maze1.csv')

    searchPath, aPath, fwdPath = aStar(m, (5, 1))

    a=agent(m,5,1,goal=(7,7),footprints=True,shape='square',color=COLOR.blue)
    b=agent(m,7,7,goal=(5,1),footprints=True,shape='square', color=COLOR.green)
    d=agent(m,5,1,color=COLOR.blue, filled=True)
    m.tracePath({a: searchPath},showMarked=True)
    m.tracePath({b: aPath}, delay=200)

    m.run()
