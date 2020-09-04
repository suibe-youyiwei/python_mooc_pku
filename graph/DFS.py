#解决骑士周游问题算法
#生成合法走棋位置
def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)] #马走日的八个格子
    for i in moveOffsets:
        newX = x+i[0]
        newY = y+i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize): #判断移动位置是否合理
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x>0 and x<bdSize:
        return True
    else:
        return False

#构建走棋关系图
from graph import Graph
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row,col,bdSize) #编号
            newPositions = genLegalMoves(row,col,bdSize) #合法走棋走到的位置
            for e in newPositions:
                nid = posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid) #建立节点与边
    return ktGraph

def posToNodeId(row,col,bdSize):
    return row*bdSize+col


#深度优先搜索
def knightTour(n,path,u,limit):
    u.setColor('grey')
    path.append(u)
    if n<limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i<len(nbrList) and not done:
            if nbrList[i].getColor() == "white":
                done = knightTour(n+1,path,nbrList[i],limit)
            i+=1
        if not done:
            path.pop()
            u.setColor("white")
    else:
        done = True
    return done