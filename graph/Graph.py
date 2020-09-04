#实现顶点Vertex类
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = []

    def addNeighbor(self,nbr,weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id)+"connected to:"+str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

#定义Graph类
class Graph:
    def __init__(self):
        self.vertList = {} #定义顶点的列表
        self.numVertices = 0 #顶点数量

    def addVertex(self,key):
        self.numVertices = self.numVertices+1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    #定义in操作
    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self,f,t,cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    #定义迭代函数方法
    def __iter__(self):
        return iter(self.vertList.values())
